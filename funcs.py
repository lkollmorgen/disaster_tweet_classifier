import numpy as np

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
        col = texts.str.contains(words[x]).astype('int').values
        indicator_array[:,x] = col
    return indicator_array

