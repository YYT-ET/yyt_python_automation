from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
class Testcase(unittest.TestCase):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    @classmethod
    def setUpClass(self):
        print('所有用例执行前操作，且只执行一次')
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        print('打开网页')
        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        print('last')
        time.sleep(1)
        self.driver.close()

    # def setUp(self):
        # self.driver.switch_to.frame('login_frame')  # 直接找frame的id或者名称，或者这个from的路径
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://mail.qq.com/')
    #     print('打开网页')
    #     self.driver.switch_to_frame('login_frame')  # 直接找frame的id
    #     self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
    #
    # def tearDown(self):
        # self.driver.switch_to.default_content()  # 切回主页面
        # self.driver.close()

    def testcase1(self):
        self.driver.switch_to.frame('login_frame')  # 直接找frame的id或者名称，或者这个from的路径
        self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('289157871')
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('Fc1026yyt9034BPH')
        self.driver.find_element_by_xpath('//*[@id="p_low_login_enable"]').click()
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        self.driver.switch_to.default_content()#切回主页面

    def testcase2(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="folder_1"]/b[1]').click()

    # def testcase3(self):
    #     time.sleep(1)
    #     self.driver.switch_to.frame('frm')
    #     name = self.driver.find_element_by_xpath('/html/body/div/form[3]/div[5]/table/tbody/tr/td[3]/table/tbody/tr/td[1]/nobr').text
    #     print(name)
    #     self.driver.switch_to.default_content()  # 切回主页面
    #     # if name =='':



# self.driver.find_element_by_xpath('//*[@id="switcher_qlogin"]').click()

if __name__ =='__main__':
    unittest.main()








#
# name=driver.find_element_by_xpath('//*[@id="div_showyesterday"]/table/tbody/tr/td[3]/table/tbody/tr/td[1]').text
# if name=='95555':
#     driver.find_element_by_xpath('').click()

