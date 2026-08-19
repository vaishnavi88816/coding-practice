def move_zeroes(numbers):
    # j points to the position where the next non-zero element should be placed
    j = 0

    # i scans every element of the array
    for i in range(len(numbers)):

        # Process only non-zero elements
        if numbers[i] != 0:

            # Place the non-zero element at j position
            numbers[i], numbers[j] = numbers[j], numbers[i]

            # Move j to the next available position
            j += 1

    return numbers


# Take array input from the user
numbers = list(map(int, input("Enter the array elements: ").split()))

# Call the function
result = move_zeroes(numbers)

# Display the result
print("Array after moving zeroes:", result)