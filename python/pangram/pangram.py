# my own solution
###---------------------------------------------
import re

def is_pangram(str):
    letter = re.findall(r'[a-z]', str.lower())
    letter_num = len(set(letter))
    if letter_num == 26:
        return True
    return False
###----------------------------------------------

# other people's solution that I like
###----------------------------------------------
# import string
#
# def is_pangram(s):
#     # all 26 char
#     alpha = string.ascii_lowercase
#
#     # each char in the string, if the char match the alpha, replace it with ""
#     for char in s.lower():
#         alpha = alpha.replace(char, '')
#     # if the len of aphpa return 0, meaning the string using all 26 letter
#     return len(alpha) == 0
#
# alpha = string.ascii_lowercase
# print(alpha)
###------------------------------------------------

###------------------------------------------------
# def is_pangram(phrase):
#     phrase = filter(str.isalpha, phrase.lower())
#
#     return len(set(phrase)) == 26
###-------------------------------------------------
