import re

print(u'\n^匹配一行文本开始处的文本')
lines = ['hello world', 'Hello world.', 'ni hao', 'hello tom']
results = []
results2 = []
for line in lines:
    if re.findall(r"^[hH]", line):
        results.append(line)
for line in lines:
    if re.findall(r'm$', line):
        results2.append(line)
print(results)
print(results2, '\n')

text = 'apple took itake tattle tattle tabled tax yed temperate'
print(re.findall(r'\bta.*\b', text))
print(re.findall(r'\bta.*?\b', text))
print(re.findall(r'\bta\S*?\b', text))
print(re.findall(r'\bta\S*?ed\b', text), '\n')

text2 = 'phone phoneplus iphone telephone telegram'
words = text2.split()
results3 = []
for word in words:
    if re.findall(r'phone\B', word):
        results3.append(word)
print(results3)
