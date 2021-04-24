import string
import collections

class Solution:

    def cipher(self, input, key):
        alphabet = list(string.ascii_lowercase)
        length = len(alphabet)
        output = ""
        for i in input:
            if i in alphabet:
                pos = (alphabet.index(i) + key) % length
                output += alphabet[pos]
            elif i.lower() in alphabet:
                i = i.lower()
                pos = (alphabet.index(i) + key) % length
                output += alphabet[pos].upper()
                print(pos)
            else:
                output += i
        return output
