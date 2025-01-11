**Project: Network Sensor on Flask**

This project is a prototype of a network sensor that allows you to monitor the status of network interfaces as well as the system where the sensor is located. It uses Flask to provide a web interface through which you can track network data and system activity. The sensor will be useful for real-time network monitoring and system performance analysis.

### **What the project does:**

- **Network Interface Monitoring**: The sensor allows you to track the status and activity of network interfaces in the system (e.g., Ethernet, Wi-Fi).
- **System Monitoring**: In addition to monitoring network interfaces, the project also tracks system performance metrics such as CPU usage, memory usage, and other resources.
- **Web Interface**: All data is displayed through a web page, enabling remote monitoring of the network and system status.

### **Steps to Run the Project:**

1. **Clone the repository to your local machine**  
   Copy the project to your directory by running the following command:
   ```bash
   git clone https://github.com/disciplined-pioneer/Network-scanner-on-flask.git
   ```

2. **Navigate to the repository folder**  
   Open a terminal and run the command:
   ```bash
   cd Network-scanner-on-flask
   ```

3. **Make sure Python is installed**  
   Check if Python is installed by running the command:
   ```bash
   python --version
   ```
   If Python is not installed, download and install it from the official website.

4. **Create a virtual environment**  
   Create a virtual environment to isolate the project dependencies:
   ```bash
   python -m venv venv
   ```

5. **Activate the virtual environment**  
   To activate the virtual environment, run the following command:
   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **On Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

6. **Install dependencies**  
   Install the necessary dependencies listed in the `requirements.txt` file using the command:
   ```bash
   pip install -r requirements.txt
   ```

7. **Run the project**  
   After installing the dependencies, start the Flask server with:
   ```bash
   flask run
   ```

   The application will be available at:
   ```
   http://127.0.0.1:5000
   ```

### **Application Functionality:**

- **Dashboard**: The web page displays key data about network interfaces and system activity.
- **Data Refresh**: The sensor will automatically update data, providing real-time information on network status.
- **Charts and Tables**: The project can display graphs of network interface and system load in real-time.

### **Usage:**
Once the web server is running, open your browser and go to `http://127.0.0.1:5000` to start using the application. You will see an interface for monitoring network data and system status.
