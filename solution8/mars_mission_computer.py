import random
import time
import json
import threading
import sys
import platform
import os
import shutil
import psutil

class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    def get_env(self):
        return self.env_values.copy()


class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }
        self.ds = DummySensor()
        self.load_settings()

    def load_settings(self):
        self.info_settings = []
        self.load_settings = []
        try:
            with open("setting.txt", "r") as f:
                for line in f:
                    if line.startswith("system_info="):
                        self.info_settings = line.strip().split("=")[1].split(",")
                    elif line.startswith("system_load="):
                        self.load_settings = line.strip().split("=")[1].split(",")
        except FileNotFoundError:
            self.info_settings = ["os", "os_version", "cpu", "cpu_cores", "memory"]
            self.load_settings = ["cpu_usage", "memory_usage"]

    def get_mission_computer_info(self):
        try:
            info = {}
            if "os" in self.info_settings:
                info["os"] = platform.system()
            if "os_version" in self.info_settings:
                info["os_version"] = platform.version()
            if "cpu" in self.info_settings:
                info["cpu"] = platform.processor()
            if "cpu_cores" in self.info_settings:
                info["cpu_cores"] = os.cpu_count()
            if "memory" in self.info_settings:
                mem = shutil.disk_usage("/")  # fallback for demonstration
                info["memory"] = f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
            print("[시스템 정보]")
            print(json.dumps(info, indent=4))
        except Exception as e:
            print(f"시스템 정보 확인 중 오류 발생: {e}")

    def get_mission_computer_load(self):
        try:
            load = {}
            if "cpu_usage" in self.load_settings:
                load["cpu_usage"] = f"{psutil.cpu_percent(interval=1)} %"
            if "memory_usage" in self.load_settings:
                mem = psutil.virtual_memory()
                load["memory_usage"] = f"{mem.percent} %"
            print("[시스템 부하]")
            print(json.dumps(load, indent=4))
        except Exception as e:
            print(f"시스템 부하 확인 중 오류 발생: {e}")

if __name__ == "__main__":
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()