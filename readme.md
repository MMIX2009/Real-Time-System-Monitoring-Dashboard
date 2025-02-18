This is a **real-time system monitoring dashboard** built with **Streamlit**. 

Here's a summary of how it works:

### 🚀 **Application Flow**

1. **Initialization**  
   - The app starts with `streamlit.set_page_config()` to set the title and layout.  
   - It displays a **title** and initializes **empty placeholders** for five charts:  
     - **RAM Usage**  
     - **CPU Usage**  
     - **Disk Usage**  
     - **Network Traffic (Sent/Received)**  
     - **GPU Usage**  

2. **Data Acquisition**  
   The app uses the `psutil` library to gather system performance data:  
   - **RAM**: `psutil.virtual_memory().percent`  
   - **CPU**: `psutil.cpu_percent(interval=1)`  
   - **Disk**: `psutil.disk_usage('/').percent`  
   - **Network**: `psutil.net_io_counters()` to get **sent** and **received** bytes (converted to MB).  
   - **GPU**: Attempts to access `psutil.sensors_temperatures()` for GPU temperature.

3. **Data Processing**  
   - Collected metrics are stored in a **Pandas DataFrame**.  
   - The dataframe retains the **last 50 records** to avoid performance issues.

4. **Visualization**  
   - `plotly.express` is used to generate dynamic **line charts** for each metric.  
   - These charts **update every 5 seconds** using `time.sleep(5)`.

5. **Deployment Considerations**  
   - When run locally, the app monitors the **local machine's performance**.  
   - When deployed on **Streamlit Cloud**, it monitors the **server's performance**.

### 🛠️ **User Interaction**  
- Open the dashboard with **`streamlit run app.py`** locally.  
- Access the dashboard via a **URL** when deployed to Streamlit Cloud.

Would you like suggestions for optimization or additional features? 😊
