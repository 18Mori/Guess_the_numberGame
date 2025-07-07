import random

def get_difficulty():
    while True:
        difficulty = input("\nChoose difficulty level (easy, medium, hard): ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "medium":
            return 8
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid difficulty🤨. Please choose easy, medium, or hard.")

def play_game():
    random_number = random.randint(1, 100)
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    max_attempts = get_difficulty()
    attempts = max_attempts
    print(f"You have {max_attempts} attempts to guess the number.")

    guessed_correctly = False

    while attempts > 0:
        try:
            guess = int(input(f"Attempt {max_attempts - attempts + 1}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Invalid input. Bro!🤬 Please enter a whole number.")
            continue
        
        if guess < 1 or guess > 100:
            print("Your guess is out of the valid range (1-100). Try again.")
            continue

        attempts -= 1
        if guess == random_number:
            print(f"Congratulations!🎉 You've guessed the number in {max_attempts - attempts} attempts.")
            return
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

    if not guessed_correctly:
        print("\nGame Over!😭 You ran out of guesses.")
        print(f"The secret number was: {random_number}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == "y":
        print("Great! Let's play again!🎮")
    elif play_again == "n":
        print("Thanks for playing! Goodbye!👋")
        exit()
    else:
        print("Invalid input. Please enter yes or no.")

play_game()
