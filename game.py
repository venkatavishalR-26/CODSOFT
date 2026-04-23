import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice(user_history):
    # Simple AI: try to counter the user's most frequent move
    if not user_history:
        return random.choice(choices)

    most_common = max(set(user_history), key=user_history.count)

    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("=== Advanced Rock Paper Scissors ===")

    rounds = int(input("Enter number of rounds (best of): "))
    user_score = 0
    comp_score = 0
    user_history = []
    game_history = []

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in choices:
                break
            print("Invalid choice! Try again.")

        user_history.append(user_choice)
        comp_choice = get_computer_choice(user_history)

        print(f"Computer chose: {comp_choice}")

        winner = decide_winner(user_choice, comp_choice)

        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            comp_score += 1
        else:
            print("It's a draw!")

        game_history.append((user_choice, comp_choice, winner))

        print(f"Score -> You: {user_score} | Computer: {comp_score}")

    print("\n=== Final Result ===")
    if user_score > comp_score:
        print("🎉 You won the game!")
    elif comp_score > user_score:
        print("💻 Computer won the game!")
    else:
        print("🤝 It's a tie!")

    print("\nGame History:")
    for i, (u, c, w) in enumerate(game_history, 1):
        print(f"Round {i}: You={u}, Computer={c}, Winner={w}")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()