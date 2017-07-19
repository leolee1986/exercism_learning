# my own solution
###-------------------------------
import re

def is_isogram(word):
    # use regex to replace all special characters and space
    clean_word = re.sub('\W+','',word).lower()
    char = list(clean_word)
    if(len(char) == len(set(char))):
        return True
    else:
        return False
###-----------------------------------------
