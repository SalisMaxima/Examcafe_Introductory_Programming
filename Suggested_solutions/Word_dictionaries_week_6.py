"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
    Now your task is to implement a function word_histogram which takes a list of str containing sentences of a text as input. The function should create a histogram of words found within the provided text. Here are the specific requirements:

    Punctuation (., ,), spaces, and capitalization should be disregarded. Everything should be converted to lowercase.

    The function should return a dictionary where each key represents a unique word, and the corresponding value is the number of occurrences of that word within the text.

    The format of the returned dictionary should look like this: {'write': 2, 'the': 12, 'function': 7, ...}.

    Parameters:
        lines (list) – The lines that are analyzed for word count.

    Return type:
        dict

    Returns:
        The histogram of word occurrences.
"""

#Import the necessary libraries
import os  
import re

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")


def word_histogram(lines):
    #First we convert the lines to lower case
    lines = [line.lower() for line in lines]
    #Then we split the string into a list of words using regular expression
    words = re.findall(r'\b\w+\b', ' '.join(lines))
    #Then we create a dictionary with the words as keys and the number of times they appear as values
    histogram = {}
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

print(word_histogram(['This is the first sentence', 'This is the second sentence']))
print(word_histogram(['... to be or not to be ? ...']))
