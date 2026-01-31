#calculate the net when we have thr gross and some constraints
try:
    gross = float(input("Type gross salary: "))
    children = int(input("Type number of children: "))
except ValueError:
    print("Wrong input! They must be numbers.")
else:
    if gross < 1000:
        base_rate = 0.10
    elif gross < 2000:
        base_rate = 0.12
    elif gross < 4000:
        base_rate = 0.14
    elif gross > 4000:
        base_rate = 0.18

if gross < 2000:
    discount = children * 0.01
else:
    discount = children * 0.005

final_rate =base_rate - discount
if final_rate < 0:
    tax_rate = 0

net = gross * (1 - final_rate)
print(net)
