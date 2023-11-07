'''
Created on September 28, 2023
@author: Peter Murphy
@attention: this is only a template
'''
import unittest
from algorithm import across_bridge
class across_bridgeTest(unittest.TestCase):
    def test(self):
        #declare needed variables for testing
        #assert statements such as
        #self.assertEqual(<function call>,<expected output>)
        # or self.assertTrue(a==b)
        nums = [1, 2, 5, 8]
        a = across_bridge(nums)
        b = across_bridge([2, 2, 3, 6])
        c = across_bridge([1, 2, 6, 6])

        self.assertEqual(a,15)
        self.assertEqual(b,14)
        self.assertEqual(c,13)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
