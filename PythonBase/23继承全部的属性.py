class Animal(object):
    def __init__(self,eat,drink):
        self.eat = eat
        self.drink = drink

# class Little_Animal(object):
class Little_Animal(Animal):
    # def __init__(self,sleep):
    #     self.sleep = sleep
    def __init__(self,sleep,drink,eat):
        super().__init__(eat,drink)
        self.sleep = sleep


# 继承两个无法调用2 个 init
# 这个时候就要 little 哪里去继承一下

class Dog(Little_Animal):

    def __init__(self,sleep,drink,eat,bark):
       super().__init__(sleep,drink,eat)
       self.bark = bark

    def __str__(self):
        return '%s %s %s %s' %(self.sleep,self.drink,self.eat,self.bark)
    def __repr__(self):
        return '%s %s %s %s' % (self.sleep, self.drink, self.eat, self.bark)

if __name__ == '__main__':
    d = Dog('sleep','drink','eat','bark')
    print(d)
