import unittest
from ddt import ddt,data
from Http_request import Request
import get_excel_data
# 测试数据
test_data = get_excel_data.DoExcel("test_data.xlsx","test_data").get_excel()

@ddt
class Mytest(unittest.TestCase):
    @data(*test_data)
    def test_case_01(self,data_item):
        print("ddt分解传递的数据是：{0}".format(data_item))
        res = Request(data_item['url'],data_item['param']).http_request(data_item['mothod'])
        print(res.json())


