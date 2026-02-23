a = [1, 2, 3]
a.append("John")
a.append("Doe")
print(a)

#a.append adds something at the end of the list,
#only 1 at a time. a.append to add to list a, b.append to add to list b

#extend is same as +
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a2.extend(a1)
print(a2)
a2.sort(reverse = True)
print(a2)

#extend adds items from another list, multiple things individually

