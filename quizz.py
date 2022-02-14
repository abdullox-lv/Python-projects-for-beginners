print("Welcome to my compyuter quiz!")

name = input("Enter your name: ")
print("Yuo are welcome", name)
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play game :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!  +5xp")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!  +5xp")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!  +5xp")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!  +5xp")
    score += 1
else:
    print("Incorrect")

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print("Correct!  +5xp")
    score += 1
else:
    print("Incorrect")

percent = float((score / 4) * 100)
print("You got " + str(score) + " questions correct!")
print("You got " + str(percent) + "%.")
print(name + "You got " + str(score * 5) + " xp")
