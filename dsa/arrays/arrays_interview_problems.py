# Problem: Find maximum and minimum number in a list
# Interview Question: "Without using built-in max/min, find largest and smallest"

def find_max_min(numbers):
    if not numbers:
        return None, None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum


# Test
nums = [3, 7, 1, 9, 4, 6, 2]
big, small = find_max_min(nums)
print(f"List: {nums}")
print(f"Maximum: {big}")
print(f"Minimum: {small}")
