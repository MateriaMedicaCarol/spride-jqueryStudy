from fnmatch import fnmatchcase as match
import fnmatch

# 匹配以.py结尾的字符串
print(fnmatch.fnmatch('py', '.py'))

print(fnmatch.fnmatch('title.py', '*.py'))

print(fnmatch.fnmatch('123.txt', '*.TXT'))
print(fnmatch.fnmatchcase('123.txt', '*.TXT'))

addresses = ['5000 A AAA FF', '1000 B BBB', '1000 C CCC', '2000 D DDD NN', '4234 E EEE NN']
a = [addr for addr in addresses if match(addr, '*FF')]
print(a)
b = [addr for addr in addresses if match(addr, '42[0-9][0-9] *NN*')]
print(b)
for addr in addresses:
    if match(addr, '*CC'):
        c = [addr]
print('c:', c)
for addr in addresses:
    print(addr)
