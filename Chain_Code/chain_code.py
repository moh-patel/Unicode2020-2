
#string of letters and punctuation and spaces
# reorganise each letter in the word alphabetically
# capital letters remain
# position of upper case
import string
class Solution:

    def chain(self, input):
        new_words = []

        words = input.split(' ')

        for word in words:
            upper = []
            # store position of punc as number:punc
            punc = {}
            new_word = ""    
            # going through word
            for i, char in enumerate(word):
                if char.isupper():
                    upper.append(i)
                    new_word = self.add_letter(new_word, char.lower(), i)
                elif char in string.punctuation:
                    punc[i] = char
                else:
                    new_word = self.add_letter(new_word, char, i)
            
            new_word = self.add_punc(new_word, punc)
            new_word = self.add_upper_case(new_word, upper)

            new_words.append(new_word)
        return ' '.join(new_words)
    def add_upper_case(self, word, upper):
        for i in upper:
            word = word[:i] + word[i:i+1].upper() + word[i+1:]
        return word
    
    def add_punc(self, word, punc):
        for i, char in punc.items():
            word = word[:i] + char + word[i:]
        return word

    def add_letter(self, word,char, i):
        if char.isalpha() and i==0:
            return char + word
        elif i == 0:
            word= char + word
            return word 
        elif char.isalpha():
            if word[i-1:i].isalpha() and string.ascii_lowercase.index(char) >= string.ascii_lowercase.index(word[i-1:i]):
                word = word[:i] + char + word[i:]
                return word
            else:
                return self.add_letter(word, char, i-1)
        else:
            return self.add_letter(word, char, i-1)

# print(Solution().chain("!Hello, How aRe  YoU!!dsfds"))

        # for i,char in enumerate(input):
        #     print(i, char)
        #     # word+=i
        #     # if i in string.punctuation:
        #     #     print("space or puntuation")
        #     #     print(word)
        #     # if i.isspace():
        #     #     print("space")
        #     #     word = ""


        # print(word)

