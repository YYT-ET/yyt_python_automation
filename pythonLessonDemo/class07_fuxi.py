'''
selenium:
webelement.is_display
webelement.text
webelement.get_attribute('href') #获取属性

javascript:
window:
window.open(url)
window.scrollTo(0,10000)#滚动条滑动
location:
location.href()
location.reload
location.assgin()

document:
document.getElementsByTagName('input')[0].value='123'
document.getElementsById('vip').style.visibility='hidden'

邮件发送：email,smtplib
1.构建数据
2.构建邮件内容
3.发送
'''
from selenium import webdriver
# from selenium.webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.zzu.edu.cn/')
# driver.switch_to.frame('zzu_top_6')
# ActionDriver.driver.find_element_by_xpath('').perform()
# driver.find_element_by_xpath('').click()

def homework(x,y,oper):
    if oper=='//':
        if x>y>0:
            return (x//y)
        else:
            return -(x-y)//abs(y)
    elif oper=='%':
        if x%y>0:
            return x%y
        else:
            sum=abs(x)-(abs(y)*abs(x-y)//abs(y))
            if sum*y>0:
                return sum
            else:
                return -sum

    else:
        print('运算符有误')


driver=webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
js="alert(document.getElementById('VIP').style.visibility)"
driver.execute_script(js)
value=driver.execute_script(js)
print(value)
