# num_list = [x for x in range(100)]
# print(num_list)

# num_list_1 = (x for x in range(100))
# <generator object <genexpr> at 0x10fce0780> 这里生成了一个迭代器
# 迭代器会调用next 方法
# print(num_list_1)
# for x in num_list_1:
#     print(x)


def get_nums(sz):
    for x in range(sz):
        yield x

# 这里也是返回一个生成器
# 会不断调用next
# print(get_nums(100))
# for x in get_nums(100):
#     print(x)

def test01():
    t = get_nums(10)
    print(t)
    for x in t:
        print(x)

def test02():

    a = get_nums(10)

    for _ in range(10):
        print(next(a))



def get_num2(n):
    for i in range(n):
        # 这里只是一个生成器,直接回返回None 啥也没有
        t = yield i
        print(t)

def test03():

    a = get_num2(10)

    for _ in range(10):

        print(next(a))

def get_num3(n):
    yield from range(n)

def test04():

    print(list(get_num3(10)))


def test05():
    '''
    test4 和 test05 效果一样.主要是避免语法显得复杂
    :return:
    '''
    a = get_nums(10)
    for _ in range(10):
        print(next(a))

def test06():


    direction = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
    ]

    for _ in range(10):
        for d in direction:
            print(d)


def test07():
    q = 10
    print([]+[q])

def test08():

    a = [
        [1,2,3],
        [4,5,6]
    ]

    print(a)

    sum(a)

def test09():
    a = [1,2,3,4]
    print(a.index(1))

def test10():

    ans = [[1,2],[1,3],[1,9],[3,7]]

    # res = sorted(ans,lambda key:)


if __name__ == '__main__':

    # test01()

    # test02()

    # test03()

    # test04()

    # test05()

    # test06()

    # test07()

    # test08()
    test09()
    pass





