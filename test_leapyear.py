import unittest
import leapyear

class TestCase(unittest.TestCase):
    #test to check if numbers divisible by 400 return leapyear
    def test_fourhundred(self):
        hundreds = [0, 400, 800, 1200, 1600, 2000, 2400]
        for x in hundreds:
            self.assertEqual(leapyear.checkLeap(x), "leapyear")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)