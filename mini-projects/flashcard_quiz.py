flashcards = [
    {"question": "Python alli list create maadalu?", "answer": "[]"},
    {"question": "Python alli dictionary create maadalu?", "answer": "{}"},
    {"question": "Python alli comment haakalu?", "answer": "#"},
    {"question": "String length find maadalu yaavudu function?", "answer": "len()"},
    {"question": "Random module import maadalu?", "answer": "import random"},
    {"question": "User input tegeyalu yaavudu function?", "answer": "input()"},
    {"question": "Number to string convert maadalu?", "answer": "str()"},
    {"question": "String to number convert maadalu?", "answer": "int()"},
    {"question": "List alli item add maadalu?", "answer": ".append()"},
    {"question": "Screen clear maadalu yaavudu module?", "answer": "os"}
]

def show_flashcard(card, number, total):
    print(f"\n🃏 Card {number}/{total}")
    print("=" * 35)
    print(f"❓ {card['question']}")
    input("\n👆 Answer nenapu maadi, ENTER haaki nodi...")
    print(f"✅ Answer: {card['answer']}")

def quiz_mode(cards):
    score = 0
    print("\n📝 Quiz Mode!")
    print("=" * 35)
    for i, card in enumerate(cards):
        print(f"\nQ{i+1}: {card['question']}")
        user_answer = input("Nimma answer: ").strip().lower()
        correct = card['answer'].strip().lower()
        if user_answer == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Tappu! Correct: {card['answer']}")
    print(f"\n🏆 Score: {score}/{len(cards)}")

def main():
    import random
    print("🃏 Flashcard Quiz App!")
    print("=" * 35)

    while True:
        print("\n📌 Menu:")
        print("1. Flashcards nodu")
        print("2. Quiz mode")
        print("3. Exit")

        choice = input("\nOption (1-3): ")

        if choice == "1":
            cards = flashcards.copy()
            random.shuffle(cards)
            for i, card in enumerate(cards):
                show_flashcard(card, i+1, len(cards))

        elif choice == "2":
            cards = flashcards.copy()
            random.shuffle(cards)
            quiz_mode(cards)

        elif choice == "3":
            print("👋 Bye!")
            break
        else:
            print("⚠️ 1 to 3 maatra type maadi!")

main()
