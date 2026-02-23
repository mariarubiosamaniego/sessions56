a = []  #empty list
a = [1, 2, 4, 9]
print(a)
a = [True, [1, "Bob", -8.2], False, "Jamaica", 99.99]
print(a)
print(len(a))  #amount of items on the list
a[2] = "No longer False"  #lists are mutable
print(a)

print(a[::-1])
print(a[2::2])

print([1, 2, 3] + ["Bob", "Bob", "BOBOBOB"])
print([1, 2, 9]*4)
a = ["Bob", "James", "Jane"]
for item in a:  #iterate over a list
    print(item)