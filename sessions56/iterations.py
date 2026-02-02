num = 1
while num <= 10:
    print(num)
    num = num + 1

#the num = num +1 makes the condition to stop being infinite
#ran until the condition becomes false (never)

import random

money = 10000
counter = 1

while money > 0:
    print("money:", money)
    expense = random.randint(1, 100)
    print("iteration", counter, "expense =", expense)

    money = money - expense
    counter = counter + 1
#counter=1 because it is the first iteration
#we repeat the loop as long as money is greater than 0
#everything indented under while runs once per iteration: print displays the amount of money left
#available, expense = random.randint(1, 100) generates a random expense from 1 to 100 and changed with very loop
#and the last print jut displays the iteration and its expense.
#counter + 1 increases counter each time
#the money - expense part makes the loop finite ending the money at some point

