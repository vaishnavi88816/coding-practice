

n = int(input("Enter the value of N: "))

arr = list(map(int, input(f"Enter {n-1} elements separated by space: ").split()))

expected_sum = n * (n + 1) // 2

actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("Missing Number:", missing)