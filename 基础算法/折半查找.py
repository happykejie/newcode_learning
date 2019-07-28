# -*- coding: UTF-8 -*-
def binaryfind(A,m):
    if len(A) == 0:
        return  -1
    i = int(len(A)/2)
    print(A[i])
    if A[i] == m:
        return  i
    if A[i] >m and i-1>=0:
        return binaryfind(A[0:i-1],m)
    if A[i]<m and i+1 <len(A):
        return  binaryfind(A[i+1:len(A)],m)
    return  -1

A = [3,1,5,6,7,4,2,8]
A.sort()
M=9

success = False
for i in range(len(A)):
    m = M-A[i]
    j = binaryfind(A,m)
    if j != -1 and j != 1:
        print ("存在i和j使得A[i]+A[j]={0}".format(M))
        success = True
        break
    if success != True:
        print ("不存在i和j使得A[i]+A[j]={0}".format(M))


result = binaryfind(A,8)
print  result

