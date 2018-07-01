from selenium import webdriver
import xlrd
driver=webdriver.Chrome()
driver.get('http://127.0.0.1:5000/')
#点击进入登陆界面
driver.find_element_by_xpath('/html/body/a').click()
# 输入用户名
driver.find_element_by_xpath('/html/body/form/p[1]/input').send_keys('15921774900')
# 输入密码
driver.find_element_by_xpath('/html/body/form/p[2]/input').send_keys('123456')
# 点击登陆
driver.find_element_by_xpath('/html/body/form/p[3]/button').click()

# excel = xlrd.open_workbook('o519.xls')
# sheet = excel.sheet_by_index(0)

def testCase():
    '''读取excel表的数据，'''
    # username= sheet.col_values(0,1,2)
    # password=sheet.row_values(1,1,2)
    # print(username,password)
    #for
        #login()

