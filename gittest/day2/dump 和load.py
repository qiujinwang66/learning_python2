import pickle

L = [1, 2, 3]
# with open("/Users/wangqiujin/Desktop/pycharm/gittest/L.dat", "wb") as f:
#     pickle.dump(L,f)
# with open("/Users/wangqiujin/Desktop/pycharm/gittest/L.dat", "rb") as f:
#     print(f.read())
with open("/Users/wangqiujin/Desktop/pycharm/gittest/L.dat", "rb") as f:

    print(pickle.load(f))

