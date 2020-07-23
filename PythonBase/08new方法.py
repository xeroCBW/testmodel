class Brand:
    def __init__(self,name):

        print('__init__')
        self.name = name


    def __new__(cls, *args, **kwargs):
        print('__new__')
        print(cls,args,kwargs)



# b = Brand('cbw')



class Brand2(object):
    def __init__(self,name):

        self.name = name
        print('__init__')


    def __new__(cls, *args, **kwargs):
        print('__new__')
        print(cls,args,kwargs)
        return object.__new__(cls)



b2 = Brand2('cbw')
