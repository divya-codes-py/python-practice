import random

choices = ["stone", "paper", "scissors"]

while True:
    user = input("\nEnter your choice (stone/paper/scissors): ")
    computer = random.choice(choices)
    
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("🤝 Its a Tie!")
    elif user == "stone" and computer == "scissors":
        print("🎉 You Win!")
    elif user == "paper" and computer == "stone":
        print("🎉 You Win!")
    elif user == "scissors" and computer == "paper":
        print("🎉 You Win!")
    else:
        print("😞 Computer Wins!")
    
    again = input("Play again? (yes/no): ")
    if again == "no":
        print("Thanks for playing! 👋")
        break
