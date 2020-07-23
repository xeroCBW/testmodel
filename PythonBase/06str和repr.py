class Brand:

    def __init__(self,name):
        print('创建对象')
        self.name = name

    def __str__(self):
        return self.name

    def __del__(self):
        print('对象被释放掉了')


b = Brand('cbw')

print(b)
print(b)


# 创建对象
# cbw
# cbw
# 对象被释放掉了