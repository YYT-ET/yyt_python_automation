'''
文件操作 txt文件
open方法 打开一个txt文件，如果没有该文件，w会自动创建
w:写模式
r:读取模式
a:追加模式
b:二进制模式
r+:读/写
w+:读/写
'''
# -*- coding: utf-8 -*-
file = open('0519.txt','w+')
print(file.mode)#查看文件的读取模式mode
file.write('hell\nman')
print(file.closed)#closed查看是否关闭状态
'''read前，先close,再打开'''
file = open('0519.txt','r')
print(file.read())
file.closed

'''追加模式'''
file = open('0519.txt','a')
file.write('\nThree')
file.write('\nFour')
file.write('\n五')
file = open('0519.txt','r')
print(file.read())
# print(file.read())

file = open('D:/自动化相关/0519.txt','w+')
print(file.mode)#查看文件的读取模式mode
file.write('新建文件')
print(file.readline())
file.closed
# file = open('0519.txt','a')
# file.write('\ntwo')


'''with，会自动关闭该文件'''
with open('D:/自动化相关/0519.txt','a+') as f:
    f.write('第二行')
print(f.closed)

'''execel
xlwt:写入excel表格
xlrd:读取excel
'''

from xlwt import Workbook

# excel = Workbook()#新建一个excel表格
# sheet = excel.add_sheet('sheet1') #创建一个sheet
# sheet.write(0,0,'username')#写入数据
# excel.save('0519.xlsx')
#
# list=['username','psw','phone']
# #新建一个excle表格
# sheet2 = excel.add_sheet('sheet2')
# for i in range(len(list)):
#     sheet2.write(0,i,list[i])#写入数据0代表第一行
# excel.save('0519.xlsx')

'''将list中的值写入第一列'''
# list=['username','psw','phone']
# excel = Workbook()
# sheet = excel.add_sheet('test')
# for i in range(len(list)):
#     sheet.write(i,0,list[i])
# excel.save('0519.xls')

'''xlrd'''
import xlrd
excel = xlrd.open_workbook('0519.xls')#打开一个excel文件
print(excel.sheet_by_index(0).name)#打开一个sheet
sheet = excel.sheet_by_index(0)
print(sheet.row_values(0))   #获取行的数据
print(sheet.col_values(0,1,2))#获取列的数据

'''xlut'''