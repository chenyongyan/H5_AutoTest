#coding:utf-8

import requests,pymysql,re,json,unittest,datetime,time

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)

class case_api(unittest.TestCase):

    def test_token(self):
        # 链接数据库
        self.db = pymysql.connect(
            host=dict_load['mysql']['host'],
            user=dict_load['mysql']['user'],
            password=dict_load['mysql']['pwd'],
            database=dict_load['mysql']['京东预存款db']
        )

        # 获取数据库列表
        cursor = self.db.cursor()
        cursor.execute('SHOW DATABASES')
        token_sql = dict_load['mysql']['查询京东AccessToken']
        cursor.execute(token_sql)
        result = cursor.fetchall()
        JD_AccessToken = re.findall(r"'(.+?)'", str(result))
        token = JD_AccessToken[0]
        return token

    # 查询京东预存款余额
    def test1(self):
        url = 'https://bizapi.jd.com/api/price/selectBalance'
        JD_token = case_api.test_token(self)
        date = {'token': JD_token}
        respones = requests.post(url, date)
        print('京东预存款余额:', format(respones.text))

    # 订单信息查询接口
    def test2(self):
        url = 'https://bizapi.jd.com/api/order/selectJdOrder'
        JD_token = case_api.test_token(self)
        date = {'token': JD_token,
                'jdOrderId': '91325361711',
                'queryExts': '15217635445'

                }
        respones = requests.post(url, date)
        print('订单信息查询:', format(respones.text))

    # 新建订单查询接口
    def test3(self):
        url = 'https://bizapi.jd.com/api/checkOrder/checkNewOrder'
        JD_token = case_api.test_token(self)
        Now_time = time.strftime("%y-%m-%d",time.localtime())
        print(Now_time)


        date = {'token': JD_token,
                'date':'2019-04-10',
                'pageNo': ''
                }
        respones = requests.post(url, date)
        print('新建订单查询:', format(respones.text))

if __name__=='__main__':
    unittest.main()