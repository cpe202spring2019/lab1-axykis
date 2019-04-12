import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "SLO, 35.3, -120.7")

    def test_repr_unequal(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(repr(loc), "NOTSLO, 35.3, -120.7")

    def test_repr_two_equal_objects(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), repr(loc2))

    def test_repr_two_different_objects(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("San Diego", 32.7, -117.2)
        self.assertNotEqual(repr(loc), repr(loc2))

    def test_repr_setting_two_objects_equal(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = loc
        self.assertEqual(repr(loc), repr(loc2))

    
    def test_eq(self):
        loc = Location("San Diego", 32.7, -117.2)
        loc2 = Location("San Diego", 32.7, -117.2)
        self.assertEqual(loc,loc2)

    def test_eq_set_obj_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2=loc1
        self.assertEqual(loc1,loc2)

    def test_eq_set_3obj_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = loc1
        loc3 = loc2
        self.assertEqual(loc1,loc2,loc3)


if __name__ == "__main__":
        unittest.main()
