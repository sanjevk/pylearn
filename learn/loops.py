i=1
while i<=10:
    print(i)
    if i==6:
        break
    i+=1

"""FOR LOOPS"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
else:
    print("Loop finished")

c=int(1.5)
for a in range(2,10,c):
    print(a)