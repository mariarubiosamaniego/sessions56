import random
#add random numbers between -10 and 10
total = 0
for i in range(100):
    total = total + random.randint(-10, 10)
    print(total)

def greeting():
    print("Hello")
    print("Hola")
    print("Bonjour")
    print("Salem")
    print("Ciao")
    print("Tschus")

for i in range(3):
    greeting()
print("Now we do something else")
for i in range(5):
    greeting()

def enhanced_greeting(name):
    print("Hello", name)
    print("Hola", name)
    print("Bonjour", name)
    print("Salem", name)
    print("Ciao", name)

def enhanced_greeting2(name):
    """
    Prints greetings in other languages towards another person
    :param name: the name of the person
    :return: str
    """""
    message = ""
    message += f"Hello {name}\n"
    message += f"Hola {name}\n"
    message += f"Bonjour {name}\n"
    message += f"Ciao {name}\n"
    return message

enhanced_greeting("Valeria")
enhanced_greeting("Maria")

print(help(enhanced_greeting))

result = enhanced_greeting2("Maria")

print(f"The greetings are: {result}")

#the first function prints, the secind one returns