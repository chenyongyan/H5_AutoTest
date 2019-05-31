# user/python3
# coding:utf-8

import re,pymysql,requests
from selenium import webdriver
from Public_method import MySql,table
import json
from time import sleep
from Public_method import means
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class initialization(object):
    # 检测积分是否达到要求
    def environmentPrepar(self):
        mobile_emulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get(dict_load['url']['C端URL'])
        sleep(1)
        loc = (By.CSS_SELECTOR, dict_load['C端页面元素']['用户积分'])
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
        u1 = means.get_text(self, 'css', dict_load['C端页面元素']['用户积分'])
        u2 = re.findall(r"(......+?)", str(u1))
        u3 = str(u2).replace(',', '')
        # C端用户下单前用户积分
        u4 = u3[2:-2]
# 0>>>
        table.cretaTable(self)
        table.write(self,0,u4)
        sleep(4)
        if int(u4) <= 4000:
            print('用户积分不足，请充值积分！')
        elif int(u4) > 4000:
            print('积分充足！准备执行用例......')
        else:
            print('用户积分为0，请检查环境！')
        # 数据库初始化
        self.db = pymysql.connect(host=dict_load['mysql']['host'],user=dict_load['mysql']['user'], password=dict_load['mysql']['pwd'],)
        try:
            self.db
            print('数据库连接成功！准备执行用例......')
        except:
            print('数据库连接失败！请检查！')
        self.cursor = self.db.cursor()
        self.cursor.execute('SHOW DATABASES')
        c = MySql.db_Query(self, dict_load['mysql']['商家菜籽db'], dict_load['mysql']['查询商家菜籽sql'])
        c1 = re.findall(r"[(]'(.......+?).", str(c))
        if int(c1[0]) <= 1000000:
            MySql.db_NotQuery(self, dict_load['mysql']['商家菜籽db'], dict_load['mysql']['加菜籽sql'])
            print('菜籽充足！准备执行用例......')
        else:
            print('菜籽充足！准备执行用例......')

    # C端用户下单后用户积分
    def get_jifen_AfterValues(self):
        mobile_emulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get(dict_load['url']['C端URL'])
        sleep(1)
        loc = (By.CSS_SELECTOR, dict_load['C端页面元素']['用户积分'])
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
        q1 = means.get_text(self, 'css', dict_load['C端页面元素']['用户积分'])
        q2 = re.findall(r"(......+?)", str(q1))
        q3 = str(q2).replace(',', '')
        q4 = q3[2:-2]
# 1>>
        table.write(self,1,q4)

    # B端用户下单前菜籽余额(6位数)
    def get_caizi_values(self):
        c = MySql.db_Query(self, dict_load['mysql']['商家菜籽db'], dict_load['mysql']['查询商家菜籽sql'])
        c1 = re.findall(r"[(]'(.......+?).", str(c))
        return c1[0]

    # 测试前京东预存款余额
    def get_JD_values(self):
        AccessToken = MySql.db_Query(self, dict_load['mysql']['京东预存款db'], dict_load['mysql']['查询京东AccessToken'])
        url = dict_load['url']['京东预付款URL']
        date = {'token': AccessToken}
        respones = requests.post(url, date)
        AdvanceDeposit = re.findall(r'"result":"(.+?)"', str(respones.text))
        value = AdvanceDeposit[0]
        return value

    # 下单前数据库订单数
    def get_countOrder_values(self):
        a = MySql.db_Query(self, dict_load['mysql']['商家菜籽db'], dict_load['mysql']['查询用户订单总数sql'])
        a1 = re.findall(r"[(][(](.+?),", str(a))
        return a1[0]

    # 获取商家支付的菜籽数量
    def get_pay_caizi_values(self):
        self.driver.get(dict_load['url']['B端URL'])
        self.driver.find_element_by_css_selector(dict_load['B端页面元素']['兑换订单']).click()
        sleep(1)
        loc = (By.CSS_SELECTOR, dict_load['B端页面元素']['待发货列表商品1'])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(loc))
        self.driver.find_element_by_css_selector(dict_load['B端页面元素']['待发货列表商品1']).click()
        sleep(1)
        p1 = self.driver.find_element_by_css_selector(dict_load['B端页面元素']['B端支付菜籽']).text
        p2 = re.findall(r"^(......)", str(p1))
        p3 = str(p2).replace(',', '')
        pay = p3[2:-2]
# 2>>>
        table.write(self,2,pay)

    # 获取数据库新生成的订单号
    def get_NewOrderNumber_On_db(self):
        db_PartnerOrderNO = MySql.db_Query(self, dict_load['mysql']['查询新订单号db'], dict_load['mysql']['查询新订单号sql'])
        db_odd_numbers = re.findall(r"'(.+?)'", str(db_PartnerOrderNO))
        return db_odd_numbers[0]

    # 获取B端待发货商品列表新订单单号
    def get_newOrderNumber_On_B_h5(self):
        self.driver.get(dict_load['url']['B端URL'])
        self.driver.find_element_by_css_selector(dict_load['B端页面元素']['兑换订单']).click()
        sleep(2)
        b_orderNumber = means.get_text(self, 'css', dict_load['B端页面元素']['B端待发货列表新增商品单号'])
# 3>>>
        table.write(self,3,b_orderNumber)

    # 获取C端待发货商品列表新订单单号
    def get_newOrderNumber_On_C_h5(self):

        self.driver.get(dict_load['url']['C端URL'])
        self.driver.find_element_by_css_selector(dict_load['C端页面元素']['订单']).click()
        sleep(2)
        c_orderNumber = means.get_text(self, 'css', dict_load['C端页面元素']['C端待发货列表新增商品单号'])
# 4>>>
        table.write(self,4,c_orderNumber)

    # 判断订单状态>>>>待发货
    def order_status(self):
        db_PartnerOrderNO = MySql.db_Query(self, dict_load['mysql']['查询新订单号db'], dict_load['mysql']['查询新订单号sql'])
        c_OrderNO = table.read(self,4)
        assert db_PartnerOrderNO[0] == c_OrderNO
# 5>>
        table.write(self,5,'待发货')

    # 清空数据库订单
    def wipe_data(self):
        MySql.db_NotQuery(self, dict_load['mysql']['清空所有订单db'], dict_load['mysql']['清空所有订单sql'])
