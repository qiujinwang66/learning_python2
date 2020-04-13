import sys
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# if __name__ == "__main__":
#     print(factorial(5))

# def test():
#     return test()
# print(sys.getrecursionlimit())
# if __name__ == "__main__":
#     test()
#  x的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1
# def power (x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n-1)
# if __name__ == "__main__":
#     print(power(2, 6))
# 取出n层嵌套列表里的所有元素
# 提示判断一个元素i是否是list 使用isinstance(i,list)函数
l = [21, 2, 3, [47, 5, 6]]
def lie(l):
    for i in l:
        if isinstance(i,list):
            lie(i)

        else:
            print(i)

if __name__ == "__main__":
     lie(l)
