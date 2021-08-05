# 调用类内部的方法用self.methodName，调用类外的函数直接用函数名
# 调用类内部的变量，self.变量名

def diao(x, y):
    return (abs(x), abs(y))


class Ant:
    def __init__(self, x=0, y=0):
        self.s = x
        self.t = y
        self.d_point()

    def yi(self, x, y):
        x, y = diao(x, y)
        self.e_point(x, y)
        self.d_point()

    def e_point(self, x, y):
        self.s += x
        self.t += y

    def d_point(self):
        print("现在的位置是：（%d,%d)" % (self.s, self.t))


ant_a = Ant()
ant_a.yi(2, 7)
ant_a.yi(-5, 6)

age = 3
print('nihao ' + str(age) + '!')


class Site:
    def who(self):
        self._name = 'ding'
        _age = 5
        caiji = 7
        print(_age)
        print(caiji)

    def who2(self):
        print(self._name)


site1 = Site()
site1.who()
site1.who2()
a = 3
a += 1
print(a)
