import streamlit as st
import psutil
import time
import pandas as pd
import plotly.express as px

# Initialize Streamlit app
st.set_page_config(page_title="Real-Time System Monitoring Dashboard", layout="wide")

# Title of the dashboard
st.title("📊 Real-Time System Monitoring Dashboard")

# Placeholder for dynamic charts
ram_chart = st.empty()
cpu_chart = st.empty()
disk_chart = st.empty()
network_chart = st.empty()
gpu_chart = st.empty()

# Initialize data storage
data = pd.DataFrame(columns=["Time", "RAM", "CPU", "Disk", "Network Sent", "Network Received", "GPU Usage"])

# Update data and display charts every second
while True:
    # Fetch system stats
    current_time = time.strftime("%H:%M:%S")
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    network_sent = net_io.bytes_sent / (1024 * 1024)  # MB
    network_received = net_io.bytes_recv / (1024 * 1024)  # MB

    # GPU usage (if available)
    try:
        gpu_usage = psutil.sensors_temperatures().get('gpu', [None])[0].current if psutil.sensors_temperatures().get('gpu') else 0
    except Exception:
        gpu_usage = 0

    # Append new data to the dataframe
    new_row = pd.DataFrame({
        "Time": [current_time],
        "RAM": [ram],
        "CPU": [cpu],
        "Disk": [disk],
        "Network Sent": [network_sent],
        "Network Received": [network_received],
        "GPU Usage": [gpu_usage]
    })
    data = pd.concat([data, new_row], ignore_index=True)

    # Limit the dataframe to the last 50 records for better performance
    data = data.tail(50)

    # Plot RAM usage
    ram_fig = px.line(data, x="Time", y="RAM", title="RAM Usage (%)", markers=True)
    ram_chart.plotly_chart(ram_fig, use_container_width=True)

    # Plot CPU usage
    cpu_fig = px.line(data, x="Time", y="CPU", title="CPU Usage (%)", markers=True)
    cpu_chart.plotly_chart(cpu_fig, use_container_width=True)

    # Plot Disk usage
    disk_fig = px.line(data, x="Time", y="Disk", title="Disk Usage (%)", markers=True)
    disk_chart.plotly_chart(disk_fig, use_container_width=True)

    # Plot Network usage
    network_fig = px.line(data, x="Time", y=["Network Sent", "Network Received"], title="Network Traffic (MB)", markers=True)
    network_chart.plotly_chart(network_fig, use_container_width=True)

    # Plot GPU usage
    gpu_fig = px.line(data, x="Time", y="GPU Usage", title="GPU Usage (°C)", markers=True)
    gpu_chart.plotly_chart(gpu_fig, use_container_width=True)

    time.sleep(5)  # Update every 5 seconds
