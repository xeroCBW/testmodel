# 运算符

a = 10
b = 2
c = a**b

d = c//3


print(c)
print(d)


# 逻辑判断

a = 10
b = 20

if a and b :
    print('a 和 b 都是正数 ')
else:
    print('a and b 条件 不成立')

if a or b :
    print('a b 只要一个成立就可以')
else:
    print('这是条件不成立的情况')

# 成员运算符号--是否在数组中
list3 = [1, 2, 3]

if(1 in list3):
    print('true')
else:
    print('false')

# ==和 ！=

if(a is b):
    print('判断a b 是否相等：true')
else:
    print('判断a b 是否相等：false')

if(a is not b):
    print('a不等于b:true')
else:
    print('a不等于b:false')


