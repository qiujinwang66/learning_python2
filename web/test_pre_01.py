import unittest
from selenium import webdriver

class pre_test(unittest.TestCase):
    def setUp(self):
        print("这是pre------")
        self.url = "http://100.90.138.36:8083/"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待30秒
        self.driver.get(self.url)