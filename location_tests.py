import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "SLO, 35.3, -120.7")

    def test_repr_unequal(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "SLO, 35.3, -120.7")


    # Add more tests!
    def test_eq(self):
        loc = Location("San Diego", 32.7, -117.2)
        loc2 = Location("San Diego", 32.7, -117.2)
        self.assertEqual(loc,loc2)

    def test_eq_set_obj_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2=loc1
        #self.assertEqual()
assert true
assert false
notequal
if __name__ == "__main__":
        unittest.main()
