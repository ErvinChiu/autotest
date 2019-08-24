import  requests
class Request:
    #创建初始化函数，每次请求都提供url&params 两个参数
    def __init__(self,url,param):
        self.url = url
        self.param = param
    def http_request(self,method,cookies=None):#定义默认值
        if method.upper() =="GET":
            try:
                res=requests.get(self.url,self.param,cookies=cookies)
            except Exception as e:
                print("执行get请求报错，错误信息是：{0}".format(e))
                res = "ERROR:get 请求报错{0}".format(e)
        elif method.upper() == "POST":
            try:
                res = requests.post(self.url, self.param, cookies=cookies)
            except Exception as e:
                print("执行post请求报错，错误信息是：{0}".format(e))
                res = "ERROR:post 请求报错{0}".format(e)
        else:
            print("你请求的方式不对！！")
            res="error:请求方式错误{0}".format(method)
        return res
if __name__=="__main__":
    url = "http://dev-sit-ind.pinganzhiyuan.com/credit-management/v1/user-credits"
    param = {"uid":"User2019081301","product_code":"CHIU","credit_amount":"1000000","app_bundle_id":"13","app_channel":"15","app_device_id":"ioservinchiu20190813"}
    res_init=Request(url,param).http_request("POST")
    print(res_init.json())
