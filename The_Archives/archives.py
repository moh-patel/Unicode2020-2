import re
class Solution:

    def get_check_digit(self, input):
        check = re.match("[0-9]-[0-9]{2}-[0-9]{6}-[a-z]$", input)
        if check:
            i = 0
            # while(i<9):

            total = 0
            i = 1
            for pos in input:
                if pos.isdecimal():
                    total += i*int(pos)
                    i += 1
            return total % 11
        return False
