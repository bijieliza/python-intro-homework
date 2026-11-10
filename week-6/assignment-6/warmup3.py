def set_name():
    name = "Priya"
set_name()
#Uncommenting the line below causes a NameError
#print(name)
#NameError: name 'name' is not defined
def set_name():
    name = "Priya"
    return name
name=set_name()
print(name)