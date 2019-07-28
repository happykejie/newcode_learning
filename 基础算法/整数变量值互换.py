# -*- coding: UTF-8 -*-
# 整数变量值互换


a = 1234
b = 5678

print ("binary before swap,a:{0},b{1}".format(bin(a),bin(b)))

a = a ^ b
b = a ^ b
a = a ^ b
print ("binary before swap,a:{0},b{1}".format(bin(a),bin(b)))

# 最低位1清零
x = 5

x = x&(x-1)

print  x

# 获取最低位的1

x = 4

#x = x&!(x-1)
print  x
