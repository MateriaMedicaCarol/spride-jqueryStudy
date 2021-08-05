def test(index, i):
    stulst = ['aaa', 'bbb', 'ccc', 'dddddd']
    try:
        print(len(stulst[index]) / i)
    except:
        print("error")


test(3, 2)
test(3, 0)
test(4, 0)

# a,b=2
c,d=3,5
print(c,d)
