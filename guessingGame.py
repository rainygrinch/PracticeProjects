import random

number = random.randint(1, 20)
num_guesses = 6
guesses_left = num_guesses

print("I'm thinking of a number between 1 and 20. You have 6 guesses to get it right.")

while guesses_left > 0:
    guess_str = input("Guess the number: ")

    try:
        guess = int(guess_str)
    except ValueError:
        print("Sorry, that's not an integer. Please try again.")
        continue

    guesses_left -= 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {num_guesses-guesses_left} guesses.")
        break

    if guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
    else:
        print(f"Sorry, you didn't guess the number. The number was {number}.")