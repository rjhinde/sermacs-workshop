"""
string_util.py
Miscellaneous string processing functions
"""


def title_case(sentence):
    """
    Capitalize the first letter of every word in a sentence.

    Parameters
    ----------
    sentence: string
    	Sentence to be converted to title case

    Returns
    -------
    result: string
    	Input string converted to title case
    
    Example
    -------
    >>> title_case('This iS a sampLe.')
    	This Is A Sample.
    """
    
    # error checking
    
    if not isinstance(sentence, str):
    	raise TypeError('Input to title_case must be string')
    
    # convert entire sentence to lower case then split it into words
    
    words = (sentence.lower()).split()
    
    # capitalize each word
    
    for i in range(len(words)):
    	words[i] = words[i].capitalize()
    
    # put the words back together into a sentence, separating them with spaces
    
    result = ' '.join(words)
    
    return result
    