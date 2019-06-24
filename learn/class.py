
"""Class basics"""

class Sanjev:
    name="Sanjev"
    age=24
    maritalstatus="Single"

id1=Sanjev()
print(id1.name)
print(id1.age)
print(id1.maritalstatus)

"""__init__"""

class family:
    def __init__(self,name,age):
        self.name=name
        self.age=age

m1=family("Sanjev",24)

print(m1.name)
print(m1.age)

"""Functions with __init__"""

class friends:
    def __init__(kps,name,number):
        kps.name=name
        kps.number=number

kp1=friends("Sakthi", 8695007788)

print(kp1.name)
print(kp1.number)


"""Functions with init 2"""
class Friends:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfriends(self):
        print(self)

f1=Friends("Sanjev",24)

print(f1.name)
