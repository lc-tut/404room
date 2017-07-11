from abc import ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor

class Sensor(metaclass=ABCMeta):
    plugins = []
    thread_pool_executor = ThreadPoolExecutor(max_workers=124)

    @abstractmethod
    async def start(self):
        pass

    def __init__(self, store):
        self.store = store

    def add_plugins(self, func_ary):
        for func in func_ary:
            self.plugins.append(func)

    def execute_plugins(self):
        for plugin in self.plugins:
            self.__submit(plugin(self.store))

    def __submit(self, func):
        self.thread_pool_executor.submit(func)
