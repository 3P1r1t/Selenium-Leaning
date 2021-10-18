### Selenium自动化测试

> 环境配置

```` python
driver = webdriver.Chrome("路径") 
driver = webdriver.Chrome()#配置环境变量后
````

>  方法

```` python
driver.title  #标题
assert "xxx" in driver.title #断言使用
````

> 8种定位方式

````python
driver.find_element(By.ID,"id")	#id定位
driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("CLASS") #class定位
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("CSS") #CSS选择器定位
driver.find_element(By.LINK_TEXT,"直播").click() #超文本定位
driver.find_element(By.PARTIAL_LINK_TEXT,"直") #模糊超文本定位
driver.find_element(By.TAG_NAME,"input").click() #<input>标签 唯一
driver.find_element(By.NAME,"wd").send_keys("aaaaaaa") #Name定位
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("aaaaaaa") #XPath定位
-----------------------------------分割线----------------------------------------
driver.find_elements(By.CLASS_NAME,"mnav")[0].click()#复数CLASS定位
search_jq="$('#kw').val('哈哈哈哈')"
driver.execute_script(search_jq)  #使用JQuery定位

````

关于class：

class属性中间的空格并不是空字符串，那是间隔符号，表示的是一个元素多个class的属性名称（class属性是比较特殊的一个，除了这个有多个属性外，其它的像name，id是没有多个属性的）

例如：class="mnav c-font-normal c-color-t"，取mnav 或c-font-normal 或c-color-t都可以，只要这个class属性在页面上唯一就行。

#### 鼠标事件

> 导入库： ` from selenium.webdriver.common.action_chains import ActionChains`

````PYTHON
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element("id","kw").send_keys("哈哈哈哈")
driver.find_element("id","su").click()
time.sleep(1)

first=driver.find_elements(By.CSS_SELECTOR,r"#\31  > h3 > a")[0].click()
ActionChains(driver).move_to_element(first).click().perform() ##链式写法
###行为事件是存储在actionchains对象队列。当你使用perform()，事件按顺序执行。
time.sleep(1)
driver.close()
````

> 方法大全 : 

````PYTHON
click(on_element=None) ——单击鼠标左键
click_and_hold(on_element=None) ——点击鼠标左键，不松开
context_click(on_element=None) ——点击鼠标右键
double_click(on_element=None) ——双击鼠标左键
drag_and_drop(source, target) ——拖拽到某个元素然后松开
drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
key_down(value, element=None) ——按下某个键盘上的键
key_up(value, element=None) ——松开某个键
move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
move_to_element(to_element) ——鼠标移动到某个元素
move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
perform() ——执行链中的所有动作
release(on_element=None) ——在某个元素位置松开鼠标左键
send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
````

> 代码部分:

```` python
driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/mouseover.htm")
Woh= driver.find_element(By.XPATH,"/html/body/form/input[1]")
Boh= driver.find_element(By.XPATH,"/html/body/form/input[2]")
result = driver.find_element(By.NAME,'t1')
ActionChains(driver).move_to_element(Woh).perform()
print(result.get_attribute('value'))
time.sleep(2)
ActionChains(driver).move_to_element(Boh).perform()
print(result.get_attribute('value'))
ActionChains(driver).move_by_offset(10,-50).perform()
print(result.get_attribute('value'))
driver.close()
````

>  模拟Ctrl+C Ctrl+V Ctrl+A

```PYTHON
ActionChains(driver).move_to_element(Woh).move_to_element(result).click().perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').send_keys('c').send_keys('v').send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(2)
```

> 删除元素属性

```python
driver.execute_script("arguments[0].removeAttribute('style')", element)   ##arguments是python向JS传递的内容，使用element参数传递
```

> 操作滚动条

1.使用Keys_Down

```` python
ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
````

2.使用driver.execute_script()方法调用JS

````python
driver.execute_script("window.scrollTo(0,400)")
````



