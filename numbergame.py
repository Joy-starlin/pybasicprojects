import random

secret_number = random.randint(0, 100)
attempts_left = 5

print("Guess the number between 0 and 100.")

while attempts_left > 0:
    guess_input = input(f"Enter your guess ({attempts_left} attempts left): ")
    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if guess < 0 or guess > 100:
        print("Your guess must be between 0 and 100.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    attempts_left -= 1
else:
    print("Sorry, you've used all your attempts. The correct number was", secret_number)
