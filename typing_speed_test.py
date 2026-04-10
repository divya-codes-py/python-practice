import time
import random

sentences = [
    "python is a great programming language",
    "practice makes a man perfect",
    "coding every day improves your skills",
    "functions help us reuse our code easily",
    "lists and dictionaries are very useful in python",
    "keep learning and never give up",
    "every expert was once a beginner",
    "consistency is the key to success"
]

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1
    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def typing_test():
    print("⌨️  Typing Speed Test!")
    print("=" * 40)
    print("Sentence nodidare, ENTER haaki start maadi!")
    input()

    sentence = random.choice(sentences)

    print(f"\n📝 Type this:\n")
    print(f"   {sentence}\n")
    print("=" * 40)

    start_time = time.time()
    typed = input("Nimma answer: ")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    words_typed = len(typed.split())
    wpm = round((words_typed / time_taken) * 60, 2)
    accuracy = calculate_accuracy(sentence, typed)

    print("\n" + "=" * 40)
    print("📊 Nimma Results:")
    print(f"   ⏱️  Time: {time_taken} seconds")
    print(f"   🚀 Speed: {wpm} WPM (words per minute)")
    print(f"   🎯 Accuracy: {accuracy}%")

    if accuracy == 100:
        print("\n🌟 Perfect! Bahala channagide!")
    elif accuracy >= 80:
        print("\n👍 Channagide! Keep practicing!")
    else:
        print("\n💪 Practice maadi, improve aaguttire!")

while True:
    typing_test()
    again = input("\nMatte try maadali? (yes/no): ").lower()
    if again != "yes":
        print("👋 Bye! Keep typing! ⌨️")
        break
