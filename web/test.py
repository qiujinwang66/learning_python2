
import unittest
from selenium import webdriver
import requests
from time import sleep
from tools.HTMLTestRunner import HTMLTestRunner

# https://blog.csdn.net/weixin_45131345/article/details/105374287::q


class TestLogin(unittest.TestCase):
    def setUp(self):
     # 可以找其他网站登录测试
        self.url = "http://127.0.0.1:8888/iwebshop/index.php?controller=systemadmin&action=index"
        # self.url = "http://127.0.0.1:8888/iwebshop/index.php?controller=systemadmin&action=index"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 获取cookie
        self.cookie = self.getcookie()
        # print(self.cookie)

    # 发送requests 请求验证码
    # def getimage(self):
    #     rep = requests.get(
    #         "http://127.0.0.1:8888/iwebshop/index.php?controller=simple&action=getCaptcha&h=30&s=15&w=90")
    #     with open("aa.png", "wb") as file:
    #         file.write(rep.content)
    # 以截图方式获取验证码
    def getimage(self):
        sleep(3)
        self.driver.get_screenshot_as_file("./bb.png")

    def test01(self):
        # 获取登录信息admin是否成功登录
        login_name = self.driver.find_element_by_css_selector("#header > p > span > label:nth-child(1)").text
        # 截图保留下证据
        self.driver.get_screenshot_as_file("adminlogin.png")
        self.assertEqual(login_name, "admin", "admin没有成功登录")

    def getcookie(self):
        self.getimage()
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_name("admin_name").send_keys("admin")
        driver.find_element_by_css_selector("input[name='password']").send_keys("123456")
        sleep(10)
        driver.find_element_by_xpath("//input[contains(@value,'登录')]").click()

        return driver.get_cookies()

    def tearDown(self):
        sleep(10)
        self.driver.close()