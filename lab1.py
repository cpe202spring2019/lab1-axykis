
def max_list_iter(int_list):
   if len(int_list)==0:
       return "None"
   max = int(int_list[0])
   for i in range ( len(int_list)):
      if int_list[i]  > max:
         max = int_list [i]
   return max;

   # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   pass

def reverse_rec(int_list):
   print(int_list)
   #this is the base case for recursive function
   if len(int_list) == 1:
      return int_list
   #if the list is greater than just one index
   x=reverse_rec(int_list[1:])
   print(x)
   x.append(int_list[0]);
   return x

   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""



def bin_search(target, low, high, int_list):
   midpoint = (int)(1+((low + high)/2))
   if (len(int_list) == 1 and target == int_list[0]):
      return 0

   if high > 1 :

      if target == int_list[midpoint]:
         return midpoint

      elif int_list[midpoint] > target:
         return bin_search(target, low, midpoint-1, int_list)

      else:
         return bin_search(target, midpoint+1, high, int_list)
   else:
      return "None"

   # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
