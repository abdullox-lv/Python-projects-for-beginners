import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid input")
        continue

    random_index = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_input = options[random_index]
    print("Computer picked: " + computer_input)

    if user_input == computer_input:
        print("It's a tie!")

    elif user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_score += 1

    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_score += 1

    elif user_input == "scissors" and computer_input == "paper":
        print("You won")
        user_score += 1

    else:
        print("You lost!")
        computer_score += 1


print("You win: " + str(user_score) + " times")
print("Computer win: " + str(computer_score) + " times")
print("Goodbye!")
