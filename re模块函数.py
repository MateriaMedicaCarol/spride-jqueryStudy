import re

# findall 返回一个列表
# 如果正则表达式使用了组，则返回一个元组


text = 'jgood is a handsome boy,he is cool, clever, and so on...'
regex = re.compile(r'\w*oo\w*')
print(regex)
print(regex.findall(text))

m = re.match('foo', 'foo')
print(m)
print(m.group())

n = re.match('fco', 'foo')
print(n)
# print(n.group()) AttributeError: 'NoneType' object has no attribute 'group'

s = 'well i wonder could it be when i was dreaming about you baby'
# 两对括号列表的元素为元组
print(re.findall(r'((\w+)\s+\w+)', s))
print(re.findall(r'((\w+\s+\w+))', s))
print(re.findall(r'(\w+\s+\w+)', s))

print('\n')
# 一个括号输出的列表元素是字符串，不输出括号外的东西
print(re.findall(r'(\w+)', s))
print(re.findall(r'(\w+)\s+\w+', s))

print('\n')
# 没有括号输出的列表元素是字符串
print(re.findall(r'\w+\s+\w+', s))

# group()函数的用法
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))  # 123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))  # 123
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  # abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))  # 456

# python中输出两个字符间自动存在一个空格;成为了一个字符，所有没有空格
print('\n' + re.search("([0-9]*)([a-z]*)([0-9]*)", a).group())  # 不传递参数默认num=0
print('\n' + str(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups()))  # 123abc456,返回整体

# 一定要用括号分组，否则有错误IndexError: no such group
# print(re.search("[0-9]*[a-z]*[0-9]*", a).group(1))


# import socket
#
# sk = socket.socket()
# sk.bind('127.0.0.1', 8080)
# sk.listen(5)
# conn, address = sk.accept()
# sk.sendall(bytes('hello world', encoding='utf-8'))


# import socket
#
# obj = socket.socket()
# obj.connect(('127.0.0.1', 8080))
# ret = str(obj.recv(1024), encoding='utf-8')
# print(ret)
