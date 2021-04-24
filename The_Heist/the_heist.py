import numpy as np


class Solution:

    def calculate_capacity(self, input):
        length = len(input)
        two_D = np.zeros((255, length))

        # creates the 2D object
        pos = 0
        for i in input:
            for x in range(i):
                two_D[x, pos] = 1
            pos += 1

        # calculate the volume
        total = 0
        for x in two_D:
            match_index = 0
            stack = 0
            for i in x:
                if i == 1:
                    if match_index > 1:
                        total += stack
                        stack = 0
                    else:
                        match_index = 1
                elif i == 0:
                    if match_index != 0:
                        stack += 1
                        match_index += 1
            match_index = 0
        return total


# # output 11
# print('output 11=', calculate_capacity([1, 4, 2, 1, 1, 2, 5, 3, 4]))

# # output 16
# print('output 16=', calculate_capacity([5, 4, 2, 1, 1, 2, 5, 3, 4]))
# # output 14
# print('output 14=', calculate_capacity([1, 6, 2, 1, 1, 2, 5, 5, 3]))
# # output 3
# print('output 3=', calculate_capacity([15, 2, 5, 2]))

# # output 0
# print('output 0=', calculate_capacity([2, 2]))

# arr = [1]

# length = len(arr)

# X = np.zeros((5, length))
# print(X)

# pos = 0
# for i in arr:
#     for x in range(i):
#         X[x, pos] = 1
#     pos += 1

# print(X)

# total = 0
# for x in X:
#     match_index = 0
#     stack = 0
#     for i in x:
#         if i == 1:
#             if match_index == 0:
#                 match_index += 1
#             elif match_index == 1:
#                 match_index = 1
#             elif match_index > 1:
#                 total += stack
#                 stack = 0
#         elif i == 0:
#             if match_index != 0:
#                 stack += 1
#                 match_index += 1
#     match_index = 0
# print(total)
