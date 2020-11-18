
from selenium import webdriver
driver = webdriver.Chrome()
# driver.get("http://dpub.didi.cn/")
url = "http://100.90.138.36:8083/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)  # 隐性等待30秒
driver.get(url)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div/div/div[1]/div[1]').click()
# driver.implicitly_wait(29)
# driver.find_element_by_id("username").send_keys('jessewangqiujin_v')
# driver.find_element_by_id("password").send_keys('WTOvgu^631')
# driver.find_element_by_id('submit').click()
# t = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/p[2]')
# print('登陆后会显示：{}'.format(t.text))
