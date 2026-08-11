n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements separated by space: ").split()))

arr = list(set(arr))
arr.sort()

if len(arr) < 2:
    print("No second largest element")
else:
    print("Second Largest Element:", arr[-2])