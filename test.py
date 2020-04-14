from mySolution import power,powerH,C
import unittest

class TestLab4(unittest.TestCase):
    def testPower(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(2, 5), 32)
    
    def testPowerH(self):
        self.assertEqual(powerH(0, 0), 1)
        self.assertEqual(powerH(1, 0), 1)
        self.assertEqual(powerH(2, 2), 4)

    def testC(self):
        self.assertEqual(C(0, 0), 1)
        self.assertEqual(C(1, 0), 1)
        self.assertEqual(C(4, 2), 6)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'],exit = False)