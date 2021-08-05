import time

print('time.altzone ', time.altzone)
t = time.localtime()
print(t)
print(t.tm_year)
print('time.asctime', time.asctime(t))
print(time.ctime())


def procedure():
    time.sleep(2.5)

# time.clock()函数在python3.8中不支持 使用time.perf_counter()函数代替
# t0 = time.perf_counter()
# procedure()
# print(time.perf_counter() - t0)
#
# t0 = time.time()
# procedure()
# print(time.time() - t0)
