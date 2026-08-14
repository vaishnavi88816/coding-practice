"""
Problem: Two Sum

Given an array of integers and a target value,
return the indices of two numbers whose sum equals the target.

Approach:
1. Use a dictionary to store each number with its index.
2. For every element, calculate:
       needed = target - current
3. If 'needed' is already present in the dictionary,
   return both indices.
4. Otherwise, store the current number with its index.

Time Complexity: O(n)
Space Complexity: O(n)

Concepts Used:
- Function
- Dictionary (Hash Map)
- Loop
- Condition
- Return Statement
"""

def two_sum(arr, target):
    seen = {}  # Stores value as key and index as value

    for i in range(len(arr)):
        current = arr[i]
        needed = target - current

        # Check whether the required number already exists
        if needed in seen:
            return seen[needed], i

        # Store current value with its index
        seen[current] = i

    return None


# User Input
n = int(input("Enter the number of elements: "))

print("Enter the elements:")
arr = list(map(int, input().split()))

target = int(input("Enter the target sum: "))

result = two_sum(arr, target)

if result:
    print("Indices:", result[0], result[1])
else:
    print("No pair found.")