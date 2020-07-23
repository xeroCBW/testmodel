class Brand:
    def __call__(self, *args, **kwargs):

        print('__call__')



b = Brand()
print(b)
# b() 加上()就会执行  实例名()
