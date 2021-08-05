def copy(friend, relatives):
    while (friend):
        current_friend = friend.pop()
        relatives.append(current_friend)
        print(relatives)


friend = ['茉莉花', '油菜花', '菊花', '牡丹花']
relatives = []
copy(friend, relatives)
print(relatives)

# import any
# any.users(["张三", "李四", "王五", "赵六"])

from any import users

users(["张三", "李四", "王五", "赵六"])
