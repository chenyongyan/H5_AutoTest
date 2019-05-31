# user/python3
# coding:utf-8


import json,random
import time
from Public_method import means,intializating
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)


    # 填写收货地址
    def input_addr(self):
        means.click(self,'css',dict_load['收货地址']['收货人姓名'])
        time.sleep(2)
        name1 = 'jechen'
        name2 = 'kit'
        name3 = 'tiffiny'
        name4 = 'chenqiuhua'
        t = [name1, name2, name3, name4]
        name = random.sample(t, 1)
        means.clear(self,'css',dict_load['收货地址']['收货人姓名'])
        means.input(self,'css',dict_load['收货地址']['收货人姓名'],str(name))
        time.sleep(1)
        num = random.choice(['135', '138', '155']) + \
              "".join(random.choice("0123456789") for i in range(8))
        means.clear(self,'css',dict_load['收货地址']['手机号码'])
        means.input(self,'css',dict_load['收货地址']['手机号码'],str(num))
        time.sleep(1)
        means.click(self,'css',dict_load['收货地址']['所在地区'])
        time.sleep(1)
        loc = (By.CSS_SELECTOR,dict_load['收货地址']['省'])
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self,'css',dict_load['收货地址']['省'])
        time.sleep(1)
        means.click(self,'css',dict_load['收货地址']['广东省'])
        time.sleep(1)
        loc = (By.CSS_SELECTOR, dict_load['收货地址']['市'])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self,'css', dict_load['收货地址']['市'])
        time.sleep(1)
        means.click(self,'css',dict_load['收货地址']['广州市'])
        time.sleep(1)
        loc = (By.CSS_SELECTOR,dict_load['收货地址']['区'])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self,'css',dict_load['收货地址']['区'])
        time.sleep(1)
        means.click(self,'css',dict_load['收货地址']['天河区'])
        time.sleep(1)
        addr1 = '中兴发送到阁2303号这个地方'
        addr2 = '澳门仿佛刚刚恢复规划街66号'
        addr3 = '回家看看羊肉汤商家待发货'
        addr4 = '爱清街实打同一人实地方34号'
        l = [addr1, addr2, addr3, addr4]
        addr = random.sample(l, 1)
        means.clear(self,'css',dict_load['收货地址']['详细地址'])
        means.input(self,'css',dict_load['收货地址']['详细地址'],str(addr))
        time.sleep(1)
        means.click(self,'css',dict_load['收货地址']['保存'])