import unittest
import requests
from selenium import webdriver

class login_Test(unittest.TestCase):
    def setUp(self):
        print("开始了-------------")
        self.url="http://dpub.didi.cn/"
        self.driver=webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.implicitly_wait(30)#隐性等待30秒
        self.driver.get(self.url)

    def login(self,username,passwrod):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(passwrod)
        self.driver.find_element_by_id('submit').click()

    def tearDown(self):
        self.driver.close()
        print("结束了-------------")
        '''登录成功'''
    def test_loginsSuccess(self):
        self.login('jessewangqiujin_v','WTOvgu^631')
        t = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/p[2]')
        print('登陆成功后会显示：{}'.format(t.text))
        self.assertEqual(t.text, u"我的项目")

if __name__ == "__main__":
    unittest.main()