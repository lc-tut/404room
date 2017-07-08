import unittest

import sys
sys.path.append('../')

from sensors.door import Door

class TestDoor(unittest.TestCase):
    def test_add_plugins(self):
        def test():
            return 1

        door = Door()
        door.add_plugins(test)
        self.assertEqual(len(door.plugins), 1)

if __name__ == '__main__':
    unittest.main()
