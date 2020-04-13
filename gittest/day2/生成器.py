


def gen():
    for i in range(10):
        x = (yield i)
        print(x)

g = gen()
print(next(g))
print(g.send(8))
print(g.send(22))


f = ( x ** 2 for x in range(4))
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))