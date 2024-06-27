def sort_num(numbers):
    # This function only sorts the numbers variable and returns the sorted numbers back
    numbers.sort()
    return numbers


numbers = [6, 4, 7, 9, 1, 3, 8, 2, 5, 10]

# Create variable that uses the sorted list from the sort_num function above
sorted_nums = sort_num(numbers)

# Print sorted_nums variable
print('Sorted Numbers: ', sorted_nums)


