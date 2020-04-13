
# 序列化--
#     	 把对象变为字节就是序列化，把字节变为对象就是反序列化
#     	 son和pickle用法一样，但是格式不一样，应用的方式也不一样
#         json 是将字典、列表转换
#         pickle是可以将所有的Python对象，类、实例都转换



import pickle


class Record:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


R = pickle.dumps(Record)
print(R)
print(pickle.loads(R))

record = Record("贾敏强", "15801396646")
r = pickle.dumps(record)
print(r)
print(pickle.loads(r))