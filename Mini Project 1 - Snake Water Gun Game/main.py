# 🐍 Mini Project: Snake, Water and Gun Game
# Concepts used: dictionary, functions, conditionals, loops, random, input/output

import random

# Step 1️⃣: Create dictionary for rules
# Snake 🐍 drinks Water 💧, Gun 🔫 kills Snake 🐍, and Water 💧 rusts Gun 🔫
rules = {
    'snake': 'water',   # Snake wins over water
    'water': 'gun',     # Water wins over gun
    'gun': 'snake'      # Gun wins over snake
}

# Step 2️⃣: Define function to decide the winner
def check_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie!"
    elif rules[user_choice] == comp_choice:
        return "You Win!"
    else:
        return "Computer Wins!"

# Step 3️⃣: Main game function
def play_game():
    print("🎮 Welcome to Snake, Water and Gun Game 🎮")
    print("Choices: Snake 🐍 | Water 💧 | Gun 🔫")

    # Initialize score counters
    user_score = 0
    comp_score = 0

    # Play multiple rounds
    rounds = int(input("How many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # Take user input
        user_choice = input("Enter your choice (snake/water/gun): ").lower()

        # Validate input
        if user_choice not in rules.keys():
            print("❌ Invalid choice! Please choose from snake, water, or gun.")
            continue

        # Computer random choice
        comp_choice = random.choice(list(rules.keys()))
        print(f"Computer chose: {comp_choice.capitalize()}")

        # Decide winner
        result = check_winner(user_choice, comp_choice)
        print(result)

        # Update scores
        if result == "You Win!":
            user_score += 1
        elif result == "Computer Wins!":
            comp_score += 1

    # Step 4️⃣: Display final results
    print("\n🏁 Final Scores 🏁")
    print(f"You: {user_score} | Computer: {comp_score}")

    if user_score > comp_score:
        print("🎉 Congratulations! You are the overall Winner! 🎉")
    elif comp_score > user_score:
        print("💻 Computer wins the game! Better luck next time!")
    else:
        print("🤝 It’s an overall Tie!")

# Step 5️⃣: Run the game
play_game()
