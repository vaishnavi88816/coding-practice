def first_non_repeating_index(s):
    """
    Returns the index of the first non-repeating character.
    If all characters repeat, returns -1.
    """

    # Dictionary to store character frequencies
    freq = {}

    # Count the frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find the index of the first unique character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    # No unique character found
    return -1


# Driver Code
string = input("Enter a string: ")

result = first_non_repeating_index(string)

print("Index of first non-repeating character:", result)