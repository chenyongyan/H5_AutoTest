# coding:utf-8

import unittest
import time,json
from Public_method import means,intializating,inputAddr,get_goods,table

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)


class Case(unittest.TestCase):

    def test(self):
        print('>>>>>>>>>>>>>选择规格/数量/收货地址下单成功积分、菜籽、预存款扣除数额准确,状态切入待发货，C端B端生成订单<<<<<<<<<<<<<<')
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
        # 填写收货地址
        means.click(self,'css',dict_load['收货地址']['点击收货地址'])
        time.sleep(1)
        inputAddr.input_addr(self)
        time.sleep(1)
        means.click(self,'css',dict_load['商品']['立即兑换'])
        # 获取商品积分价格和商品积分邮费
        Price = means.get_text(self,'css',dict_load['商品']['商品积分价格和积分邮费之和'])
        means.click(self, 'css', dict_load['商品']['兑换'])
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
        # 购买商品后总订单量
        count_order_on_db_after = intializating.initialization.get_countOrder_values(self)
        # 判断订单状态>>>>待发货
        status = table.read(self,5)
        print('********************************金额*******************************************')
        print('原先用户积分:{1}'.format(self,jifen_before[0]))
        print('原先用户菜籽：{1}'.format(self,caiz_before))
        print('原先数据库订单数：{1}'.format(self, count_order_on_db_before))
        print('购买商品花费的积分:{1}'.format(self,Price))
        print('购买商品花费的菜籽:{1}'.format(self,caiz_Pay[0]))
        print('******************************剩余金额*****************************************')
        print('剩余积分：{1}'.format(self,jifen_after_pay[0]))
        print('剩余菜籽：{1}'.format(self,caizi_after_pay))
        print('********************************订单*******************************************')
        print('C端新增订单号：{1}'.format(self,new_OrderNumber_On_C_h5[0]))
        print('B端新增订单号：{1}'.format(self,new_OrderNumber_On_B_h5[0]))
        print('数据库订单总数：{1}'.format(self,count_order_on_db_after))
        print('订单状态：{1}'.format(self,status[0]))
        print('********************************断言*******************************************')
        # 断言
        try:
            assert int(jifen_before[0]) == int(Price)  + int(jifen_after_pay[0]),int(caiz_before) == int(caiz_before) + int(caiz_Pay[0])
            assert int(count_order_on_db_after) == int(count_order_on_db_before) + 1
            print('商品积分扣除正确！')
            print('商家菜籽扣除正确！')
            print('订单写入数据库成功！')
        except:
            return False

        # excel数据清理
        table.wipe_excel(self)

if __name__=="__main__":

    unittest.main()