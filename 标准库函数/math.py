import math

print(math.modf(100.12))
print(math.modf(100.12)[0])

# >=x的整数
print(math.ceil(-45.17))
# 小于等于x的整数
print(math.floor(-45.17))

x = 1.2345678
print(format(x, '.2f'))
print(format(x, '.3f'))
print(format(x, '.6f'))
print('{:0.3f}'.format(x))

print(math.isinf(x))
print(math.sqrt(x))
print(math.isnan(x))
