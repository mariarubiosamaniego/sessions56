s1 = "hello world"
s2 = 'hello world'
print(s1)
print(s2)

#if you create a new s1, old s1 is deleted and changed to the new one
s1 = "hello world 89e587169"
print(s1[1])   #we now only print the first digit of the new s1 (but the first character is the second really - digit 0 is h
print(s1[-1])  #last digit
print(len(s1)) #amount of characters

#index needs to be integer
print(8/4)
print(s1[8//4])