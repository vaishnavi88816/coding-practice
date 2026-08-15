
def first_non_repeating(s):
    """
    Returns the first non-repeating character.
    If all characters repeat, returns -1.
    """

    # Dictionary to store character frequencies
    freq = {}

    # Count the frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find the first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    # No unique character found
    return -1


# Driver Code
string = input("Enter a string: ")

result = first_non_repeating(string)

print("First non-repeating character:", result) 