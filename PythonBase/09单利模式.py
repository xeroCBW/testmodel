class Sigleton(object):
    instance = None


    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            obj = object.__new__(cls)
            cls.instance = obj
        return cls.instance

s = Sigleton()
s1 = Sigleton()
s2 = Sigleton()

# 返回的是同一个对象
# <__main__.Sigleton object at 0x104e7a128>
# <__main__.Sigleton object at 0x104e7a128>
# <__main__.Sigleton object at 0x104e7a128>

print(s)
print(s1)
print(s2)