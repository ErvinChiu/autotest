import  requests
url = "http://dev-sit-ind.pinganzhiyuan.com/credit-management/v1/user-credits"
params = {"uid":"User2019081201","product_code":"CHIU","credit_amount":"1000000","app_bundle_id":"10","app_channel":"12","app_device_id":"ioservinchiu20190812"}
headers = {"Content-Type":"application/json"}
res = requests.post(url,params,headers)
print(res.json())
