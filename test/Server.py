import requests

url = 'http://www.lunareclipse.net.cn:8000'
api = '/api/token'
email = 'ab'
password = 'ab'
r = requests.post(url+api,auth = (email,password))

auth_token=r.json()['token']
hed = {'Authorization': 'Bearer ' + auth_token}
# 获取用户信息
api = '/api/user/1'
print(auth_token)

print(hed)
r = requests.get(url+api,headers=hed)
print(r.json)
print(r.text)

user = r.text
print(user)