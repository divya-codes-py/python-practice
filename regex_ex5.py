import re

text = "Hello!!! This is... a TEST?? Clean   this   text!!!"

# Remove special characters
cleaned = re.sub(r'[^a-zA-Z\s]', '', text)

# Multiple spaces to single space
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

print(f"📝 Original: {text}")
print(f"✅ Cleaned: {cleaned}")
