words = ["python", "java", "javascript", "c++", "ruby"]

result = [word.upper() for word in words if len(word) > 4]
print(f"Filtered words: {result}")
