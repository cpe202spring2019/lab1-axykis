import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_simple(self):
        #Just a regular list
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_empty(self):
        #this is the case where it is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter_all_val_same(self):
        tlist = [3,3,3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_negative(self):
        tlist = [-1,-2,-3]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_max_list_iter_all_zero(self):
        tlist = [0,0,0,0]
        self.assertEqual(max_list_iter(tlist), 0)

    def test_max_list_iter_max_in_pos1(self):
        tlist = [3,2,1]
        self.assertEqual(max_list_iter(tlist), 3)
    def test_max_list_iter_max_pos_mid(self):
        tlist = [1,2,3,2,1]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_max_at_end(self):
        tlist = [1,3,4,5,6]
        self.assertEqual(max_list_iter(tlist), 6)



    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_repeated_values(self):
        self.assertEqual(reverse_rec([1,2,2,2,4]), [4,2,2,2,1])

    def test_reverse_rec_empty_case(self):
        self.assertEqual(reverse_rec([]), None)

    def test_reverse_rec_pallendrome(self):
        self.assertEqual(reverse_rec[1,2,2,1], [1,2,2,1])

    def test_reverse_rec_negative_values(self):
        self.assertEqual(reverse_rec[-1,-2,-3],[-3,-2,-1])

    def test_reverse_rec_single_num(self):
        self.assertEqual(reverse_rec([2]),[2])



    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
