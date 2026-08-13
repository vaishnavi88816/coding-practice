"""
Question: Count Frequency of Each Character

Problem:
Given a string, count how many times each character appears.

Example:
Input: banana

Output:
b : 1
a : 3
n : 2
"""

text = input("Enter a string: ")

# Dictionary to store character and its frequency
freq = {}

# Check each character one by one
for ch in text:

    # If character already exists, increase its count
    if ch in freq:
        freq[ch] = freq[ch] + 1

    # If character appears for the first time, set count to 1
    else:
        freq[ch] = 1

# Print each character with its frequency
for ch, count in freq.items():
    print(ch, ":", count)