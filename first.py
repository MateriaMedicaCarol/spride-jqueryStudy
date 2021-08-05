g_numb1 = 1
g_numb2 = 2


def add_num():
    # global g_numb1
    g_numb1 = 3
    result = g_numb1 + 1
    print("result:%d" % result)


add_num()
print("g_numb1:%d" % g_numb1)

abc = 'abc'
print("nihao", abc)
print("nihao%s" % abc)

print('name:%s,age%d' % ('ding', 12))

print('peace', 100)

print("我想吃西瓜?\'buxiangchi!\'")
print('woxiang\\\\')
print(R'\t\r')

# 格式化输出
print("我的名字是%s,今年%d岁" % ('猪八戒', 338))

mystr = 'you build it ,you run it'
c = mystr.count('u')
print(c)
print(mystr.count('you'))

number = list(range(1, 4))
print(number)
print(number[2])

car = ['aodi', 'bmw', 'benchi', 'lingzhi']
print(car[0].title)
print(car[1])
cars = car[1]
print(cars)
