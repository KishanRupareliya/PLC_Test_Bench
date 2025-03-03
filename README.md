📌 Project Overview

This project is a PLC Test Bench Web Dashboard that collects real-time PLC data, including:

Motor speed

Temperature

Vibration levels

Energy consumption

System status

It displays the data in a real-time interactive web dashboard using Flask and Chart.js.

🚀 Features

✅ Real-time Data Streaming from PLC
✅ Live Charts & Graphs (Chart.js)
✅ REST API Endpoint (/api/data) for JSON Data
✅ Web Interface (/dashboard) to Monitor PLC Metrics
✅ AWS IoT Integration (Optional for MQTT & S3 Uploads)

🛠 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-repo/plc-test-bench-dashboard.git
cd plc-test-bench-dashboard

2️⃣ Install Dependencies

Ensure Python is installed (Python 3.7+ required). Then, install Flask and other required libraries:

pip install flask chart.js boto3 paho-mqtt

3️⃣ Run the PLC Web Dashboard

python plc_web_dashboard.py

✅ Expected Output:

 * Running on http://127.0.0.1:5001
 * Running on http://192.168.x.x:5001

4️⃣ Open the Dashboard in a Browser

http://127.0.0.1:5001/dashboard

If accessing from another device, use:

http://192.168.x.x:5001/dashboard

🖥 API Endpoints

Endpoint

Method

Description

/api/data

GET

Fetch real-time PLC sensor data in JSON format

/dashboard

GET

Web dashboard with charts

📌 Example API Response (/api/data):

{
    "motor_running": true,
    "motor_speed": 1200,
    "temperature": 45,
    "vibration_level": 0.5,
    "energy_consumption": 12.3,
    "torque": 4.5,
    "system_status": "Running"
}

📡 AWS IoT & S3 Integration (Optional)

1️⃣ Configure AWS Credentials

aws configure

Provide:

AWS Access Key ID

AWS Secret Access Key

AWS Region (e.g., eu-north-1)

2️⃣ Publish MQTT Messages to AWS IoT Core

python plc_mqtt.py

✅ Expected AWS IoT Test Client Output:

{
  "motor_speed": 1200,
  "temperature": 45,
  "status": "Running"
}

3️⃣ Upload PLC Data to AWS S3

python plc_s3.py

✅ Expected Output:

✅ Upload successful: https://s3.eu-north-1.amazonaws.com/your-bucket/plc_data.json

❓ Troubleshooting
