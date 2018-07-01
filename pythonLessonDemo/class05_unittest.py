# conding=utf-8

from selenium import webdriver
import unittest
import time
from pythonLessonDemo.HTMLTestRunner_PY3 import HTMLTestRunner

'''复习：
selenium的基本操作：
刷新：refresh
前进：forword
后退：
获取多少个游览器窗口、切换窗口、关闭、退出、放大、缩小、设置窗口大小值
键盘操作：导入Keys类：TAB ENTER
鼠标操作：Actionchains:
         double_click:双击
         click_and_hole:按住不放
         release:
         drag_and_drop:拖拽
         move_to_elments:移动到
定位元素：id、name、classname、linktext、patialinktext、css、tag_name
xpath:稳定 灵活 万能
      //+标签
      //：相对路径
      @：[@属性名="值"]
      text：[text()="值"]
      /..:上级
      /：下级
      *：标签
      模糊查询：contains::[contaions(@属性名称,'属性值包含了什么')]
      starts-wish:[starts-with(test(),'已什么开始')]
'''
'''课程：
SVG：可伸缩矢量图形：元素定位：//*[name()='svg']
frame:三种标签：'''
# driver = webdriver.Chrome()
# driver.get('http://www.kuaidi100.com/')
# driver.find_element_by_xpath('//*[@id="uDeskTarget"]').click() #联系客服
# #切换到frame,再定位到frame里的元素
# driver.switch_to_frame('//*[@id="udesk_iframe"]')
# driver.find_element_by_xpath('//*[@id="txtMsg"]').send_keys('nihhao') #输入文字
# #退出frame
# driver.switch_to_default_content()

'''unittest:python自带的单元测试框架'''
# print(help(unittest))
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  # test method names begin with 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#
# if __name__ == '__main__':
#     unittest.main()

# class Testcase():
#     def testcase1(self):
#         driver = webdriver.Chrome()
#         driver.get('http://127.0.0.1:5000/')
#         time.sleep(3)
#         driver.find_element_by_xpath('//*[@id="testid"]').click()
#         driver.close()
#         print('case1')
#
#     def testcase2(self):
#         driver = webdriver.Chrome()
#         driver.get('http://127.0.0.1:5000/')
#         driver.find_element_by_xpath('/html/body/a').click()
#         time.sleep(3)
#         driver.close()
#         print('case2')
#
# Testcase().testcase1()
# Testcase().testcase2()

'''unittest'''
class Testcase(unittest.TestCase):
    #每个用例执行前最先执行（其次先）
    # def setUp(self):
    #     print('用例执行前')
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://127.0.0.1:5000/')
    #
    # #最后执行
    # def tearDown(self):
    #     print('执行后清理环境')
    #     self.driver.close()

    #所有用例执行前操作，且只执行一次（最先）
    @classmethod
    def setUpClass(self):
        print('所有用例执行前操作，且只执行一次')
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000/')

    #所有用例执行完之后，最后一步操作
    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print('所有用例执行完之后，最后一步操作')


    def testcase1(self):
        self.driver.find_element_by_xpath('//*[@id="testid"]').click()
        text=self.driver.switch_to.alert().text
        print(text)
        self.driver.switch_to.alert.accept()#点击alert
        self.assertEqual(text,'别点我点登陆啊')

        time.sleep(1)
        print('case1')

    def testcase2(self):
        self.driver.find_element_by_xpath('/html/body/a').click()
        time.sleep(1)
        print('case2')


if __name__ == '__main__':
    print('这是再当前文件运行')
    unittest.main(verbosity=2)









