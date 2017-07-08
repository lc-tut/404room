from sensors.door import Door
from concurrent.futures import ThreadPoolExecutor
import asyncio

from plugins.examplePlugin import example_plugin


plugins = [example_plugin]

door = Door()
door.add_plugins(plugins)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    asyncio.ensure_future(door.start())

    loop.run_forever()
