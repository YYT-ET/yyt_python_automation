'''
函数
def 函数名（参数）
'''
# print(abs(10))  #求绝对值
# def def_my(x):
#     if x>0:
#         return x;
#     else:
#         return -x;
#
# a=def_my(10)
# print(a)

from selenium import webdriver
import time
# url='http://www.kuaidi100.com/'
# driver=webdriver.Chrome()
# driver.get(url)
# #等待3秒
# time.sleep(3)
# #执行javastrip的方法
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# driver.find_element_by_xpath('//*[@id="welcome"]/a[2]').click()
# # 输入用户名
# driver.find_element_by_xpath('//*[@id="name"]').send_keys('15902127953')
# #输入密码
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('test123456')
# #点击登陆
# driver.find_element_by_xpath('//*[@id="submit"]').click()

def def_login(url,name,password):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    # 执行javascript的方法
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #点击进入登陆界面
    driver.find_element_by_xpath('//*[@id="welcome"]/a[2]').click()
    # 输入用户名
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    # 点击登陆
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    #找用户名
    username=driver.find_element_by_xpath('//*[@id="userName"]').text
    return username


def testcase1():
    a = 'http://www.kuaidi100.com/'
    b = '15902127953'
    c = 'test123456'
    print(def_login(a, b, c))






