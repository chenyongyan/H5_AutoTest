# coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest,xlrd,xlwt
import time,json,re,random
from selenium import webdriver
from Public_method import means,intializating,inputAddr,get_goods,table

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class Case(unittest.TestCase):

    # 确认订单页修改地址，下单成功，收货地址更改修改后地址
    def test(self):
        print('>>>>>>>>>>>>>>>>>>>确认订单页修改地址，下单成功，收货地址更改修改后地址<<<<<<<<<<<<<<<<<<<<<<')
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
        count_order_on_db__before = intializating.initialization.get_countOrder_values(self)
        time.sleep(1)
        # 判断积分是否能足以支付商品
        get_goods.get_goods(self)
        # 获取之前的收货地址
        address = means.get_text(self,'css',dict_load['收货地址']['收货地址'])
        time.sleep(2)
        means.click(self,'css',dict_load['商品']['立即兑换'])
        # 获取商品价格和商品邮费之和
        count_jifen_pay = means.get_text(self,'css',dict_load['商品']['商品积分价格和积分邮费之和'])
        time.sleep(1)
        # 修改收货地址
        means.click(self,'css',dict_load['收货地址']['订单页面修改地址'])
        time.sleep(2)
        inputAddr.input_addr(self)
        time.sleep(1)
        means.click(self,'css',dict_load['商品']['兑换'])
        time.sleep(1)
        means.click(self,'css',dict_load['C端页面元素']['查看订单'])
        time.sleep(2)
        means.click(self,'css',dict_load['C端页面元素']['待发货列表商品1'])
        time.sleep(2)
        new_address = means.get_text(self,'css',dict_load['C端页面元素']['收货地址信息'])
        time.sleep(1)
        # 购买商品后积分余额
        jifen_after_pay = table.read(self,1)
        # 购买商品后菜籽余额
        caizi_after_pay = intializating.initialization.get_caizi_values(self)
        # 支付商品的菜籽
        caiz_Pay = table.read(self,2)
        # C端新增订单号
        new_OrderNumber_On_C_h5 = table.read(self,4)
        # B端新增订单号
        new_OrderNumber_On_B_h5 = table.read(self,3)
        # 数据库新增订单号
        new_OrderNumber_On_db = intializating.initialization.get_NewOrderNumber_On_db(self)
        # 购买商品后总订单量
        count_order_on_db_after = intializating.initialization.get_countOrder_values(self)
        # 判断订单状态>>>>待发货
        status = table.read(self,5)
        print('********************************金额*******************************************')
        print('原先用户积分:{1}'.format(self,jifen_before[0]))
        print('原先用户菜籽：{1}'.format(self,caiz_before))
        print('原先数据库订单数：{1}'.format(self,count_order_on_db__before))
        print('购买商品花费的积分:{1}'.format(self,count_jifen_pay))
        print('购买商品花费的菜籽：{1}'.format(self,caizi_after_pay))
        print('******************************剩余金额*****************************************')
        print('剩余积分：{1}'.format(self,jifen_after_pay[0]))
        print('剩余菜籽：{1}'.format(self,caizi_after_pay))
        print('********************************订单*******************************************')
        print('B端新增订单号：{1}'.format(self,new_OrderNumber_On_B_h5[0]))
        print('C端新增订单号：{1}'.format(self,new_OrderNumber_On_C_h5[0]))
        print('数据库新增订单号：{1}'.format(self,new_OrderNumber_On_db))
        print('数据库订单总数：{1}'.format(self,count_order_on_db_after))
        print('订单状态：{1}'.format(self,status[0]))
        print('********************************断言*******************************************')
        print(r"修改前地址：",format(address))
        print(r"修改后地址：",format(new_address))
        assert int(jifen_before[0]) == int(jifen_after_pay) + int(count_jifen_pay)
        print('用户积分断言成功！')
        assert int(count_order_on_db_after) == int(count_order_on_db__before) + 1
        print('订单写入数据库成功！')
        assert int(caiz_before) == int(caizi_after_pay[0]) + int(caiz_Pay[0])
        print('商家菜籽断言成功！')


        # excel数据清理
        table.wipe_excel(self)


if __name__=="__main__":
    unittest.main(exit=False)

