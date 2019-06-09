"""List"""

Names = ["Sanjev","Saravanan","Ashok"]
for x in Names:
    print(x)
Names[1]="Ashok"
Names[2]="Saravanan"

for x in Names:
    print(x)

print(Names[0])

if "Sanjev" in Names:
    print("Yes, Sanjev is in the list")

print(len(Names))
Names.append("Kathiravan")
print(Names)
Names.remove("Kathiravan")
print(Names)
Names.insert(0,"Kathiravan")
print(Names)

Names.remove("Sanjev")
print(Names)
Names.pop()
print(Names)
Names.append("Saravanan")
print(Names)
del Names[0]
print(Names)
Names.append("Kathiravan")
print(Names)

MyNames=Names.copy()
print(MyNames)

MyNames.clear()
MyNames = ["Kanax", "Sampoornam","Ramya","Gokul","Senthu","Yugan","Sanjev"]
print(MyNames)

MyNames.sort(reverse=False)
print(MyNames)

print(Names.count("Sanjev"))
print(MyNames.count("Sanjev"))

print(MyNames)
MyNames = reversed(MyNames)

"""Tuples"""

NameT=("Sanjev","Ramya","Gokul")
print(NameT)
for x in NameT:
    print(x)

print(NameT.count("Sanjev"))

NameTuple=tuple(NameT)
print(NameTuple)

print(NameTuple[1])

if "Sanjev" in NameTuple:
    print("Yes")


"""Sets"""
setA = {"Sanjev","Ramya","Gokul","Ram"}
setB = {"Kanax","Sambu","Gopal","Devi","Senthu","Yugan"}
setC = {"Senthu","Yugan","Gokul","Ramya"}

setA.add("Gayathri")
setB.update(["PostalMan","PostalWoman"])
print(setB)
print(setA)
print(setC)
print(len(setA))
for x in setA:
    print(x)

setD=setB.copy()
print(setD)
setX=setA.difference()
print(setX)
setY=setA.intersection(setB)
print(setY)
setM=setA.isdisjoint(setB)
print(setM)

setH=setA.symmetric_difference(setB)
print(setH)