import json

import redis

# 设置decode response 这个设置成为true 就可以
connect = redis.StrictRedis(host='localhost',port=6379,password='19920202qwer',decode_responses=True)


def test01():
    connect.set('hello', '123')
    res = connect.get('hello')
    print(res)


def test02():
    res = connect.keys('*')
    for x in res:
        print(x)


def test03():
    '''
    测试代码
    :return:没有返回值
    '''

    connect.lpush('list_demo',10)
    connect.lpush('list_demo', 11)
    connect.lpush('list_demo', 12)
    connect.lpush('list_demo', 13)
    connect.lpush('list_demo', 14)
    res = connect.lrange('list_demo',0 ,100)
    res = connect.sort('list_demo')
    for x in res:
        print(x)


    connect.lpop()


def test04():

    person = {
        'name':'cbw',
        'age':19
    }

    res = json.dumps(person,ensure_ascii=False)

    # connect.set('person:1',res)
    t =  connect.get('person:1')
    print(t)




    pass

if __name__ == '__main__':
    # test01()
    # test02()
    # test03()

    test04()

