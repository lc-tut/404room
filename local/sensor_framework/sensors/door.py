from concurrent.futures import ThreadPoolExecutor
from sensors.sensor import Sensor
import time
import socket

class Door(Sensor):
    def __init__(self, store):
        super().__init__(store)
        self.door_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    async def start(self):
        self.door_socket.bind('/tmp/door.sock')
        self.door_socket.listen(1)

        while True:
            conn, addr = self.door_socket.accept()
            try:
                while True:
                    data = conn.recv(1024)
                    self.store.set('Door',{'count', Data},self.execute_plugins)
            except:
                conn.close()
                os.remove(SOCK_FILENAME)
