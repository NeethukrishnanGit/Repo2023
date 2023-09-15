def circle(radius):
    area=3.14*radius*radius
    print("Area of circle is: ",area)

def rectangle(length,breadth):
    area=length*breadth
    print("Area of rectangle is: ",area)

def square(side):
    area=side*side
    print("Area of square is: ",area)

while True:
    print("1. Area of circle")
    print("2. Area of rectangle")
    print("3. Area of square")
    print("4. Exit")

    choice=int(input("Enter the choice: "))

    if choice==1:
        radius=int(input("Enter the radius: "))
        circle(radius)
    elif choice==2:
        length=int(input("Enter the length: "))
        breadth=int(input("Enter the breadth: "))
        rectangle(length,breadth)
    elif choice==3:
        side=int(input("Enter the side: "))
        square(side)
    elif choice==4:
        break
    else:
        print("Incorrect input")
