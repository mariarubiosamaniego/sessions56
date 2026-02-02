money = 100000000

if money > 10 ** 9: #more than 1billion
    print("welcome to Forbes")
elif money > 10 ** 8:
    print("Welcome to Forbes up and coming")
elif money > 10 ** 7:
    print("Hope you like your ferraris")
else:
    print("sorry, you are not rich")

#change the number on the miney value to see how when you run you get different answers
#always start your commands with the least probable one because as soon as it matches it stops
#with elif we are able to add more than 2 possibilities