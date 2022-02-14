import random

top_of_range = input("What is the top of the range? ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("Please enter a positive number.")
        quit()

else:
    print("Please enter a number.")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number between 0 and " + str(top_of_range) + ": ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number.")
        continue

    if user_guess == random_number:
        print("You got it")
        break

    elif user_guess > random_number:
        print("You were too high")

    else:
        print("You were too low")

print("It took you " + str(guesses) + " guesses.")
