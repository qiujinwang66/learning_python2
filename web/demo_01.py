from selenium import webdriver
import unittest
import time

class login1Test(unittest.TestCase):
    def setUp(self):
        self.url='http://test1.xgs.xiaoshushidai.com'
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)#隐性等待30秒
        self.driver.get(self.url)

    def login(self,username,passwrod,txtVerify):
        self.driver.find_element_by_id('txtUserName').send_keys(username)
        self.driver.find_element_by_id('txtPassword').send_keys(passwrod)
        self.driver.find_element_by_id('txtVerify').send_keys(txtVerify)
        self.driver.find_element_by_id('btnSubmit').click()

    def tearDown(self):
        self.driver.quit()
# 带验证码登陆成功
    def test_loginsSuccess(self):
        self.login("T_mac",'Aa654321','123')
        tip=self.driver.find_element_by_class_name('info').text
        print(tip)
        self.assertEqual(tip,'您好，T_mac''\n''测试删除')
# 用户名为空
    def test_nulluser(self):
        self.login('','','')
        self.driver.switch_to.alert().accept()
        nullusererror=self.driver.switch_to.alert().text
        self.assertEqual(nullusererror,'请输入管理员账号')
# 密码为空
    def test_nullpwd(self):
        self.login('13620180611','','')
        self.driver.switch_to.alert().accept()
        nullpassword=self.driver.switch_to.alert().text
        self.assertEqual(nullpassword,'请输入管理员密码')
# 验证码为空
    def test_nulltxtVerify(self):
        self.login('13620180611','Aa654321','')
        self.driver.switch_to.alert().accept()
        nulltxtVerify=self.driver.switch_to.alert().text
        self.assertEqual(nulltxtVerify,'请输入验证码')

if __name__=='__main__':
unittest.main()