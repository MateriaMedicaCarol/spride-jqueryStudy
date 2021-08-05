import sys

try:
    f = open('456.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print('Could not convert data to an integer')

# format 格式化函数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
# "0" 是必须的

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0}, 地址 {1}".format(*my_list))

my_list2 = {'name': '菜鸟教程', 'url': 'www.runoob.com'}
print("网站名：{name}, 地址 {url}".format(**my_list2))
