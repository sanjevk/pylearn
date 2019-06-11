add=lambda a,b: a+b
sub=lambda a,b: a-b
multiply=lambda a,b: a*b
div=lambda  a,b: a/b

choice=input("Enter your choice of operation: ")
x=int(input("First value: "))
y=int(input("Second value: "))
if choice=="add":
    print(add(x,y))
