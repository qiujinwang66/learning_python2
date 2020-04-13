

# def deco(func):
#     def inner():
#         print("running inner")
#     return  inner
# @deco
# def target():
#     print("running target")
#
# if __name__ == "__main__":
#     target()
#等于下面的写法
# def deco(func):
#     def inner():
#         print("running inner")
#     return  inner
#
# def target():
#     print("running target")
#
# if __name__ == "__main__":
#     target = deco(target())
#     target()
import time

def deco(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return  wrapper
@deco
def func():
    print("hello")
    time.sleep(1)
func()

def add_deco(f):
    def wrap(x, y):
        print("加法")
        return f(x, y)
    return wrap
@add_deco
def add_method(x, y):
    return x+y
print(add_method(2, 3))

#   带参数的装饰器

def out_f(arg):
    print("out_f" + arg)
    def decor(func):
        def inner():
            func()
        return inner
    return  decor

@out_f("123")
def func():
    print("hello")


