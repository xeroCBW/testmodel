import copy

def test01():
    '''
    深复制,不会改变数据,全部复制值
    :return:
    '''
    a = [1,2,3]
    b = a[::]
    b[0] = 100

    print(a)
    print(b)


    # [1, 2, 3]
    # [100, 2, 3]

def test02():
    '''
    浅复制,会改变数据,复制引用
    :return:
    '''
    a = [1, 2, 3]
    b = a[::]
    b[0] = 100

    c = a
    c[0] = 100

    print(a)
    print(b)

    print(c)

    # [100, 2, 3]
    # [100, 2, 3]
    # [100, 2, 3]


def test03():
    a = [1,2,[3,4]]
    b = a[::]
    c = copy.deepcopy(a)

    print(a)
    print(b)
    print(c)

    # [1, 2, [3, 4]]
    # [1, 2, [3, 4]]
    # [1, 2, [3, 4]]


def test04():
    a = [1, 2, [3, 4]]
    b = a[::]
    c = copy.deepcopy(a)

    b[2][1] = 100
    c[2][1] = 100

    print(a)
    print(b)
    print(c)

    # [1, 2, [3, 4]]
    # [1, 2, [3, 4]]
    # [1, 2, [3, 100]]

    # 深层次复制还是要用 copy ,[::]只能复制一层
    # [1, 2, [3, 100]]
    # [1, 2, [3, 100]]
    # [1, 2, [3, 100]]

if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    test04()
    pass



