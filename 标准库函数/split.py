str = 'this is string example ... wow!!!'
print(str.split())
print(str.split('i', 1))
print(str.split('w'))
print(str[0])
print(str.startswith('this'))
print(str.startswith('string', 8))
print(str.startswith('this', 2, 4))

print(str[20])
print(str[18])
print(str.endswith('!!'))
print(str.endswith('!!', 20))
print(str.endswith('!!', 20, 24))

import re
#
# print(re.split('w', str))
# line = 'asdf fjdk; afed, fjek,asdf'
# parts = re.split(r'[;,\s]\s*', line)
# print(parts)
# fields = re.split(r'(;|,|\s)\s*', line)
# print(fields)
