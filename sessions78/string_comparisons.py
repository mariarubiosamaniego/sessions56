s = "hello world"

print(help(s.capitalize))
print("heLLO WORLd!".capitalize())

print(help(s.center))
print("BOB".center(30, "*"))


#find finds the position where a substring can be found
s = "I can see a cat on the street. The street is nice. The cat is black"
print("The position of the cat is:", s.find("cat"))
print("The position of the next cat is:", s.find("cat", 9))
print("find returns -1 if we cannot find it:", s.find("dog"))

emails = "bob@gmail.com and alice@yahoo.com and james@facebook.com"
#how many emails
#count method just counts inside the string
print(emails.count("@"))
pos = 0
while True:
    pos = emails.find("@", pos)
    if pos == -1:
        break
    print("Found one email at that position", pos)
    pos += 1

#replace will replace part of a string with another one
print(s)
print(s.replace("cat", "parrot"))
print(s.replace(" ", "//"))

#split will  break the string into components
print(s.split())



