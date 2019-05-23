import requests
url = 'http://www.lunareclipse.net.cn:8000'
#注册新用户
email = 'ertyu'
password = 'ertyu'
nickname = 'nickname'
avatar = "hhh"
api = '/api/user'
data= {'nickname':nickname,'password':password,'email':email,
       'avatar':avatar}
r = requests.post(url+api,json=data)
print("注册新用户")
print(r.json())

# token

api = '/api/token'
email = 'ab'
password = 'ab'
r = requests.post(url+api,auth = (email,password))

auth_token=r.json()['token']
hed = {'Authorization': 'Bearer ' + auth_token}

# 获取用户信息
api = '/api/user/6'
print(auth_token)

print(hed)
r = requests.get(url+api,headers=hed)
print("获取用户信息")
print(r.json())


# 修改用户信息

api = '/api/user/6'

data= {'nickname':nickname,'password':password,'email':email,
       'avatar':avatar}
r = requests.put(url+api,json=data,headers=hed)
print("修改用户信息")
print(r.json())


# 获取用户群组信息
api = '/api/groups'
r = requests.get(url+api,headers=hed)
print("获取用户群组信息")
print(r.text)
print(r.json())

# 获取单个群组信息
api = '/api/group/1'

r = requests.put(url+api,headers=hed)
print("获取单个群组信息")
print(r.text)

# 创建群组
api = '/api/group/create'
group_id = 1
page = 1
per_page=10
avatar='avatar'
data={'group_id':group_id,'avatar':avatar,'group_name':'hahah'}
r = requests.post(url+api,json=data,headers=hed)
print("创建群组")
print(r.json())

# 获取指定分组包括组员的群组信息
api = '/api/group'
group_id = 1
page = 1
per_page=10
data={'group_id':group_id,'page':page,'per_page':per_page}

r = requests.post(url+api,json=data,headers=hed)
print("获取指定分组包括组员的群组信息")
print(r.json())

# 加入群组
api = '/api/group/join'
group_id = 1
page = 1
per_page=10
data={'group_id':group_id}

r = requests.post(url+api,json=data,headers=hed)
print("加入群组")
print(r.json())


# 退出群组
api = '/api/group/exit'
group_id = 1
page = 1
per_page=10
data={'group_id':group_id}

r = requests.post(url+api,json=data,headers=hed)
print("退出群组")
print(r.text)


# 获取分页全部用户信息

api = '/api/users'
data= {'page':1,'per_page':10}
r = requests.get(url+api,params=data,headers=hed)
print("获取分页全部用户信息")
print(r.json())




# 获取用户所有群组的消息根据时间倒序

api = '/api/message/all'
data= {'page':1,'per_page':10}
r = requests.post(url+api,json=data,headers=hed)
print("获取用户所有群组的消息根据时间倒序")
print(r.json())


# 获取指定群聊详细信息

api = '/api/message/group'
data={'group_id':group_id}
r = requests.post(url+api,json=data,headers=hed)
print("获取指定群聊详细信息")

print(r.json())


# 发送消息

api = '/api/message/send'
content = 'sdgsd'
data={'group_id':group_id,'content':content}
r = requests.post(url+api,json=data,headers=hed)
print("发送消息")
print(r.json())


# 注销
api = '/api/token'
r = requests.delete(url+api,headers=hed)
print("注销")
print(r.text)

