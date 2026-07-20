count =0
number =25
try:
    while count < 5:
        guess = int(input("Enter your guess number from 0-100: "))
        if guess == number:
            print("Congratulations! You guessed it right.")
            break
        else:
            print("Try again.")
        count += 1
    else:
        print("Sorry, you've used all your attempts. The correct number was", number)
except ValueError:
    print("Please enter a valid number.")
