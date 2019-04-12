import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), 'SLO', "35.3", "-120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc = Location("San Diego", 32.7, -117.2)
        loc2 = Location("San Diego", 32.7, -117.2)
        self.assertEqual(__eq__(loc,loc2), loc.name = loc2.name and loc.lat = loc2.lat and loc.lon = loc2.lon)

    def test_eq_set_obj_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2=loc1
        self.assertEqual()

if __name__ == "__main__":
        unittest.main()
