#you can assign a string to a variable
s1 = ("hello")
s2 = ("bye")

#you can add 2 strings: you get a string back
print(s1+s2)

#you can multiply a string via an integer
print(s1*2)
print(4*s2)

#you can iterate over a string via for
#c=character=char
for c in s1:
    print(c)

s1 = "I am very angry"
s2 = ("!")
print(s1+s2)

for c in s1:
    print(c*5, end="")
print()

s2 = ""
for c in s1:
    s2 = s2 + c*5
    print(s2)