# 使用装饰器对权限进行验证 这个没做
'''
def test(info):
    if info.username == 'root' and 'info.passwd'=='1223':
        print('你有权限')
    else:
        print('你没有权限')
        return
    return data = "1,2,3"

def test2(info):
    if info.username == 'root' and 'info.passwd'=='1223':
        print('你有权限')
    else:
        print('你没有权限')
        return
    return data2 = "4,5,6"
@permit
def test2(info)
    return data2 = "4,5,6"
@permit
def test(info)
    return data = "123"
'''
# 实现permit装饰器对权限进行验证

def permit(f):
    def wrapper(info):
        if info.username == 'root' and info.passwd=='123':
            print('你有权限 装饰器')
            return f(info)
        else:
            print('你没有权限')

    return wrapper


@permit
def test(info):
    return  '正常数据'

class Info:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

info = Info('root', '123')

print(test(info))
#  递归 获取所有文件

'''
import os
def fac(all_path):
    flie_list = os.listdir(all_path)
    for flie in flie_list:
        dir_path = os.path.join(all_path, flie)
        if os.path.isdir(dir_path):
            fac(dir_path)
        elif os.path.isfile(dir_path):
            print(flie)
if __name__ == "__main__":
    path = "/Users/wangqiujin/Desktop/pycharm/gittest/"
    fac(path)

# 找出单个目录中最大的文件

import os
maxsize = 0
for dirpath, dirnames, filenames in os.walk("/Users/wangqiujin/Desktop/pycharm/gittest/"):
    # print('[' + dirpath + ']')
    for filename in filenames:
        path = os.path.join(dirpath, filename)
        filsize = os.path.getsize(path)
        if filsize > maxsize:
            maxsize = filsize
            maxpath = path
print(maxpath, maxsize)
'''
'''
#  找出单个目录树中最大的文件
import os
maxsize = 0
for dirpath, dirnames, filenames in os.walk("/Users/wangqiujin/Desktop/pycharm/gittest/"):
    # print('[' + dirpath + ']')
    for filename in filenames:
        filsize = os.path.getsize(dirpath)
        if filsize > maxsize:
            maxflisize = filsize
            maxflifile = dirpath
        path = os.path.join(dirpath, filename)
        filsize = os.path.getsize(path)
        if filsize > maxsize :
            maxsize = filsize
            maxfile = path
print(maxfile, maxsize)
print(maxflifile, maxflisize)
'''