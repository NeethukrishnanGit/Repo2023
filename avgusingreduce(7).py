from functools import reduce

def avg(list):
    return reduce(lambda a,b:a+b,list)/n

list=[1,2,3,4,5,6,7,8,9]
n=len(list)
avg=avg(list)

print("The average of no's are : ",avg)

