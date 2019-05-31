# user/python3
# coding:utf-8

import json,time,re,xlrd,xlwt
from Public_method import means
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

    # 获取商品积分，判断用户积分余额是否充足
    def get_goods(self):
        self.driver.get(dict_load['url']['C端URL'])
        loc = (By.CSS_SELECTOR,dict_load['C端页面元素']['积分排序'])
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self, 'css', dict_load['C端页面元素']['积分排序'])
        loc = (By.CSS_SELECTOR,dict_load['商品']['goods3_pay'])
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(loc))
        a = means.get_text(self, 'css', dict_load['商品']['goods3_pay'])
        a1 = re.findall(r"(.+?)积分", str(a))
        a2 = str(a1).replace(',', '')
        a3 = a2[2:-2]
        time.sleep(2)
        file = open('E:\\AutoTest\\Public_file\\date.txt' ,'r')
        jifen_before_pay = file.readlines()[0]
        if int(jifen_before_pay) < int(a3):
            print('积分不足，请充值！')
            self.driver.close()
        means.click(self, 'css', dict_load['商品']['goods3'])






