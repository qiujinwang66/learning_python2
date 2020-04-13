


# l = [1,3,5,2]
# b = l.__iter__()
# print(next(b))
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b , self.a + self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
l = []

for i in fibs:
    l.append(i)
    if i > 1000:
        print(i)
        break

print(l)