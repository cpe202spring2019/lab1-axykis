import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc = Location("San Diego", 32.7, -117.2)
        loc2 = Location("San Diego", 32.7, -117.2)
        self.assertEqual(eq(loc), eq(loc2))

if __name__ == "__main__":
        unittest.main()
