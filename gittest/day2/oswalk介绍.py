import os

for dirpath, dirames, filenames  in os.walk("/Users/wangqiujin/Desktop/pycharm/gittest/"):
    #print('[' + dirpath + ']')
    for filename in filenames:
        print(os.path.join(dirpath, filename))