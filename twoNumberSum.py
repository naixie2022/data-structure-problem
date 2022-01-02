"""
  This is a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum.

  If there are two numbers in the input array sum up to the target sum. Return an array with these two number.
  Otherwise return an empty array. 
"""
import unittest

def twoNumberSum(array, targetSum):

  # Python uses Timsort on array, the runtime complexity is O(n logn)
  array.sort()
  
  left = 0
  right = len (array) - 1

  # complexity O(n)/2 for the loop
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left = left + 1
    elif currentSum > targetSum:
      right = left - 1
  return []


# -------------- Test--------------------------
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([4, 5, -4, 9, 11, 1, -1, 7], 20)
        self.assertTrue(len(output) == 2)
        self.assertTrue(9 in output)
        self.assertTrue(11 in output)


##if __name__ == '__main__':

unittest.main()