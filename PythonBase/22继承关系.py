class A(object):
    def __init__(self):
        print('...A start...')
        print('....A end....')

class B(A):

    def __init__(self):
        print('...B start...')
        super().__init__()
        print('....B end....')


class C(A):
    def __init__(self):
        print('...C start...')
        super().__init__()
        print('....C end....')


class D(B,C):

    def __init__(self):
        print('...D start...')
        super().__init__()
        print('-------------')
        print('....D end....')


def test01():

    '''
    # 继承先后外置
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    ...D start...
    ...B start...
    ...C start...
    ...A start...
    ....A end....
    ....C end....
    ....B end....
    -------------
    ....D end....

    '''
    print(D.__mro__)
    d = D()




if __name__ == '__main__':

    test01()

