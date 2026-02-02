#conditions
#3 ways to do IF:
name = input("What is your name? ")
choice = input("Do you want to play a game? (y/n)")
if choice == "y":
    print("hello", name)

#we type name to store it when writing it in the console
#choice enables choosing yes or no so with the if statement we check the choice
#here there is no else so nothing happens if the condition is not met

#2 type of IF -> if + else
import random

number = random.randint(1, 100)

if number % 2 == 0:
    print("even steven")
else:
    print("nothing")

#same as above but now if the answer of choice is no, the else command happens