fo = open('10.4.txt', 'r+', encoding='UTF-8')
print('文件名', fo.name)
line = fo.read()
print('读取的内容：%s' % (line))
fo.close()
