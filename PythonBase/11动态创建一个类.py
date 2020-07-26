class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('cbw',12)

print(type(p))
print(type(Person))


# <__main__.Dog object at 0x106661390>
# dog

def __init__(self,name):
    self.name = name
Dog = type('Dog',(object,),{'role':'dog','__init__':__init__})
d = Dog('xxx')
print(d)
print(d.name)
