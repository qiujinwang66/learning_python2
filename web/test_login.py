from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

# https://www.cnblogs.com/luozhongming/p/13586985.html

class login_test(unittest.TestCase):
    def setup(self):
        print("环境初始化")
    def testcase_login(self):
        driver = webdriver.Chrome()
        driver.set_window_position(25, 45)
        driver.set_window_size(1200, 800)
        driver.get("http://10.96.94.211:3000/index.html#/")
        driver.find_element_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/label[2]/span/input').clear()
        driver.find_element_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/label[2]/span/input').send_keys(
            'XXXXXXX')
        driver.find_element_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/label[3]/span/input').clear()
        driver.find_element_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/label[3]/span/input').send_keys(
            '*****')  # password
        driver.find_element_by_id('login').click()
        time.sleep(3)#登录做一个sleep等待
        print("登录结束")
        driver.quit()
if __name__ == '__main__':
        print("----------运营Web端自动化测试开始执行---------- ")
        suite = unittest.TestSuite()  # 构造测试集
        suite.addTest(login_test('testcase_login'))
        # 定义自动化报告目录
        filename = r"C:\Users\XX\Desktop\Python\Web-Test\report\report.html"
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
                stream=fp,
                title=u'运营Web端系统自动化测试报告',
                description=u'登录测试'
         )
        runner.run(suite)
        fp.close()