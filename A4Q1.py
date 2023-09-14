import random

a=int(input("power:"))
x=[]
for i in range(random.randint(1,10)):
    x.append(random.randint(0, 25))
print(x)
print([i**a for i in x])