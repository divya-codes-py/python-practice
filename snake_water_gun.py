import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "player"
    else:
        return "computer"

def display_emoji(choice):
    emojis = {"snake": "🐍", "water": "💧", "gun": "🔫"}
    return emojis[choice]

def main():
    print("🎮 Snake Water Gun Game!")
    print("=" * 35)
    print("Rules:")
    print("🐍 Snake drinks 💧 Water")
    print("💧 Water douses 🔫 Gun")
    print("🔫 Gun kills 🐍 Snake")
    print("=" * 35)

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\n📌 Aayke maadi:")
        print("1. Snake 🐍")
        print("2. Water 💧")
        print("3. Gun 🔫")
        print("4. Exit")

        choice = input("\nOption (1-4): ")

        if choice == "1":
            player = "snake"
        elif choice == "2":
            player = "water"
        elif choice == "3":
            player = "gun"
        elif choice == "4":
            break
        else:
            print("⚠️ 1 to 4 maatra type maadi!")
            continue

        computer = get_computer_choice()
        rounds += 1

        print(f"\nNeevu: {display_emoji(player)} {player.upper()}")
        print(f"Computer: {display_emoji(computer)} {computer.upper()}")

        result = get_winner(player, computer)

        if result == "draw":
            print("🤝 Draw!")
        elif result == "player":
            print("🎉 Neevu gellide!")
            player_score += 1
        else:
            print("💀 Computer gellitu!")
            computer_score += 1

        print(f"\n📊 Score — Neevu: {player_score} | Computer: {computer_score}")

    print("\n" + "=" * 35)
    print(f"🏆 Final Score:")
    print(f"   Neevu: {player_score}")
    print(f"   Computer: {computer_score}")
    print(f"   Rounds: {rounds}")

    if player_score > computer_score:
        print("🌟 Neevu gellide! Congratulations!")
    elif computer_score > player_score:
        print("💻 Computer gellitu! Matte try maadi!")
    else:
        print("🤝 Draw! Channagide!")

main()
