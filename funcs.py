import numpy as np
import pandas as pd
import math #to check for nan
import re #get rid of high ascii characters


#identify presence of inputted words in
def words_in_texts(words, texts):
    """
    Params:
        words (list): Words to find.
        texts (Series): Strings to search in.
    
    Returns:
        A 2D NumPy array of 0s and 1s with shape (n, d) where 
        n is the number of texts, and d is the number of words.
    """
    indicator_array = np.zeros((len(texts),len(words)))
    for x in range(len(words)):
        col = texts.str.lower().str.contains(words[x]).astype('int').values
        indicator_array[:,x] = col
    return indicator_array

def capitals_vs_sentence_len(text):
    """
    Params:
        string (list): tweet to analyze

    Returns:
        float : The ratio of capital letters to the total number of characters in the string
    """
    uppercases = [letter for letter in text if letter.isupper() and letter.isascii()]
    ratio = float(len(uppercases)/len(text))
    if len(text) == 0:
        return 0.0
    return ratio

def count_periods(text):
    """
    Params:
        text (list): tweet to analyze

    Returns
        int : the number of periods in the text
    """
    return int(len([x for x in text if x == '.']))

def count_digits(text):
    """
    Params:
        text (list): tweet to analyze

    Returns:
        int : the number of digits in the text
    """
    return int(len([x for x in text if x.isdigit()]))


      