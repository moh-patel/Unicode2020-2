from archives import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("0-19-852663-x"), 6)

if __name__ == '__main__':
    unittest.main()