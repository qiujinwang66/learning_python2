#
# import os
#
# g = os.walk("/Users/wangqiujin/Desktop/pycharm/gittest/")
# print(next(g))
# print(next(g))
# print(next(g))

#def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# if __name__ == "__main__":
#     print(factorial(5))

# 列出目录下包括子目录的所有文件
# import os
# for dirpath, dirames, filenames  in os.walk("/Users/wangqiujin/Desktop/pycharm/gittest/"):
#     #print('[' + dirpath + ']')
#     for filename in filenames:
#         print(os.path.join( filename))
import os

def fac(all_path):
    flie_list = os.listdir(all_path)
    for flie in flie_list:
        dir_path = os.path.join(all_path, flie)
        if os.path.isdir(dir_path):
            fac(dir_path)
        if os.path.isfile(dir_path):
            print(flie)


if __name__ == "__main__":
    path = "/Users/wangqiujin/Desktop/pycharm/gittest/"
    fac(path)



