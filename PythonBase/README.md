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
6. 