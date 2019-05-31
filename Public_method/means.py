# coding:utf-8

import os,json
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

##########################自己封装的方法##########################


# 前进
def forward(self):
    self.driver.forward()

# 浏览器后退
def back(self):
    self.driver.back()

# 关闭浏览器
def closeBrowser(self):
    self.driver.quit()

# 获取截图
def get_img(self):
    file_path = os.path.dirname(os.path.abspath('.')) + '/IMAGE/'
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_name = file_path + rq + '.png'
    try:
        self.driver.get_screenshot_as_file(screen_name)
    except NameError as e:
        self.get_windows_img()

# 切换窗口
def switch_handel(self):
    all_handles = self.driver.window_handles
    for handle in all_handles:
        self.driver.switch_to.window(handle)

#打开浏览器
def openBrowser(self, type, url):
    if type == 'Firefox':
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)
    elif type == 'Chrome':
        mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.driver.get(url)
        self.driver.implicitly_wait(15)
    elif type == 'IE':
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)
    elif self.browser_type == '':
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

# 输入框输入方法
def input(self, type, loc, value):
    if type == "xpath":
        self.driver.find_element_by_xpath(loc).send_keys(value)
    elif type == "class_name":
        self.driver.find_element_by_class_name(loc).send_keys(value)
    elif type == "id":
        self.driver.find_element_by_id(loc).send_keys(value)
    elif type == "name":
        self.driver.find_element_by_name(loc).send_keys(value)
    elif type == "link_text":
        self.driver.find_element_by_link_text(loc).send_keys(value)
    elif type == "partial_link_text":
        self.driver.find_element_by_partial_link_text(loc).send_keys(value)
    elif type == "css":
        self.driver.find_element_by_css_selector(loc).send_keys(value)

# 点击方法
def click(self, type, loc):
    if type == "xpath":
        self.driver.find_element_by_xpath(loc).click()
    elif type == "class_name":
        self.driver.find_element_by_class_name(loc).click()
    elif type == "id":
        self.driver.find_element_by_id(loc).click()
    elif type == "name":
        self.driver.find_element_by_name(loc).click()
    elif type == "link_text":
        self.driver.find_element_by_link_text(loc).click()
    elif type == "partial_link_text":
        self.driver.find_element_by_partial_link_text(loc).click()
    elif type == "css":
        self.driver.find_element_by_css_selector(loc).click()


# 清除方法
def clear(self, type, loc):
    if type == "xpath":
        self.driver.find_element_by_xpath(loc).clear()
    elif type == "id":
        self.driver.find_element_by_id(loc).clear()
    elif type == "name":
        self.driver.find_element_by_name(loc).clear()
    elif type == "link_text":
        self.driver.find_element_by_link_text(loc).clear()
    elif type == "partial_link_text":
        self.driver.find_element_by_partial_link_text(loc).clear()
    elif type == "css":
        self.driver.find_element_by_css_selector(loc).clear()

# 获取页面元素
def get_element(self, type, loc):
    if type == "xpath":
        self.driver.find_element_by_xpath(loc)
    elif type == "id":
        self.driver.find_element_by_id(loc)
    elif type == "name":
        self.driver.find_element_by_name(loc)
    elif type == "link_text":
        self.driver.find_element_by_link_text(loc)
    elif type == "partial_link_text":
        self.driver.find_element_by_partial_link_text(loc)
    elif type == "classname":
        self.driver.find_element_by_class_name(loc)
    elif type == "css":
        self.driver.find_element_by_css_selector(loc)

# 获取文本信息
def get_text(self, type, loc):
    if type == "xpath":
        text = self.driver.find_element_by_xpath(loc).text
        return text
    elif type == "name":
        text = self.driver.find_element_by_name(loc).text
        return text
    elif type == "link_text":
        text = self.driver.find_element_by_link_text(loc).text
        return text
    elif type == "class_name":
        text = self.driver.find_element_by_class_name(loc).text
        return text
    elif type == "id":
        text = self.driver.find_element_by_id(loc).text
        return text
    elif type == "css":
        text = self.driver.find_element_by_css_selector(loc).text
        return text

# 移动鼠标悬停在某元素上
def move_to_elemen_and_click(self, type, loc):
    if type == "xpath":
        xm = self.driver.find_element_by_xpath(loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == "id":
        xm = self.driver.find_element_by_id(loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == "name":
        xm = self.driver.find_element_by_name(loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == "link_text":
        xm = self.driver.find_element_by_link_text(loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == "css":
        xm = self.driver.find_element_by_css_selector(loc)
        webdriver.ActionChains(self.driver).click(xm).perform()

# 切换进入表单
def switch_in_iframe(self, iframe):
    self.driver.switch_to_frame(iframe)

# 切出表单
def switch_out_iframe(self):
    self.driver.switch_to_default_content()

# 显示等待知道元素可见
def element_is_visibility(self, timeout, loc):
    result = WebDriverWait(self, timeout).until(expected_conditions.visibility_of_element_located(loc))
    return result

#滚动界面
def page_slide(self, value):
    js = "var q=document.documentElement.scrollTop=" + str(value) + ""
    self.driver.execute_script(js)

# 结束浏览器进程
def kill_driver(self, driver_name):
    if driver_name[-4:].lower() != ".exe":
        driver_name += ".exe"
    os.system("taskkill /f /im " + driver_name)

# 选择下拉框的某一个值
def select_by_value(self, type, loc, value):
    if type == 'xpath':
        element = self.driver.find_element_by_xpath(loc)
        Select(element).select_by_value(value)
    elif type == 'id':
        element = self.driver.find_element_by_id(loc)
        Select(element).select_by_value(value)
    elif type == 'name':
        element = self.driver.find_element_by_name(loc)
        Select(element).select_by_value(value)
    elif type == 'css':
        element = self.driver.find_element_by_css_selector(loc)
        Select(element).select_by_value(value)
