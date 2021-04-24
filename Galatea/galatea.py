import math

class Solution:

    def is_prime(self, input):
        if input == 0 or input ==1:
            return False
        # Your code goes here
        x = abs(input)
        max = int(math.sqrt(x))
        for i in range(2, max+1):
            if (x%i)==0:
                return False
        return True



# first attempt without sqrt
# x = 214
# y = x // 2
# prime = True

# for i in range(2,y):
#     # print(f'testing {x % i}')
#     if (x % i) != 0:
#         not_prime = False

# print(prime) 

# https://www.youtube.com/watch?v=aG7J3m3vlNA