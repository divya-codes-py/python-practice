# Problem: Merge two sorted lists into one sorted list
# Interview Question: "Combine two sorted lists without using sort()"

# Optimal Approach - Two Pointer
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

def merge_sorted(arr1, arr2):
    merged = []
    i = 0
    j = 0

    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Test
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Merged: {merge_sorted(arr1, arr2)}")
