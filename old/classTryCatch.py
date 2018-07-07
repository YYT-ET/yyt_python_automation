
try:
    a=1/0
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('None')
finally:
    print('must be except')
print('-----------------------------')
#打开文件
#r=读
try:
    fp=open('data/aa.txt','r+')
    fp.write('hello word')
except IOError:
    print('IO error')
finally:
    try:
        fp.close()
        print('file is closed')
    except NameError:
        print('Name Error!')
print('-----------------------------')
try:
    a=open('test','r')
    a.write('hello')
except IOError:
    print('IO error')
finally:
    a.close()
    print('closed')
print('-----------------------------')
try:
    a = input('input a num.')
    c=int(a)#强制类型转换
    if c==2:
        b=c/0
except ValueError:
    print('输入错误')
except ZeroDivisionError:
    print('分母不能为零')
finally:
    print('执行完成')
print('-----------------------------')

try:
    fp=open('aa',"r")
    fp.write('666')
    a=input('input a num.')
    c=int(a)
    if c==2:
        b=c/0
except ValueError:
    print('输入错误')
except ZeroDivisionError:
    print('分母不能为零')
except:
    print('异常')
finally:
    print('执行完毕')
print('-----------------------------')
#直接抛异常


