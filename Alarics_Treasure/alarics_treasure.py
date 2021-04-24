
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

