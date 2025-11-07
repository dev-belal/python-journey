# Mini Project 1 - Snake Water Gun Game

🎮 My first Python mini project!
This simple game is inspired by the classic “Rock Paper Scissors” — but with a twist.
Here, the player competes against the computer in a **Snake–Water–Gun** match.

## 🧠 Concepts Covered

* Importing and using the `random` module
* Handling user input
* Conditional statements and game logic
* Loops and score tracking
* Displaying results with clear messages

## 💻 Example Code

```python
import random

def game():
    print("Snake, Water or Gun?")
    user = input("Your choice: ").lower()
    computer = random.choice(["snake", "water", "gun"])

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

game()
```

## 📚 Example Output

```
Snake, Water or Gun?
Your choice: gun
Computer chose: snake
You win! 🎉
```

## 🔗 Navigation

⬅️ [Previous → Chapter 8 - Practice Set](../Chapter%208%20-%20Practice%20Set/)
