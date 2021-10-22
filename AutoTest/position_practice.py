import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def alert():
    result = EC.alert_is_present()(driver)
    if result:
        result.accept()
driver = webdriver.Chrome()
driver.get("http://219.218.18.106:8081/RunningService/login.do")
action = ActionChains(driver)
driver.find_element(By.NAME,"userAccount").clear()
driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"userAccount").send_keys("aaa")
driver.find_element(By.NAME,"password").send_keys("12345678")
driver.find_element(By.NAME,"password").submit()
liebiao = driver.find_element(By.XPATH,'//*[@id="menu-list"]/ul/li[9]/a')
action.move_to_element(liebiao).perform()
driver.find_element(By.XPATH,'//*[@id="menu-list"]/ul/li[9]/ul/li[2]/a').click()
nr = driver.find_element(By.ID,'tid')
select = Select(nr)
select.select_by_value('3')
time.sleep(1)
tijiao = driver.find_element(By.ID,'updateUser')
action.move_to_element(tijiao).click().perform()
time.sleep(2)
alert()
time.sleep(1)
driver.close()

# driver.find_element("id","kw").send_keys("4399")
# driver.find_element("id","su").click()
# time.sleep(1)
#
# first=driver.find_elements(By.CSS_SELECTOR,r"#\31  > h3 > a")[0]
# driver.execute_script("arguments[0].removeAttribute('target')",first)
# driver.execute_script("window.scrollTo(0,400)")
# ActionChains(driver).move_to_element(first).click().perform() ##链式写法
# ###行为事件是存储在actionchains对象队列。当你使用perform()，事件按顺序执行。
# #driver.execute_script("window.scrollTo(0,400)")
# ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# driver.close()




# driver.get("http://www.baidu.com")
# driver.find_element("id","kw").send_keys("哈哈哈哈")
# driver.find_element("id","su").click()
# time.sleep(1)
#
# first=driver.find_elements(By.CSS_SELECTOR,r"#\31  > h3 > a")[0].click()
# ActionChains(driver).move_to_element(first).click().perform()
#
# time.sleep(1)

