from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


class MyTestCase(unittest.TestCase):
    def setup(self):
        # 可以找其他网站登录测试
        self.url = "http://10.96.94.211:3000/index.html#/"
        # self.url = "http://10.96.94.211:3000/index.html#/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 获取cookie
        # self.cookie = self.getcookie()
        # print(self.cookie)


    def tearDown(self):
        sleep(10)
        self.driver.close()