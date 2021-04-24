from alarics_treasure import Solution
import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
            solution = Solution()
            self.assertEqual(solution.parse_roman_numerals("MCMLXI"), 1961)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("III"), 3)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("IV"), 4)

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("IX"), 9)

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("LVIII"), 58)

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("MCMXCIV"), 1994)

    def test7(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("LXXIII"), 73)

    def test8(self):
        solution = Solution()
        self.assertEqual(solution.parse_roman_numerals("MMXV"), 2015)



if __name__ == '__main__':
    unittest.main()