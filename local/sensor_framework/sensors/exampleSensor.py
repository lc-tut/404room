from concurrent.futures import ThreadPoolExecutor
from sensors.sensor import Sensor
import time

class Example(Sensor):
    def __init__(self):
        print("sensor initialize")
        self.sleep_time = 1

    async def start(self):
        # 5秒に一回発火する
        i = 0
        while True:
            if (i % 5 == 0):
                self.execute_plugins()

            time.sleep(self.sleep_time)
            i += 1
