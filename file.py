fo = open('10.1.txt', 'w+')
print('the name of the file', fo.name)
# seq = ['挽王夫人 作者：吴泳      朝代：宋朝\n', '婉娩娴诗画，僮僮被典章。\n', '有齐先祭洁，薄汗展衣香。\n', '唁卫心虽切，伤周义不忘。\n', '勉哉君子正，彤管尚遗芳。']
# fo.writelines(seq)
fo = open('10.1.txt', 'r+')
txt = fo.read(10)
print('the cotent of the file:%s'%(txt))
fo.close()
