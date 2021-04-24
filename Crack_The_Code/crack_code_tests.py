from crack_code import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Zwddg ogjdv!", 8), "Hello world!")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Yvccf nficu!", 9), "Hello world!")

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Kyv t*uv zj 1: gcvrjv ivjgfeu!", 9), "The c*de is 1: please respond!")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Qnuux fxaum!", -9), "Hello world!")

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Ifmmp xpsme!", 25), "Hello world!")

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Hello world!", 0), "Hello world!")

    def test7(self):
        solution = Solution()
        self.assertEqual(solution.cipher("Gdkkn vnqkc!", -25), "Hello world!")

    def test8(self):
        solution = Solution()
        self.assertEqual(solution.cipher("123 ! *()", 1), "123 ! *()")

if __name__ == '__main__':
    unittest.main()