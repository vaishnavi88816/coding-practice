"""
Problem: Contains Duplicate

Description:
Given a list of integers, return True if any value appears more than once.
Otherwise, return False.

Example:
Input:
1 2 3 1

Output:
True

Approach:
- Create an empty set to store visited elements.
- Traverse the list one by one.
- If the current element is already in the set, return True.
- Otherwise, add the element to the set.
- If the loop finishes without finding any duplicate, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)

    return False


numbers = list(map(int, input("Enter the numbers: ").split()))
print("Contains Duplicate:", contains_duplicate(numbers))