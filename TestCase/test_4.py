# coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import time,json,re
from Public_method import means,get_goods,intializating,inputAddr,table

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class Case(unittest.TestCase):
    def test(self):
        print('###############>>>积分不足>>>提示不足，无法下单>>>查看状态，未进入待发货#################')
        # 环境检测
        intializating.initialization.environmentPrepar(self)
        time.sleep(1)
        # 获取下单前积分值
        jifen_before = table.read(self,0)
        time.sleep(1)
        # 获取下单前菜籽值
        caiz_before = intializating.initialization.get_caizi_values(self)
        time.sleep(1)
        # 订单下单前订单总数
        count_order_on_db_before = intializating.initialization.get_countOrder_values(self)
        time.sleep(1)
        # 商品选择
        means.click(self, 'css', dict_load['商品']['goods3'])
        time.sleep(1)
        means.clear(self,'css',dict_load['商品']['输入商品数量'])
        means.input(self,'css',dict_load['商品']['输入商品数量'],'100')
        time.sleep(1)
        means.click(self, 'css', dict_load['商品']['保存'])
        loc = (By.CSS_SELECTOR,dict_load['商品']['立即兑换文本'])
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(loc))
        text = means.get_text(self,'css',dict_load['商品']['立即兑换文本'])
        # 购买商品后积分余额
        jifen_after_pay = table.read(self,1)
        # 购买商品后菜籽余额
        caizi_after_pay = intializating.initialization.get_caizi_values(self)
        # 购买商品后总订单量
        count_order_on_db_after = intializating.initialization.get_countOrder_values(self)
        print('********************************金额*******************************************')
        print('原先用户积分：{1}'.format(self,jifen_before[0]))
        print('原先用户菜籽：{1}'.format(self,caiz_before))
        print('原先数据库订单数：{1}'.format(self,count_order_on_db_before))
        print('******************************剩余金额*****************************************')
        print('test_1后剩余积分：{1}'.format(self,jifen_after_pay[0]))
        print('test_1后剩余菜籽：{1}'.format(self,caizi_after_pay))
        print('********************************订单*******************************************')
        print('数据库订单总数：{1}'.format(self,count_order_on_db_after))
        print('********************************断言*******************************************')
        # 断言提示积分不足，订单数没有增加
        try:
            assert text == '积分不足'
            print('积分不足，无法下单！')
            assert int(count_order_on_db_before) == int(count_order_on_db_after)
            print('无法下单！订单没有增加')
            assert int(caizi_after_pay) == int(caiz_before)
            print('无法下单，菜籽不变！')
            assert int(jifen_before[0]) == int(jifen_after_pay[0])
            print('无法下单，积分不变！')

        except:
            print('断言失败！')

        # excel数据清理
        table.wipe_excel(self)


if __name__=="__main__":
    unittest.main(exit=False)
