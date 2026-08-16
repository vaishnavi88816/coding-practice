"""
Problem: Longest Common Suffix

Given a list of strings, return the longest common suffix.
If there is no common suffix, return an empty string.

Approach: Reverse Vertical Scanning

Compare characters from the end of all strings.
Stop at the first mismatch and return the common suffix.

Time Complexity: O(n × m)
Space Complexity: O(1)
"""

def longest_common_suffix(strings):
    # Edge case: Empty list
    if not strings:
        return ""

    # Take the first string as the reference
    reference = strings[0]

    suffix = ""

    # Compare characters from the last index
    for i in range(1, len(reference) + 1):

        current_char = reference[-i]

        for word in strings[1:]:

            # Stop if current string ends
            # or characters do not match
            if i > len(word) or word[-i] != current_char:
                return suffix

        # Add matching character at the beginning
        suffix = current_char + suffix

    return suffix


# Driver Code
strings = input("Enter words separated by space: ").lower().split()

result = longest_common_suffix(strings)

print("Longest Common Suffix:", result)