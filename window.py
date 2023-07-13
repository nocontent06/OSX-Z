import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class CPUInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPU Information")
        self.setGeometry(100, 100, 300, 100)
        self.initUI()

    def initUI(self):
        self.cpu_label = QLabel(self)
        self.cpu_label.setGeometry(10, 10, 280, 80)
        self.cpu_label.setText(self.get_cpu_info())
        self.cpu_label.setStyleSheet("font-size: 14px;")

    def get_cpu_info(self):
        # Get CPU information using Terminal commands
        cmd_brand = "sysctl -n machdep.cpu.brand_string"
        cmd_physical_cores = "sysctl -n machdep.cpu.core_count"
        cmd_total_cores = "sysctl -n machdep.cpu.thread_count"
        cmd_max_freq = "sysctl -n hw.cpufrequency_max"
        cmd_cur_freq = "sysctl -n hw.cpufrequency"

        brand = subprocess.check_output(cmd_brand, shell=True).decode("utf-8").strip()
        physical_cores = subprocess.check_output(cmd_physical_cores, shell=True).decode("utf-8").strip()
        total_cores = subprocess.check_output(cmd_total_cores, shell=True).decode("utf-8").strip()
        max_freq = subprocess.check_output(cmd_max_freq, shell=True).decode("utf-8").strip()
        cur_freq = subprocess.check_output(cmd_cur_freq, shell=True).decode("utf-8").strip()

        # Format the output
        if brand.startswith("Intel"):
            brand = brand.replace("(R)", "")
            brand = brand.replace("(TM)", "")
            brand = brand.replace("CPU", "")
            brand = brand.split("@")[0].strip()

        cpu_info = "CPU: {}\n".format(brand)
        cpu_info += "Physical Cores: {}\n".format(physical_cores)
        cpu_info += "Total Cores: {}\n".format(total_cores)
        cpu_info += "Max Frequency: {} MHz\n".format(max_freq)
        cpu_info += "Current Frequency: {} MHz".format(cur_freq)
        return cpu_info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CPUInfoApp()
    window.show()
    sys.exit(app.exec_())

