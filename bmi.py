# -*- coding: utf-8 -*-

name = input ('please input your name:')
a = input('please input your height in cm:')
b = input('please input your weight in kg:')
height = int(a)
weight = int (b)
bmi = weight/height/height*10000
print ('son of a bitch', name, 'your height is %s cm your weight is %s kg and your bmi is %.2f' %(a,b,bmi))
if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')