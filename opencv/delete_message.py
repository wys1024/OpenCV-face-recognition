import os

def func4(str1):
    imagePath = "F:/AI/mycodetest/opencv/data/jm/"
    files = os.listdir(imagePath)
    for f in files:
        if str(os.path.split(f)[1].split('.')[1])==str1:
            print("删除成功",f)
            path2 = os.path.join(imagePath, f)
            os.remove(path2)
