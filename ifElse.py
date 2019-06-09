a=5
b=6
c=10
d=9
if a<b and c<d:
    print("5 is less than 6")
elif a<b and c>d:
    print("Either one condition is true")
else:
    print("No condition satisfied")

print("A is lesser") if a<b else print("B is greater") if b>a else print("False")
if a<b:print("A is smaller")