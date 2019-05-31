# coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import time,json,re
from selenium import webdriver
from Public_method import means,inputAddr,intializating,get_goods,table

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class Case(unittest.TestCase):
    def test(self):
        print('###############>>>>>>选择数量大于库存数量，提示库存不足，无法下单>>>>>>>#################')
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
        # 判断积分是否能足以支付商品
        get_goods.get_goods(self)
        time.sleep(2)
        loc = (By.CSS_SELECTOR,dict_load['商品']['点击规格'])
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self,'css',dict_load['商品']['点击规格'])
        time.sleep(2)
        means.click(self,'css',dict_load['商品']['输入商品数量'])
        means.input(self,'css',dict_load['商品']['输入商品数量'],'100')
        time.sleep(2)
        means.click(self,'css',dict_load['商品']['保存'])
        time.sleep(2)
        # 这里手动执行不会触发查询库存接口
        kucunbuzu = means.get_text(self,'css',dict_load['商品']['立即兑换'])
        '''''''''
        loc = (By.CSS_SELECTOR,dict_load['商品']['兑换'])
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(loc))
        means.click(self, 'css', dict_load['商品']['兑换'])
        time.sleep(2)
        loc = (By.CSS_SELECTOR,dict_load['商品']['库存不足'])
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(loc))
        kucunbuzu = means.get_text(self,'css',dict_load['商品']['库存不足'])
        '''
        # 购买商品后积分余额
        jifen_after_pay = table.read(self,1)
        # 购买商品后菜籽余额
        caizi_after_pay = intializating.initialization.get_caizi_values(self)
        # 购买商品后总订单量
        count_order_on_db_after = intializating.initialization.get_countOrder_values(self)
        print('********************************金额*******************************************')
        print('原先用户菜籽：{1}'.format(self,caiz_before))
        print('原先用户积分：{1}'.format(self,jifen_before[0]))
        print('原先数据库订单数：{1}'.format(self,count_order_on_db_before))
        print('******************************剩余金额*****************************************')
        print('剩余积分：{1}'.format(self,jifen_after_pay[0]))
        print('剩余菜籽：{1}'.format(self,caizi_after_pay))
        print('********************************订单*******************************************')
        print('数据库订单总数：{1}'.format(self,count_order_on_db_after))
        print('********************************断言*******************************************')

        try:
            #assert kucunbuzu == '商品库存不足(10000)'
            assert kucunbuzu == '库存不足'
            print('提示【库存不足】，无法下单！')
            assert count_order_on_db_after == count_order_on_db_before
            print('数据库用例执行前和用例执行后订单总数一致，无法下单！')
            assert jifen_after_pay[0] == jifen_before[0]
            print('用例执行前积分余额和用例执行后积分余额一致，无法下单！')
            assert caizi_after_pay == caiz_before
            print('用例执行前菜籽余额和用例执行后菜籽余额一致，无法下单！')

        except:
            print('断言出现问题，请检查！')

        # excel数据清理
        table.wipe_excel(self)


if __name__=="__main__":
    unittest.main(exit=False)

