class Store:
    def __init__(self):
        self.kv_store = {}

    def set(self,key, value, cb):
        self.kv_store[key] = value
        cb()

    def get(self, key):
        return self.kv_store[key]
