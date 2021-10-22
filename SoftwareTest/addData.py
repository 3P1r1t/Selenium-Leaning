from time import sleep

from selenium import webdriver
import selenium, unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import csv
from ddt import ddt, data, unpack


def adddata():
    datas = []
    with open('data.CSV') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            datas.append(row)
    return datas


@ddt
class TestForZichan(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.1.251/bsams/front/login.do')
        self.driver.find_element(By.ID, 'taskId').send_keys(35)
        self.driver.find_element(By.ID, 'loginName').send_keys('stu7')
        self.driver.find_element(By.ID, 'password').send_keys('stu7')
        self.driver.find_element(By.ID, 'vericode').send_keys(input(print('请输入验证码')))
        sleep(1)
        self.driver.find_element(By.ID, 'loginName').submit()
        sleep(1)

    def tearDown(self) -> None:
        sleep(5)
        self.driver.quit()

    @data(*adddata())
    @unpack
    def test_01(self, name, code):
        self.driver.find_element(By.LINK_TEXT, '部门管理').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/input').click()
        sleep(2)
        self.driver.find_element(By.ID, 'title').send_keys(name)
        self.driver.find_element(By.ID, 'code').send_keys(code)
        self.driver.find_element(By.LINK_TEXT,'保存').click()
        sleep(1)
        self.driver.switch_to.alert.accept()

if __name__ == '__main__':
    unittest.main()
