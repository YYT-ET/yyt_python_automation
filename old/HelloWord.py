#coding=utf-8
#hello word

import keyword
print(keyword.kwlist)

print('hello word!')
print('hello','Python!')
print(500)
if True:
    print('Ture')
    print("ture")
else:
    print('False')

'''
firstNumber = 5 ; secondNumber = 6 ;
print(firstNumber + secondNumber)
print("占位符，%d" %firstNumber)

con = input("please input Content")
print("the input Content is %r"%con)
'''

f = 5.20
l = 5.30
a = f + l
print(a)

print("Let's go.")
print('Let\'s go.')
print('This is "Python"')
print("""Congratulation
to 
you""")

print("hello \n换行")
print('c:\\路径需要双斜杠来转义')

t = True
f = False
print(t and f)
print(t or f)

student = ['Li','Zhang','Yan']
print(student)
print(student[0])
print(student[1])
print(student[-1])
print('\n')
#末尾添加元素
student.append('添加学生一')
print(student)
#insert指定位置添加元素
student.insert(0,'第一个位置添加')
print(student)
#修改元素
student[0] = 'No.1'
print(student)
#pop删除末尾元素
student.pop()
print(student)
#指定删除元素
student.pop(0)
print(student)
print('\n')

course = ('Chinese','Math','English','Computer')
print(course)
print(course[3])
print(course[1:3])
print(course[1:])

score = (78,89,94,56)
print(len(score))
maxScore = max(score)
print(maxScore)
print(min(score))
