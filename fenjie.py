p = (4, 5)
x, y = p
print(x)
print(y)
data = ['acme', 50, 91.1, (2012, 2, 12)]
name, shares, price, data = data
print(name)
print(data)

operator = '/'
# c = get(operator)
result = {
    '*': x + y,
    '/': x / y
}
print(result.get(operator))
print(result[operator])

print(int())

str = ['a', 'b', 'c', 'd', 'e']
str1 = ''.join(str)
print(str1)

# 向空列表中添加元素
# 1、通过连接实现
# 2、通过append函数实现
list1 = []
list1 = list1 + ['abc']
list1.append('def')
print(list1)
list1[1] = 'ddd'
print(list1)


def printinfo(name, age):
    "打印传入的字符串"
    print("名字：", name)
    print("年龄：", age)
    print("\n")


printinfo(60, 'luoye')
printinfo(name='luoye',age=20)
printinfo('luoye',30)
printinfo('luoye','sjifa')
