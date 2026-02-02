name = input("What is your name? ")
print("hello", name)

age = input("Enter your age: ")
age = int(age)
print("you were born in", 2025- age)

#defining age in here is redundant, normally we just define it after try

#When you want to print an input or a variable, you should type the answer
#and click enter on the lower part where the stuff is being run - that way you will
#get the things ok and get to the next line, until you don't type in there the answer pycharm wont continue printing.

#input() only returns strings even though you add a number it will come back as a text, which makes
#int() necessary so you can get numbers back, it gives you integers. It waits for the user to type something in the console
#int() turns text into numbers because in input() Python stores "25" not 25 so we cannot do math
#using int() with sth that doesnt look like a number gives ValueError

try:
    age = int(input("Enter your age: "))
    print("you were born in", 2025 - age)
except ValueError:
    print("I am sorry", name, "but that is not a real number")

#everything is running smoothly because the answer is indeed a number

#try to run the code, but it might fail so the code is risky: converting input, maths and opening lines
#except means that if you get ValueError do this instead

try:
    age = int(input("Enter your age: "))
    print("you were born in", 2025 - age)
#if nothing goes wrong we jump to except

except ValueError:
    print("I am sorry", name, "but that is not a real number")

#this pops up if we type abc so int(abc) fails so then because it was ValueError this command happens

except ZeroDivisionError:
    print("You can't divide by zero")

#because at some point you are dividing by 0

else:  # else is only when no exception happens
    print("thank you for playing fair")

finally:
    print("End of game")  # this one always happens no matter what

#try to do the top, if something goes wrong, handle it, if nothing goes wrong,
#do sth else and no matter what do teh finally command