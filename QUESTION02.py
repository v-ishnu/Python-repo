"""
You are given a list of strings where each string represents a word. Write a Python program to perform the following tasks:

Count Word Frequency: Count the frequency of each word in the list.
Find the Longest Word: Identify the longest word in the list.
Filter by Length: Create a new list that contains only the words longer than a given length n.
Reverse Each Word: Reverse the characters in each word in the original list.

"""

word = ["Apple", "Elephant", "Cononel", "Lieutenant", "Micro-Biology", "Nanotechnology"]


# Count Word Frequency
Word_frequency = {} 

for i in word:
    if i in Word_frequency:
        Word_frequency[i] += 1
    else:
        Word_frequency[i] = 1
print("Word Frequency :", Word_frequency)



# Longet Word
longest_word = max(word)

# Filter Length
Filter_length = []
n = int(input('Enter length of word:'))

for i in word:
    word_length = len(i)  # get word length in integer
    if word_length >= n:
        Filter_length.append(i)
print("Filtered words:", Filter_length)


# Reverse_word
Reverse_word = []
for i in word:
    Reverse_word.append(word [:: -1])
print("Reverse Word:",Reverse_word)
