'''
pythond s输入输出
数据类型
str,list,根据索引取值，len(),type()
python运算，循环，while,for,条件判断if
写一个完整的自动化用例
'''


str1,str2='python','automation';str3='10'
int1=100;int2=10
float1=10.6;float2=2.0
list1=[1,2,3,4];list2=['java','python','php']
dict1={'zhangsan':'18'}
tuble=('1','1')
testList = {'hello', 'world', 'java', 'automaton'}

'''
python的运算，表达式的语法是直接的；+ - * / % >= <= != 
'''
# print(5*3-10+2)
# print(str1+','+str2)#字符串相加
# print(int(str3)+int1)#强转成int类型和int1相加

#乘法
# print(str1*3)
# print(2**7)#2的7次方
#
# #除法
# print(type(10/5),10/5)
# print(10//4)#//只取整数
# print(10%2)#%取余数
# print(-16//10)

'''
切片， 
[]:包含开始，排除结束
'''
print(str1[2:4])
print(str1[2:3])
print(str1[3:])
print(str1[:3]+str1[-1:])#-1：取最后一个树

print(str1[:3]+str1[3:])

#大写
print (str1.upper())
#把python首字母大写,用upper方法，切片
print((str1[:1]).upper()+(str1[1:]))

'''
循环:while,for
布尔类型：非真即假:true,false
while条件为真，不断循环，break跳出循环
1.一切非0整数都是为真，0为假
2.一切长度不为0的东西为true;长度为0：空序列 为假
3.条件表达式3！=3
'''
strnu1=''
print(bool(strnu1))
print(bool(3>0))

'''
计算[1,100]1+2+...+100
'''
a=1;sum1=0;
while a<=100:
    sum1=sum1+a;
    a=a+1;
print(sum1)

#100加到1
b=100;sum2=0;
while b>0:
    sum2=sum2+b;
    b=b-1;
print(sum2)
# from selenium import webdriver
# N的阶乘n!=n*(n-1)*(n-2)
c=10;jiecheng=1;
while c>0:
    jiecheng=jiecheng*c;
    c=c-1;
print(jiecheng)

'''
for循环'''
list1={'java','python','node'}
for temp in list1:
    print(temp)

list2={'java','python','node'}
for temp in list2:
    print(temp,end=' ')

# for i in range(1,100):
#     print(i)
#     sum=sum+i
#     print(sum)

'''
for in 和for in range的区别
for in 循环list的元素
for in range 循环list的下标
'''
list3={'java','python','node'}
for temp in list3:
    for j in temp:
        print('j:'+j)

'''
条件判断'''
# grage=int(input('请输入你的成绩:'))
# print(type(grage))

# if grage>=60:
#     print('合格')
# else:
#     print('差')

import  random
# 随机数
i =random.randint(1,100)
print('随机数：',i)
if i>95:
    print('A')
else:
    if i>=80:
       print('B')
    else:
        if i>=70:
            print('C')
        else:
            if i>=60:
                print('D')
            else:
                print('bad')

if i>95:
    print('A')
elif i>85:
    print('B')
elif i>75:
    print('C')
elif i>60:
    print('D')
else:
    print('F')


for temp in testList:
    #取余判断奇数
    s = len(temp) % 2
    a = len(temp) // 2
    if s == 1:
        # 拼接字符串
        temp = temp[:a] + temp[a:a + 1].upper() + temp[a+1:]
        print(temp)
    else:
        print(temp)


















