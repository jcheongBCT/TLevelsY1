import random as rnd
RandomNumber = rnd.randint(1, 10)
print("I have a random number between 1 and 10")

UserInput = int(input("Guess the number, you have three chances: "))
if UserInput == RandomNumber:
    print("You're grrreat!")
    exit()
elif UserInput < RandomNumber:
    print("You have guessed too low")
elif UserInput > RandomNumber:
    print("You have guessed too high")

UserInput = int(input("Guess the number, you have two chances: "))
if UserInput == RandomNumber:
    print("You're grrreat!")
    exit()
elif UserInput < RandomNumber:
    print("You have guessed too low")
elif UserInput > RandomNumber:
    print("You have guessed too high")

UserInput = int(input("Guess the number, last chance: "))
if UserInput == RandomNumber:
        print("You're grrreat!")
        exit()
elif UserInput < RandomNumber:
        print("You have guessed too low")
elif UserInput > RandomNumber:
        print("You have guessed too high")