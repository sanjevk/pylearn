def sanjev_Function():
    print("This is Sanjev's function")


sanjev_Function()

"""Function to add to dictionary"""


def add_dict(uname, uid, age):
    mydict = {"Name": uname, "ID": uid, "Age": age}
    print(mydict)


add_dict("Sanjev", "8888", "25")
add_dict("Ashok","8889","25")

"""Default parameter"""

def default_Val(regn="8888"):
    print(regn)

default_Val("8889")
default_Val()
default_Val("8887")

"""Parameter data types inside functions"""
"""List type parameter"""

def list_Function(names):
    for x in names:
        print(x)

Name_List={"Sanjev","Ashok","Saravanan"}

list_Function(Name_List)


"""Dictionary type parameter"""

def dict_Function(naming):
    for x in naming.values():
        print(x)

Name_Dict={"Name":"Sanjev","Age":"24"}

dict_Function(Name_Dict)

"""Return statement uses"""
def mother(a):
    return a*99

print(mother(5))
b=mother(19)
print(b)


