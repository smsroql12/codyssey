import random
import time
import json
import threading
import sys
from datetime import datetime

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
        log_line = (
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, "
            f"{self.env_values['mars_base_internal_temperature']:.2f}, "
            f"{self.env_values['mars_base_external_temperature']:.2f}, "
            f"{self.env_values['mars_base_internal_humidity']:.2f}, "
            f"{self.env_values['mars_base_external_illuminance']:.2f}, "
            f"{self.env_values['mars_base_internal_co2']:.4f}, "
            f"{self.env_values['mars_base_internal_oxygen']:.2f}\n"
        )
        with open("env_log.txt", "a") as log_file:
            log_file.write(log_line)

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
        self.running = True
        self.history = []

    def listen_for_stop(self):
        input("종료하려면 Enter 키를 누르세요.\n")
        self.running = False
        print("시스템 종료")

    def compute_average(self):
        if not self.history:
            return
        print("[5분 평균 출력]")
        avg = {}
        count = len(self.history)
        for key in self.env_values:
            total = sum(entry[key] for entry in self.history)
            avg[key] = total / count
        print(json.dumps(avg, indent=4))

    def get_sensor_data(self):
        stop_thread = threading.Thread(target=self.listen_for_stop)
        stop_thread.daemon = True
        stop_thread.start()

        minute_counter = 0
        self.history.clear()

        while self.running:
            self.ds.set_env()
            current = self.ds.get_env()
            self.env_values = current.copy()
            self.history.append(current)

            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 환경 정보:")
            print(json.dumps(self.env_values, indent=4))

            minute_counter += 1
            if minute_counter >= 60:  # 5분마다 평균 출력 (60 * 5초 = 300초)
                self.compute_average()
                minute_counter = 0
                self.history.clear()

            time.sleep(5)


# 인스턴스 생성 및 실행
if __name__ == "__main__":
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()
