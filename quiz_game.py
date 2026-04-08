questions = [
    {
        "question": "Python yaar create maadidru?",
        "options": ["a) James Gosling", "b) Guido van Rossum", 
                    "c) Dennis Ritchie", "d) Bill Gates"],
        "answer": "b"
    },
    {
        "question": "Python alli print madoke yaavudu?",
        "options": ["a) echo", "b) console.log", 
                    "c) print()", "d) printf"],
        "answer": "c"
    },
    {
        "question": "List create madoke yaavudu?",
        "options": ["a) {}", "b) ()", 
                    "c) []", "d) <>"],
        "answer": "c"
    },
    {
        "question": "Comment haakoke yaavudu?",
        "options": ["a) //", "b) #", 
                    "c) --", "d) **"],
        "answer": "b"
    },
    {
        "question": "int('10') output enu?",
        "options": ["a) '10'", "b) 10", 
                    "c) 10.0", "d) Error"],
        "answer": "b"
    }
]

score = 0

print("🐍 Python Quiz Game!")
print("--------------------")

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['question']}")
    for option in q['options']:
        print(option)
    
    answer = input("Ninna answer (a/b/c/d): ")
    
    if answer == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Answer: {q['answer']}")

print("\n--------------------")
print(f"🎯 Ninna Score: {score}/5")

if score == 5:
    print("Outstanding! 🌟")
elif score >= 3:
    print("Well done! 👍")
else:
    print("Keep practicing! 💪")
