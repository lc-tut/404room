from concurrent.futures import ThreadPoolExecutor
from sensors.sensor import Sensor
import time

class Door(Sensor):
    def __init__(self):
        self.sleep_time = 1
        self.pin_num = 4

        with open('/sys/class/gpio/export', 'w') as f:
            f.write(self.pin_num)

        with open('/sys/class/gpio/gpio%s/direction' % self.pin_num, 'w') as f:
            f.write("in")

    async def start(self):
        while True:
            try:
                pin_state = await self.__get_pin_state()
                if (pin_state == 0):
                    self.execute_plugins()
                    print("Door Open")
            except Exception as e:
                print(e)

            time.sleep(self.sleep_time)

    async def __get_pin_state(self):
        with open('/sys/class/gpio/gpio%s/value' % self.pin_num, 'r') as f:
            return int(f.read())
