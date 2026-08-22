"""
Problem: Rotate Array

Description:
Given an array, rotate it to the right by k positions.

Example:
Input:
[1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]

Approach:
- Reduce k using k % n to avoid unnecessary rotations.
- Reverse the complete array.
- Reverse the first k elements.
- Reverse the remaining elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def reverse(numbers, left, right):
    # Reverse the elements between left and right
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1


def rotate_array(numbers, k):
    # Handle an empty array
    if not numbers:
        return numbers

    # Reduce unnecessary rotations
    k = k % len(numbers)

    # Reverse the complete array
    reverse(numbers, 0, len(numbers) - 1)

    # Reverse the first k elements
    reverse(numbers, 0, k - 1)

    # Reverse the remaining elements
    reverse(numbers, k, len(numbers) - 1)

    return numbers


# Take input from the user
numbers = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the number of rotations: "))

# Rotate the array
result = rotate_array(numbers, k)

# Display the result
print("Rotated array:", result)