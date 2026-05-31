# Problem: Convert nested list into a single flat list
# Interview Question: "Remove all inner lists and make one flat list"

# Basic Approach - One level deep only
# Time Complexity: O(n)
# Space Complexity: O(n)
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            for element in item:
                flat.append(element)
        else:
            flat.append(item)
    return flat

# Recursive Approach - Any depth
# Time Complexity: O(n)
# Space Complexity: O(n)
def flatten_recursive(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_recursive(item))
        else:
            flat.append(item)
    return flat

# Test
nested = [1, [2, 3], [4, 5], 6, [7, 8]]
deep = [1, [2, [3, [4, 5]]]]
print(f"Nested: {nested}")
print(f"Basic: {flatten_list(nested)}")
print(f"Deep nested: {deep}")
print(f"Recursive: {flatten_recursive(deep)}")
