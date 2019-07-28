# -*- coding: UTF-8 -*-
def cat():
    msg = '我是一只hello kitty'
    while True:
        food = yield msg
        if food == '鱼肉':
            msg = '好开心'
        else:
            msg = '不开心，人家要吃鱼啦'

# miao = cat()
# print(miao.next())
# print(miao.send('鱼肉'))
# print(miao.send('鸡肉'))


def cat():
    print('我是一只hello kitty')
    while True:
        food = yield
        if food == '鱼肉':
            yield '好开心'
        else:
            yield '不开心，人家要吃鱼肉啦'

miao = cat()
miao.next()
print(miao.send('鱼肉'))

miao = cat()
print(miao.next())
print(miao.send('鱼肉'))

