# LeapYear.py Unittest
# By: Jason Graalum
import unittest
import LeapYear

class test_leapyear(unittest.TestCase):
    def test_correct1(self):
        self.assertEqual(LeapYear.leap_year(2012), True)
    def test_correct2(self):
        self.assertEqual(LeapYear.leap_year(40), True)
    def test_correct3(self):
        self.assertEqual(LeapYear.leap_year(16), True)
    
    def test_incorrect1(self):
        self.assertEqual(LeapYear.leap_year(50), False)
    def test_incorrect2(self):
        self.assertEqual(LeapYear.leap_year(2), False)
    def test_incorrect3(self):
        self.assertEqual(LeapYear.leap_year(2014), False)

if __name__ == '__main__':
    unittest.main()

