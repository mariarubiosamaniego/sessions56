n = 0
while n < 10:
    print(n)
    n = n + 1

#range does the initial state and increment after each iteration
#range knows that it starts from 0 always, 0 is implicit, but you have to give an end
#1 is also the default increment -> range(0, 10, 1) just really needs the 10 to tell them where to end
#0 is included within the range but 10 is excluded
for i in range(10):
    print(i)

for i in range(0, 100, 10):
    print(i)

#print the multiplication table until 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")
    print()
