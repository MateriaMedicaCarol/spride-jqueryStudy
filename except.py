def testAssert():
    for i in range(4):
        try:
            assert i < 2
        except AssertionError:
            print('抛出一个异常')
        print('%d\n' % i)
    print('end...')


testAssert()


class RangeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


raise RangeError('Range错误')
