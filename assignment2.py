""" 
=================================================================================
    Student Name:   Jesus Arambula
    Student ID:     916721083
    Student email:  jarambula@mail.sfsu.edu
    Professor:      Dr. Anagha Kullkarni
    Class:          CSC 620-01, Natural Language Technologies
    Due Date:       February 7th, 2022 @5:00 PM (02/07/2022)
    Purpose:
        Get a more in depth grasp on the nltk module
        and get hands-on experience with tokenizing strings.
        The levenshtein algorithm was also put into use
        as it was used to check similarities between two strings
    Additional Notes:
        Please ignore the commented print statements. They were used for 
        personal debugging purposes.
        The truncate() function was added only to make the relative frequencies
        more readable. Link to the truncate() code was also provided.
=================================================================================
"""

# import all needed modules for this program
import nltk
from nltk.corpus import words
from nltk.probability import FreqDist
# The difflib module is used to compare similarities for Step 4
import difflib

# Function truncate reduces decimal place
# Used to make relative frequency count shorter
# Taken from https://realpython.com/python-rounding/
# NOT PART OF THE ASSIGNMENT
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

print("======= Step 1 =======")

# String to be tokenized and take frequency of
string = """Betty bought butter but the butter was bitter so Betty bought better butter to make the bitter butter better"""

print("The string to be tokenized is: ")
print(f"'{string}'")

# Tokenize the string
tokens = nltk.word_tokenize(string)
# declare a frequency desitribution variable
frequencyDist = FreqDist()


# print(len(tokens))    // Debug print statement

# Number of words in string
tokenCount = len(tokens)
# Number of unique words in string
typeCount = len(set(tokens))
# Relative frequency

print("======= Step 2 =======")
print(f"There are {tokenCount} total words (tokens), and {typeCount} unique words (types)")

for token in tokens:
    # Counts the frequency of the words in the string
    frequencyDist[token] += 1
    # print(token in words.words())     // Debug print statement

# Turn the frequency distribution into a dictionary
frequencyDict = dict(frequencyDist)

# print(frequencyDict)  // Debug print statement

print("======= Step 3 =======")

relativeFrequencyDict = {}

for token in frequencyDict:
    relativeFrequencyDict[token] = frequencyDict[token] / tokenCount
    print(f"The relative frequency of '{token}' is {truncate(relativeFrequencyDict[token], 3)}")
    # print(frequencyDict[token])   // Debug print statement

# print(relativeFrequencyDict)  // Debug print statement

print("======= Step 4 =======")

# Levenshtein function
# as per the lecture slides
def levenshtein(x, y):
    # Base cases
    # If there's no x, return lenght of y
    if not x:
        return len(y)
    # If there's no y, return length of x
    if not y:
        return len(x)
    # Recursive step
    return min(
        # Remove first character
        levenshtein(x[1:], y) + 1,
        # Insert first character
        levenshtein(x, y[1:]) + 1,
        # Replace first character
        levenshtein(x[1:], y[1:]) + (x[0] != y[0])
    )

# Declare a list for similar words
similarList = []
userInput = input("Enter a word: ")

# Checks if the user input is in the vocabulary
if userInput in words.words():
    print(f"'{userInput}' is a complete and correct word in English.")
else:
    # If not, begins checking how similar each word is to user's input
    print("Calculating...")
    for word in words.words():
        sequence = difflib.SequenceMatcher(None, userInput, word).ratio()
        # Checks if the sequence is higher than 80% simlar
        # and the levenshtein distance is less than 2
        if sequence >= .80 and levenshtein(userInput, word) <= 2:
            similarList.append(word)
    print("===========================================================================")

    # Checks if the list of similar words is empty
    if not similarList:
        print(f"'{userInput}' is not similar to any word from the chosen vocabulary.")
    else:
        # If not, prints all of the similar words stored in the similar word list
        print(f"Here are the closest words similar to the word '{userInput}':")
        for word in similarList:
            print(f" - {word}")

# print(len(words.words())) // Debug print statement

# print(similarWords) // Debug print statement

