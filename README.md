# Second Largest Element

## Problem Statement

Given an array of integers, find the second largest distinct element.

### Example

**Input**
```
Enter the number of elements: 5
Enter the elements separated by space: 10 20 4 45 99
```

**Output**
```
Second Largest Element: 45
```

---

## Solutions

### 1. Using Sorting

**Approach**
- Remove duplicate elements using `set()`.
- Sort the array in ascending order.
- Print the second last element.

**Time Complexity:** O(n log n)

**Space Complexity:** O(n)

---

### 2. Without Sorting (Optimized)

**Approach**
- Traverse the array only once.
- Keep track of the largest and second largest elements.
- Update their values whenever a larger element is found.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---
## Concepts Used

- map()
- list()
- set()
- sort()
- float('-inf')
- Value Updating
- elif


---

## Key Takeaways

- The sorting approach is simple and easy to understand.
- The optimized approach is preferred in coding interviews because it runs in **O(n)** time.
- This problem helps build logic for solving maximum, minimum, and other array-based interview questions.