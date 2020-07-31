# -*- coding: utf-8 -*-
# @Time    : 2020-7-8 21:01
# @Author  : liangxiaopeng
# @File    : case_99_cheng.py

'''
九九乘法表
'''
for i in range(1,10):
    print(\
        )
    for j in range(1,i+1):
        print("%s x %s = %s \t "%(i,j,i*j),end='')
###打印大写字母和小写字母
print()
for i in range(65,91):
    print(chr(i),end='')
print()

print(''.join(chr(i) for i in range(97,123)))

###1-100数相加的和
print()
sum = 0

for i in range(1,101):
    sum+=i

print(sum)
###1-100数相加的和
print((1+100)*50)

###第二个列表中的每个数，比第一个列表中的每个数大一
list = list(range(0,10))
list1 = []
print(list)
for i in list:

    i +=1
    list1.append(i)

print(list1)
print([i+1 for i in list])
###将字符串中的数字去掉
s = '123467890rtyjkjljdlfj12032423sdfsd'
m = []
for i in s:
    if i not in '0123456789':
        m.append(i)
print(''.join(m))

##斐波那契数
def fib(n):
    result = []
    if n <= 0 or not isinstance(n,int):
        return result

    else:
        for i in range(n):
            if i < 2:
                result.append(1)
            else:
                result.append(result[i-1]+result[i-2])

    del list[0]
    print(result)

fib(15)

###
list = [0,1,1,0,1,1,0,1,1,1,0,0]
l2 = []
for i in list:
    if i == 1:
        l2.append(i)

for i in list:
    if i == 0:
        l2.append(i)

print(l2)
###



