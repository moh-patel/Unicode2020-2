
import string
import collections

class Solution:

    def parse_roman_numerals(self, input):
    
        roman_dict = {'M': 1000, 'D': 500, 'C': 100,
                    'L': 50, 'X': 10, 'V': 5, 'I': 1}

        length = len(input)
        i = 0
        sum = 0
        while(i < length):
            first = roman_dict[input[i]]
            second = roman_dict[input[i+1]] if i <= length-2 else 0
            if first >= second:
                sum += first
                i += 1
            else:
                sum += (second-first)
                i += 2

        return(sum)


# parse_roman_numerals("MCMLXI")


# def test1(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("MCMLXI"), 1961)

#     def test2(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("III"), 3)

#     def test3(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("IV"), 4)

#     def test4(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("IX"), 9)

#     def test5(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("LVIII"), 58)

#     def test6(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("MCMXCIV"), 1994)

#     def test7(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("LXXIII"), 73)

#     def test8(self):
#         solution = Solution()
#         self.assertEqual(solution.parse_roman_numerals("MMXV"), 2015)
