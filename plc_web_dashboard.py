# Flask-based Web Dashboard for Remote Monitoring
'''
from flask import Flask, jsonify
from plc_test_bench import MotorTestBench

app = Flask(__name__)

test_bench = MotorTestBench()

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(test_bench.log_data())

@app.route('/start', methods=['POST'])
def start_motor():
    test_bench.start_motor()
    return jsonify({"message": "Motor started"})

@app.route('/stop', methods=['POST'])
def stop_motor():
    test_bench.stop_motor()
    return jsonify({"message": "Motor stopped"})

@app.route('/')
def home():
    return "Welcome to the PLC Web Dashboard!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
'''

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Simulated real-time PLC data
def get_plc_data():
    return {
        "motor_running": random.choice([True, False]),
        "motor_speed": random.randint(0, 2000),
        "temperature": random.randint(20, 100),
        "vibration_level": round(random.uniform(0.0, 5.0), 2),
        "energy_consumption": round(random.uniform(0.0, 50.0), 2),
        "torque": round(random.uniform(0.0, 10.0), 2),
        "system_status": random.choice(["Running", "Idle", "Stopped"]),
    }

# Web dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# API to fetch real-time PLC data
@app.route('/api/data')
def api_data():
    return jsonify(get_plc_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
