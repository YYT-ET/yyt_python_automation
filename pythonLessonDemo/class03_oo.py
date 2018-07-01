'''
面向对象编程
类(class):抽象的，具有相同属性和方法（功能）的对象的集合
实例（instan）:根据类创建出来的具体的对象
实例化：创建一个类的实例化对象，类似于函数的调用
如何组织用例，运行用例，获得测试报告，unittest
'''

#class +类名
#创建一个员工类
# class Employee:
#     pass #占位符 什么都不会做
#
# #新建类的实例化对象
# emp1 = Employee()
# emp2 = Employee()
#
# emp1.name = 'zhangsan'
# emp1.age = '20'
# emp2.name = 'lisi'
# emp2.age = '28'
# print(emp1.name,emp1.age)

'''
类的第一个字母大写
类方法：类中定义的函数，第一个参数永远是self
init方法：
1.第一个参数永远是self
2.每次新建一个类的实例化对象的时候，会自动调用这个init方法
3.在init方法内部，可以将对象相同的属性绑定在self上
'''

#理解self
class Test:
    def diaplayself(self):
        print(self)

A = Test()
A.diaplayself()
print(A)


#理解init方法
#可以＋objecct，只写object表示没有继承什么类
#class Employee2(object):
class Employee2:
    '''定义一个员工的公共变量'''
    empcount = 0
    def __init__(self,name,age,year):
        self.name = name
        self.age = age
        self.year = int(year)
        #类里的这个empcount变量
        Employee2.empcount += 1
    '''打印员工基本信息的方法'''
    def display_info(self):
        print('员工%s,年龄是%s'%(self.name,self.age))
    '''统计员工人数，查看员工的基本信息'''
    def empcoutTest(self):
        '''统计员工的人数'''
        print('员工的总人数为%d'%Employee2.empcount)
    def rank(self):
        '''评定员工的等级'''
        if self.year > 10:
            print('员工%s等级为A'%(self.name))
        elif self.year > 5:
            print('员工%s等级为B' % (self.name))
        elif self.year > 2:
            print('员工%s等级为C' % (self.name))
        elif self.year > 1:
            print('员工%s等级为D' % (self.name))
        else:
            print('员工%s等级为F' % (self.name))


#实例化对像想员工3
# emp1 = Employee2('双双','19')
# emp2 = Employee2('张三','18')
# emp3 = Employee2('emp3.name','emp3.age')
emp4 = Employee2('yiyi','13','6')
emp5 = Employee2('小二','13','3')
emp5.rank()
emp4.rank()
# print(emp3.name,emp3.age)
# emp2.display_info()
# emp3.empcoutTest()

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# dog1 = Dog('哈士奇','7')
# print(dog1.name,dog1.age)


'''
继承：代码的重用'''


class Parent(object): #定义一个父类
    def __init__(self):
        print('这是父类的init方法') #在继承后父类的init方法不会被调用
    def parentMethon(self):
        print('这是父类的普通方法')

class Child(Parent): #定义一个子类
    def __init__(self):
        print('子类的init方法')
    def childMethon(self):
        print('子类的方法')

#实例化一个对象
child1 = Child()
#调用父类的方法
child1.parentMethon()



