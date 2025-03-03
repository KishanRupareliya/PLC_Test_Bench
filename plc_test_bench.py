# Core PLC Test Bench Logic
import time
import random

class MotorTestBench:
    def __init__(self):
        self.motor_running = False
        self.motor_speed = 0  # Speed in RPM
        self.temperature = 25  # Default temperature in Celsius
        self.overheat_threshold = 80  # Max temp before shutdown
        self.vibration_level = 0.0  # Simulated vibration
        self.energy_consumption = 0.0  # Energy tracking
        self.torque = 0.0  # Torque measurement
        self.system_status = "Idle"  # System state tracking

    def start_motor(self):
        if not self.motor_running:
            self.motor_running = True
            self.motor_speed = 1000  # Default start speed
            self.system_status = "Running"
            print("Motor Started")
        else:
            print("Motor is already running")

    def stop_motor(self):
        if self.motor_running:
            self.motor_running = False
            self.motor_speed = 0
            self.system_status = "Stopped"
            print("Motor Stopped")

    def set_speed(self, speed):
        if self.motor_running:
            self.motor_speed = speed
            print(f"Motor speed set to {speed} RPM")

    def monitor_temperature(self):
        self.temperature = random.randint(20, 100)
        print(f"Temperature: {self.temperature}°C")
        if self.temperature > self.overheat_threshold:
            print("Overheat detected! Shutting down motor.")
            self.stop_motor()

    def log_data(self):
        return {
            "motor_running": self.motor_running,
            "motor_speed": self.motor_speed,
            "temperature": self.temperature,
            "vibration_level": self.vibration_level,
            "energy_consumption": self.energy_consumption,
            "torque": self.torque,
            "system_status": self.system_status
        }

if __name__ == "__main__":
    test_bench = MotorTestBench()
    test_bench.start_motor()
    test_bench.set_speed(1500)
    test_bench.monitor_temperature()
    print("Data Log:", test_bench.log_data())
