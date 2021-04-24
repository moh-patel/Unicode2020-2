from the_heist import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([ 1, 4, 2, 1, 1, 2, 5, 3, 4 ]), 11)
    
    def test2(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([ 1,4,2,1,1,2,5,5,3]), 10)
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([ 5,4,2,1,1,2,5,3,4]), 16) 

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([ 1,6,2,1,1,2,5,5,3]), 14) 

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([ 15,2,5,2]), 3) 

if __name__ == '__main__':
    unittest.main()
