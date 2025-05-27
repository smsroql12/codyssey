import threading
import multiprocessing
import time
import random
import sys

class MissionComputer:
    def get_mission_computer_info(self):
        while True:
            print('[INFO]', 'CPU: 3.2GHz, RAM: 16GB, OS: MarsOS 1.0')
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            cpu_load = random.randint(1, 100)
            memory_usage = random.randint(1, 100)
            print('[LOAD]', f'CPU Load: {cpu_load}%, Memory Usage: {memory_usage}%')
            time.sleep(20)

    def get_sensor_data(self):
        while True:
            temperature = random.uniform(-80.0, 20.0)
            radiation = random.uniform(0.1, 5.0)
            print('[SENSOR]', f'Temperature: {temperature:.2f}C, Radiation: {radiation:.2f}mSv')
            time.sleep(5)


def run_with_threads(computer):
    t1 = threading.Thread(target=computer.get_mission_computer_info)
    t2 = threading.Thread(target=computer.get_mission_computer_load)
    t3 = threading.Thread(target=computer.get_sensor_data)

    t1.start()
    t2.start()
    t3.start()

    try:
        while True:
            if sys.stdin.read(1) == 'q':
                print('Stopping threads...')
                break
    except KeyboardInterrupt:
        print('Interrupted by user')


def run_with_processes():
    run_computer1 = MissionComputer()
    run_computer2 = MissionComputer()
    run_computer3 = MissionComputer()

    p1 = multiprocessing.Process(target=run_computer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=run_computer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=run_computer3.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    try:
        while True:
            if sys.stdin.read(1) == 'q':
                print('Stopping processes...')
                p1.terminate()
                p2.terminate()
                p3.terminate()
                break
    except KeyboardInterrupt:
        print('Interrupted by user')
        p1.terminate()
        p2.terminate()
        p3.terminate()


if __name__ == '__main__':
    print('Press "q" to stop')
    mode = input('Enter mode (thread/process): ').strip().lower()

    if mode == 'thread':
        run_computer = MissionComputer()
        run_with_threads(run_computer)
    elif mode == 'process':
        run_with_processes()
    else:
        print('Invalid mode')