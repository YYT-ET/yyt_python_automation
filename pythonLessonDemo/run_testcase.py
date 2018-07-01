from pythonLessonDemo.mail_login import Testcase
import unittest,time
from pythonLessonDemo.HTMLTestRunner_PY3 import HTMLTestRunner
from selenium import webdriver
'''流程：
1.写好textcase,testsuice
2.增加case到testsuite
3.TextTestRunner运行'''
#1
testcase = unittest.TestSuite() #创建一个testsuite的实例化对象

'''第一种方法:addTest 参数：（类名称（'测试方法的名称'））'''
# testcase.addTest(Testcase('testcase1'))
# testcase.addTest([Testcase('testcase1'),Testcase('testcase2')])
'''第二种方法addtest+TestLoader
            loadTestsFromTestCase:参数（传入类的名称）
            loadTestsFromName:参数 （模块名称.类名）
            loadTests'''
#2
# testcase.addTest(unittest.TestLoader().loadTestsFromTestCase(Testcase))
testcase.addTest(unittest.TestLoader().loadTestsFromName('mail_login.Testcase'))
#3
# unittest.TextTestRunner().run(testcase) #TextTestRunner运行

'''导入测试报告
1.写好textcase,testsuite
2.增加case到testsuite
3.运行HTML_TestRunner'''

now = time.strftime('%Y-%m-%d-%H-%M',time.localtime())
dir = 'C:/Users/ET/Desktop/TEST/'+now+'test.html' #导出的存放路径
file = open(dir,'wb')
runner = HTMLTestRunner(stream=file,title='自动化测试报告')
runner.run(testcase)

driver = webdriver.Chrome()
driver.get('C:\Users\ET\Desktop\TEST\2018-06-02-16-58test.html')
