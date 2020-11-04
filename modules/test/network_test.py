import unittest
from common.network_tools import ThNetWordTestCase

class MyTestCase(unittest.TestCase):
    def test_ping1(self):
        self.assertEqual(ThNetWordTestCase.ping("192.168.0.255",2,4)[0], False)
    def test_ping2(self):
        self.assertEqual(ThNetWordTestCase.ping("192.168.0.1", 2, 4)[0], True)


if __name__ == '__main__':
    unittest.main()
