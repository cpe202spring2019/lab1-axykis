import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(TypeError):  # used to check for exception
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
        #this is a list where all values are equal
        tlist = [3,3,3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_negative(self):
        #this is a list containing negative numbers
        tlist = [-1,-2,-3]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_max_list_iter_mix_match_posneg(self):
        #this is testing mixing and matching postive and negatice values
        tlist = [-1,2,-3,4,-5]
        self.assertEqual(max_list_iter(tlist), 4)

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

    def test_max_list_iter_letters(self):
        "this checks if characters return a value"
        tlist = ['A','B','C']
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_strings(self):
        #this tests if strings return a value
        tlist = ["a","b","c"]
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter_float(self):
        #this tests what floats return
        tlist = [2.1, 2.4, 2.8]
        self.assertEqual(max_list_iter(tlist), 2.8)

    def test_max_list_iter_float_and_int(self):
        #mixs ints and floats
        tlist = [1,2.5,5,3.5,5.3]
        self.assertEqual(max_list_iter(tlist), 5.3)

    def test_max_list_iter_type_combo(self):
        #this includes both char and ints
        tlist = ['A',32,"3", 2.1]
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)



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

    def test_reverse_rec_floats(self):
        self.assertEqual(reverse_rec([2.1,2.2,2.3]), [2.3,2.2,2.1])

    def test_reverse_rec_chars(self):
        self.assertEqual(reverse_rec([A,b,c]), [c,b,A])

    def test_reverse_rec_strings(self):

        self.assertEqual(reverse_rec(["ABC","123"]), None)

    def test_reverse_rec_multiple_types(self):
        self.assertEqual(reverse_rec(["a",b,3]),[3,b,"a"])





    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_no_target_in_set(self):
        list_val = [1,1,1,1,1,1]
        low = 0
        high = len(list_val)-1
        with self.assertRaises(IndexError):  # used to check for exception
            bin_search(4,0,len(list_val)-1, list_val)


    def test_bin_search_target_at_end(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )

    def test_bin_search_negative_target(self):
        list_val =[-4,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-4, 0, len(list_val)-1, list_val), 0 )

    def test_bin_search_characters(self):
        list_val =[0,1,2,3,'A',7,8,9,10]
        low = 0
        high = len(list_val)-1
        with self.assertRaises(TypeError):  # used to check for exception
            bin_search('A', 0, len(list_val)-1, list_val)

    def test_bin_search_list_of_only_target(self):
        list_val =[1,1,1,1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 2 )


if __name__ == "__main__":
        unittest.main()

    

