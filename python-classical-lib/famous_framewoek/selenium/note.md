from selenium import webdriver
webdriver实例的基本方法：
    find_element_by_id # ID
    find_elements_by_class_name # class
    find_elements_by_tag_name # 标签名
    find_elements_by_name # name
    find_elements_by_link_text # a标签中的text查找（精确匹配）
    find_elements_by_partial_link_text #a标签中的text查找（部分匹配即可）
    后面的定位方式
    find_elements_by_css_selector # css选择器查找
    find_elements_by_xpath # find_elements_by_xpath("//input")
    xpath搜索格式：
		'//input[@id="kw" and @name="C"]'  含有id = 'kw'的input标签，如果不确定哪个标签，可以用*代替，继续查找其下的自标签用/衔接
		'//input[@id="kw" and @name="C"]/../a'	 寻找同级标签
		'//input[contains(@class,"original")]'
		'//*[contains(text(),"btn")]'
		'//':往后寻找    '.':当前    '/.':回到上一级    './':返回子节点


	定位高阶：
		.//A/B/C[last()]    C是其上一级目录（不一定是B，如B//C）的最后一个子元素
		.//A/B/C[position()>1]

https://www.cnblogs.com/songshu120/p/5182043.html

它们返回的是webelement对象
############################webelement对象可以使用定位方法，而且是在它的分支中定位，值得注意的是使用
                            xpath时，开头是'.'


from selenium.webdriver.common.by import By
也可以通过find_element(By.ID,'kw') == find_element_by_id('kw')
By的策略集
CLASS_NAME = 'class name'
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link text'
TAG_NAME = 'tag name'
XPATH = 'xpath'


注：find_element_by_ 将获取 find_elements_by_ 的第一个元素，
    获取到的元素会被包装为 WebElement 对象  #######？？？？？？？？？？######
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait,构造器，接受一个Driver实例，超时时长（秒），执行条件函数的间隔时间。

  用于实例化一个Driver的显式等待。如果条件函数在规定时间内返回True则即刻继续执行，否则将抛出一个异常！
如：
	WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'vd-list')))


自定义条件函数：

def hasDoctors(d): # 自定义条件函数 when the function is called , the first prms will be a driver
if (len(d.find_elements_by_css_selector('.vd-list li'))):
    return True
return False
WebDriverWait(driver, 20, 0.5).until(hasDoctors) # 自定义函数形式

####EC.presence_of_all_elements_located的实质就是这个

until_not()相反





expected_conditions

支持的内置的预期条件，简称EC，如下：
title_is：判断当前页面的title是否完全等于（==）预期字符串

title_contains：判断当前页面的title是否包含预期字符串

presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见

visibility_of_element_located：判断某个元素是否可见，可见代表元素非隐藏，并且元素的宽和高都不等于0

visibility_of：与上述的方法一样，区别是上述方法要传入元祖locator即(By.ID,'kw')，此方法直接传定位到的WebElement

presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中，有则返回WebElements列表

text_to_be_present_in_element：判断元素的text是否包含预期字符串

text_to_be_present_in_element_value：判断元素的value属性是否包含预期字符串

frame_to_be_available_and_switch_to_it：检查给定帧是否可切换到，如果可以，则将给定的驱动器切换到指定的iframe

more:https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected_conditions#selenium.webdriver.support.expected_conditions


#启动项
chrome_options = Options()
chrome_options.add_argument("window-size=1024,768")

--user-agent="" 	设置请求头的User-Agent
--window-size=1366,768 	设置浏览器分辨率（窗口大小）
--headless 	无界面运行（无窗口）
--start-maximized 	最大化运行（全屏窗口）
--incognito 	隐身模式（无痕模式）
--disable-javascript 	禁用javascript
--disable-infobars 	禁用浏览器正在被自动化程序控制的提示
完整指令集:https://peter.sh/experiments/chromium-command-line-switches/


