"""
Problem: Longest Common Prefix

Given a list of strings, return the longest common prefix.
If there is no common prefix, return an empty string.

Approach: Vertical Scanning
Time Complexity: O(n × m)
Space Complexity: O(1)
"""

def longest_common_prefix(strings):
    # Edge case: Empty list
    if not strings:
        return ""

    # Take the first string as the reference
    reference = strings[0]

    # Compare each character with all other strings
    for i in range(len(reference)):
        for word in strings[1:]:

            # Return the prefix if a mismatch is found
            if i >= len(word) or word[i] != reference[i]:
                return reference[:i]

    # Entire reference is the common prefix
    return reference


# Driver Code
strings = input("Enter words separated by space: ").lower().split()

result = longest_common_prefix(strings)

print("Longest Common Prefix:", result)