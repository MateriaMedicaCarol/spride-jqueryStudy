# 不定长参数练习
import html


def avg(first, *rest):
    print(max(rest))
    print(max(rest))
    return (first + sum(rest)) / (1 + len(rest))


print("avg", avg(1, 2))
print("avg", avg(1, 2, 3, 4))


def make_element(name, value, **attrs):
    keyvals = ['%s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


print(make_element('商品', '小樱登山包', size='大号', quantity=6))
print(make_element('p', '<spam>'))


def person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = person('python', '开发语言', age=28)
print(musician)
musician = person('python', '开发语言', 28)
print(musician)


def users(names):
    "向好友打招呼"
    for name in names:
        msg = "hello," + name.title() + "!"
        print(msg)


usersname = ["张三", "李四", "王五", "赵六"]
users(usersname)
