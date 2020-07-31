### python 基础教程

1. new的作用,如果没有继承object ,同时重写init new ,只会运行new
2. new的作用,继承object,要 `return object.__new__(cls)`
3. 实例名() 会调用__call__方法// 类名()()
4. python 类本质上是type类型`<class '__main__.Person'>`
5. 动态创建一个类:
    ```
    def __init__(self,name):
        self.name = name
    Dog = type('Dog',(object,),{'role':'dog','__init__':__init__})
    d = Dog('xxx')
    print(d)
    print(d.name)
    
    <__main__.Dog object at 0x101152400>
    xxx
    ```
6. traceroute www.baidu.com 解析经过哪些路由---这个是网络层的东西,icmp
7. ping www.baidu.com
8. from import 这个是导入自己的类
9. import 只是引用
10. yield 生成器,只是返回一个生成器.并没与返回所有的实例
    ```python
    # 这个是没有生成迭代器的
    # num_list = [x for x in range(100)]
    # print(num_list)
    
    #()是生成器
    # num_list = (x for x in range(100))
    # print(num_list)
    
    
    #这里也是一个生成器
    def get_nums(sz):
        for x in range(sz):
            yield x
    
    ```
    
11. __name__ == '__main__'
12. generator生成器,调用 next 方法,节约资源,调用的时候才会生成
13. 协程 就是微线程(用户线程),弥补线程的缺失;
14. < 表示输入 > 表示输出
15. super() 可以调用父类的方法 `super.__init__(handler)`
16. 如果想使用更好层级的方法,使用类名来调用 `Parser.__init__(self, handler)`

    ```python
    class Grandparent(object):
        def my_method(self):
            print("Grandparent")
    
    class Parent(Grandparent):
        def my_method(self):
            print("Parent")
    
    class Child(Parent):
        def my_method(self):
            print("Hello Grandparent")
            Grandparent.my_method(self)
    ```
17. super()是一个函数
18. cls 是type类型,self 是cls的一个实例
19. a = b[::]# 这个是浅复试,只是一个指针
20. 深复制 a = deepcopy()来复制
