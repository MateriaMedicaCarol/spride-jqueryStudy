print('输入两个数')
print('按下q退出程序')
while True:
    first_number = input('\n请输入第一个数:')
    if first_number == 'q':
        break
    second_number = input('\n请输入第二个数:')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('除数不能为零')
    else:
        print(answer)
