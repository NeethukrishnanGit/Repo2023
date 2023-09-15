def calc(a, b, c="+"):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    else:
        return False

a= int(input("1st int:"))
b=int(input("2nd int:"))
c=input("symbol:")
print(calc(a,b,c))