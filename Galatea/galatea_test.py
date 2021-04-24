from galatea import Solution
import unittest
class SolutionTests(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(2147483647), True)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(4), False)
        
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(5), True)
        
    def test4(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(6), False)
        
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(7), True)
        
    def test6(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(8), False)
        
    def test7(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(9), False)
        
    def test8(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(10), False)
        
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(121), False)
        
    def test10(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(122), False)
        
    def test11(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(7919), True)
        
    def test12(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(-10), False)
        
    def test13(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(0), False)
        
    def test14(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(1), False)
        
    def test15(self):
        solution = Solution()
        self.assertEqual(solution.is_prime(2), True)

if __name__ == '__main__':
    unittest.main()