import re

sentence = "I have 3 cats, 2 dogs and 10 fish at home"

numbers = re.findall(r'\d+', sentence)
print(f"📝 Sentence: {sentence}")
print(f"🔢 Numbers found: {numbers}")
print(f"➕ Total: {sum(int(n) for n
