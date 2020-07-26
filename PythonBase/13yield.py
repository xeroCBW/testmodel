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



if __name__ == '__main__':

    t = get_nums(10)
    print(t)
    for x in t:
        print(x)


