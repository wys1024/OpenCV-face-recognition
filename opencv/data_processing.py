import os
import cv2
from PIL import Image
import numpy as np

def func2():

    def getImageAndLabels(path):
        # 保存人脸数据
        facesSamples = []
        # 保存姓名数据
        ids = []
        names = []
        # 保存图片信息
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # 加载分类器
        face_detector = cv2.CascadeClassifier("F:/AI/mycodetest/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
        # 遍历列表中的图片
        for imagePath in imagePaths:
            # 打开图片,灰度化PIL有九种不同格式
            PIL_img = Image.open(imagePath).convert('L')
            # 将图像转换为数组
            img_numpy = np.array(PIL_img, 'uint8')
            # 获取图片人脸特征
            faces = face_detector.detectMultiScale(img_numpy)
            # 获取每张图片的id和姓名
            id = int(os.path.split(imagePath)[1].split('.')[0])
            name = str(os.path.split(imagePath)[1].split('.')[1])
            # 预防无面容照片
            for x, y, w, h in faces:
                ids.append(id)
                names.append(name)
                facesSamples.append(img_numpy[y:y + h, x:x + w])
        # 打印脸部特征和id
        print('id:', id)
        print('name:',name)
        print('fs:', facesSamples)
        return facesSamples, ids

    #若无图像则退出
    if len(os.listdir("F:/AI/mycodetest/opencv/data/jm"))==0:
        print('无图像数据')
        return 0

    # 图片路径
    path = "F:/AI/mycodetest/opencv/data/jm/"
    # 获取图像数组和id标签数组和姓名
    faces, ids = getImageAndLabels(path)
    #print(faces)
    # 获取训练对象
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 训练
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write("F:/AI/mycodetest/opencv/trainer/trainer.yml")
