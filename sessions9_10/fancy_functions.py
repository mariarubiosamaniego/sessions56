def add_numbers(a, b, c=0):
    return a + b + c

add_numbers(1, 2)
print(add_numbers(5, 8, 9))

#the function returns, but i am printing the result
#calling the function does not print anything


#functions can call other functions
#the name is bond, james bond

def greeting(name):
    return f"The name is: {name}"

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(greeting("Sanchez, Maria Sanchez"))
print(greeting(bond_name("Jerry", "Bond")))