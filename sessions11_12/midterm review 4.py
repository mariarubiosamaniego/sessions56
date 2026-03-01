#exercise 1

print(type(2+3))
print(type(6/2))
print(type(2!=3))
print(type(5 or 6))
print(type(print))
print(type(print(2*2)))
print(type("abc".find))
print(type("bubu"*2))
print(type("bubu"*int(4/2)))    #add int here to multiply bc you cannot multiply a float
print(type["abc", 2])
print(type("abc"[2]))
print(type("abcabcabc".split("a")))

#exercise 2
print(2+3)
print(6/2)
print(2!=3)
print(5 or 6)
print(print)
print("abc", 2)
print("bubu"*int(4/2))
print([1,2,3].append("John"))
print(len(["abc",2]))

#exercise 3
a=2
b=3
c="abc"
print(a,b,c)
print(a,b,c,sep=";")
a += 2
a == 5
d=c.find("b")
print(d)
print(d==True)
e = str(a) + str(b) + str(c) + str(d)

#exercise 4
def print_b_words(filename):
    f = open(filename, "r")

    for line in f:
        words = line.split()

        for word in words:
            word = word.strip()

            if len(word) == 3 and word[0] == "b":
                print(word)

    f.close()
#print_b_words("yourfile.txt")

#exercise 5
def get_divisors(number):
    divisors = []
    for i in range(1, number +1):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(get_divisors(78))

#exercise 6
def multiple_six():
    while True:
        try:
            number = int(input("Enter a multiple of 6:"))
            if number % 6 == 0:
                return number
            else:
                print("That is not a multiple of 6, try again")
        except:
            print("Invalid input, must be an integer")
print(multiple_six())
