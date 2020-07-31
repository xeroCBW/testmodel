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
12. 一本生成器,调用 next 方法
13. 协程 就是微线程(用户线程),弥补线程的缺失;
14. < 表示输入 > 表示输出