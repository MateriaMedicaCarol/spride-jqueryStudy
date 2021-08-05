class myClass:
    "这是一个‘地球人’的类"


myclass = myClass()
print(myclass.__doc__)
print('help\n')
help(myclass)


class SmplClass:
    def info(self):
        print("python is the best language of the world")

    def mycacl(self, x, y):
        return x + y


sc = SmplClass()
sc.info()
print(sc.mycacl(4, 5))
