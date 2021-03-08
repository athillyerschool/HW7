import unittest
import leapyear

class TestCase(unittest.TestCase):
    #test to check if numbers divisible by 400 return "leapyear"
    def test_fourhundred(self):
        hundreds = [0, 400, 800, 1200, 1600, 2000, 2400]
        for x in hundreds:
            self.assertEqual(leapyear.checkLeap(x), "leapyear")
    
    #test to check that div/100 but not 400 returns "not leapyear"
    def test_hundreds(self):
        oneHundreds = [100, 200, 300, 500, 600, 700, 900, 1100, 1300, 1400, 1500, 1700]
        for x in oneHundreds:
            self.assertEqual(leapyear.checkLeap(x), "not leapyear")
if __name__ == '__main__':
    unittest.main(verbosity=2)