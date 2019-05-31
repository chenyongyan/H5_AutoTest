# user/python3
# encoding:utf-8
import unittest,json,time,re
from Public_method import means,MySql,intializating,inputAddr,get_goods
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class case(unittest.TestCase):


    def test(self):
        print('>>>>>>>>>>>>>>>>>>>未填收货地址 >> 跳转至收货地址填写<<<<<<<<<<<<<<<<<<<<<<')
        # 环境检测
        intializating.initialization.environmentPrepar(self)
        time.sleep(1)
        # 清空收货地址
        MySql.db_NotQuery(self,dict_load['mysql']['清空收货地址db'],dict_load['mysql']['清空收货地址sql'])
        time.sleep(1)
        # 选取商品
        get_goods.get_goods(self)
        time.sleep(1)
        loc = (By.CSS_SELECTOR, dict_load['商品']['立即兑换'])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self, 'css', dict_load['商品']['立即兑换'])
        time.sleep(1)
        # 获取跳转收货地址填写页面截图
        means.get_img(self)
        time.sleep(1)
        # 获取收货地址页面元素
        text = means.get_text(self,'css',dict_load['C端页面元素']['收货地址页面'])
        text1 = re.search(r"^(....)",str(text))
        text2 =text1.group()
        time.sleep(1)

        print('********************************状态*******************************************')
        print('跳转到页面信息：',format(str(text)))
        print('********************************断言*******************************************')
        # 断言
        assert text2 == '收货地址'
        print('用例通过！')

if __name__=="__main__":
    unittest.main(exit=False)