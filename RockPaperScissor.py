import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")

while True:

    print("\nChoose Rock, Paper or Scissors")
    user = input("Your choice: ").lower()

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose      : {user}")
    print(f"Computer chose : {computer}")

    if user == computer:
        print("Result: It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\n----- Score -----")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    play = input("\nPlay again? (yes/no): ").lower()

    if play != "yes":
        print("\nFinal Score")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")
        print("\nThanks for playing!")
        break