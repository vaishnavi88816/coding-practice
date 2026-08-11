n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements separated by space: ").split()))

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second largest element")
else:
    print("Second Largest Element:", second_largest)