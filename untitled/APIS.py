import requests
res=requests.get("http://www.lemfix.com/")
print(res.status_code)
print(res.headers)
print(res.cookies)