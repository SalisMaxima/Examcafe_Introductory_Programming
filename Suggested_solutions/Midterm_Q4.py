"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
    In various languages, some combinations of letters are more common than others. For example, in the English language,
    the letter q is almost always followed by the letter u.
    
    In this task, you should write a function that takes as input two strings: text, a string representing some text; and
    letter, a string containing one lower case letter from the English alphabet. 
    
    The function should return the letter that
    most frequently follows the given letter in the text. If the given letter is not found in the text or is not followed by any
    other letter, the function should return an empty string.
    
    The following rules apply:
    • The input text may contain both upper and lower case letters, but you should treat them all as lower case letters.
    For example, A and a should be treated as a.
    • All characters that are not letters of the English alphabet should be ignored. However, they should be treated as
    breaks in the flow of succession. For example, in up-down, the letter p is not followed by the letter d.
    • In general, two or more letters may be the most frequent successors. In our tests, there is always exactly one most
    frequent successor. Therefore, you can assume that if the letter is found in the text and has successors, there is
    exactly one which is the most frequent.
    
    Input:  two strings: text, a string representing some text; and
    letter, a string containing one lower case letter from the English alphabet
    
    Output: the letter that
    most frequently follows the given letter in the text. If the given letter is not found in the text or is not followed by any
    other letter, the function should return an empty string.
"""

#Import the necessary libraries
import os  

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")
def typical_successor(text, l):
    # First we convert the text to lower case
    text = text.lower()
    
    # Then we remove all non-letter characters and replace them with spaces
    text = ''.join([' ' if not i.isalpha() else i for i in text])
    
    # Now we find the index of the given letter
    index = text.find(l)
    
    # If the letter is not found, we return an empty string
    if index == -1:
        return ''
    
    # If the letter is found, we find the most frequent successor and how many times it appears after the letter
    else:
        # Then we find and count the successors of l in the text
        counts = {}
        for i in range(index, len(text)-1):
            if text[i] == l:
                if text[i+1] == ' ': # If the successor is a space, we skip it
                    continue
                elif text[i+1] in counts:
                    counts[text[i+1]] += 1
                else:
                    counts[text[i+1]] = 1
        # Finally we find the most frequent successor
        print(counts)
        most_frequent = max(counts, key=counts.get)
        
        return most_frequent
    
#test the function
text = 'Hello world. This usual salutation usually starts programming.'
print(typical_successor(text, 'l'))

#Another test
#with a long text
text = 'Hello world. This is sparta. Also this is a long text. I am writing this text to test the function. I hope it works.'
print(typical_successor(text, 'i'))