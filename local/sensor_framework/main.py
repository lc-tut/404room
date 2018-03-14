from concurrent.futures import ThreadPoolExecutor
import asyncio
import json

from utils.store import Store

if __name__ == "__main__":
    store = Store()

    with open('sensor.json', 'r') as f:
        settings = json.loads(f.read())

    loop = asyncio.get_event_loop()

    for sensor, value in settings['sensors'].items():
        sensors = value['name'].split('/')
        try:
            # importしてイベントループに追加
            exec('from ' + sensors[0] + ' import ' + sensors[1])
            exec(sensor + '=' + sensors[1]+'(store)')
            exec('asyncio.ensure_future(' + sensor + '.start())')

            for plugin in value['plugins']:
                p = plugin.split('/')
                exec('from ' + p[0] + ' import ' + p[1])
                exec(sensor + '.add_plugins([' + p[1] +'])')
        except Exception as e:
            print(e)

    loop.run_forever()
