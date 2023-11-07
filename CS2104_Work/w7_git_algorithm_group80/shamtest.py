'''
Created on sept 28, 2023
@author: Shamit Pradhan
'''
import unittest
from algorithm import across_bridge
class sameNumber(unittest.TestCase):
    def test(self):
        #declare needed variables for testing
        #assert statements such as
        #self.assertEqual(<function call>,<expected output>)
        # or self.assertTrue(a==b)
        arr = [5, 5, 5]
        j = across_bridge(arr)
        a = [1, 1, 1]
        t = across_bridge(a)
        b = [321, 321, 321, 321, 321, 321]
        t1 = across_bridge(b)
        d = [0, 0, 0]
        t2 = across_bridge(d)
        self.assertEqual(j, 15)
        self.assertEqual(t, 3)
        self.assertEqual(t1, 963)
        self.assertEqual(t2, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()