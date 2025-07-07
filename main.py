import random

def get_difficulty():
    difficulty = input("\nChoose difficulty level (easy, medium, hard): ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 8
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid difficulty. Defaulting to medium.")
        return 8

def play_game():
    random_number = random.randint(1, 100)
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Difficulty level: {get_difficulty()}")
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == random_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

play_game()

