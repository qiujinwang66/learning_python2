import os
path = "/Users/wangqiujin/Desktop/pycharm/gittest/"
all_files = os.listdir(path)
file_dict = dict()
for each_file in all_files:
    # 判断我们的这个each_file是否是文件
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size
for each in file_dict.items():
    print("{}大小{}".format(each[0], each[1]))