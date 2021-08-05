import requests

# r = requests.get('https://www.baidu.com')
# print(r.text)
# print('\n')

payload = {'key1': ['a', 'b', 'c', 'd'], 'key2': 'e'}
payload2 = (('key2', 'e'), ('key2', 'f'), ('key2', 'g'))
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)
a = requests.post('http://httpbin.org/post', data=payload)
print(a.text)
c = requests.post('http://httpbin.org/post', data=payload2)
print(c.text)

# import requests
# import json
#
# host = "http://httpbin.org/"
# endpoint = "post"
# # url = ''.join([host, endpoint])
# # url='http://httpbin.org/post'
# # print(url)
# data = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)
# # response = r.json()
