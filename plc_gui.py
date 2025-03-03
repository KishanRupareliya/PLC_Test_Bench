# GUI for PLC Test Bench
import tkinter as tk
from tkinter import ttk
from plc_test_bench import MotorTestBench

class MotorTestBenchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PLC Test Bench GUI")
        self.test_bench = MotorTestBench()

        self.labels = {}
        parameters = ["motor_running", "motor_speed", "temperature", "system_status"]
        for param in parameters:
            ttk.Label(root, text=param.replace("_", " ").title()).pack()
            self.labels[param] = ttk.Label(root, text="0")
            self.labels[param].pack()

        ttk.Button(root, text="Start Motor", command=self.start_motor).pack()
        ttk.Button(root, text="Stop Motor", command=self.stop_motor).pack()
        ttk.Button(root, text="Monitor Temperature", command=self.monitor_temperature).pack()

    def start_motor(self):
        self.test_bench.start_motor()
        self.update_display()

    def stop_motor(self):
        self.test_bench.stop_motor()
        self.update_display()

    def monitor_temperature(self):
        self.test_bench.monitor_temperature()
        self.update_display()

    def update_display(self):
        data = self.test_bench.log_data()
        for key, value in data.items():
            self.labels[key].config(text=str(value))

if __name__ == "__main__":
    root = tk.Tk()
    app = MotorTestBenchGUI(root)
    root.mainloop()
