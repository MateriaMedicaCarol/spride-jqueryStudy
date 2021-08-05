class NewClass(object):
    num_count = 0

    def __init__(self, name):
        self.name = name
        NewClass.num_count += 1
        print(name, NewClass.num_count)

    def __del__(self):
        NewClass.num_count -= 1
        print('del', self.name, NewClass.num_count)

    # def __init__(self, name):
    #     self.name = name
    #     self.num_count=0
    #     self.num_count += 1
    #     print(name, self.num_count)
    #
    # def __del__(self):
    #     self.num_count -= 1
    #     print('del', self.name, self.num_count)

    def test(self):
        print('aa')


aa = NewClass('java')
NewClass.num_count=8
bb = NewClass('c')
cc = NewClass('c++')
del aa
del bb
del cc
