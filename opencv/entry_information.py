import os
import cv2

def func1(str1):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    flag = 1
    num = 1
    while (cap.isOpened()):  # 检测摄像头是否开启
        ret_flag, Vshow = cap.read()  # 得到每帧图像
        cv2.imshow("Capture_Test", Vshow)  # 显示图像
        k = cv2.waitKey(1) & 0xFF  # 压下按键判断
        if k == ord(' '):
            cv2.imwrite("F:/AI/mycodetest/opencv/data/jm/" + str(num) + "." + str1 + ".jpg", Vshow)  # 把这个图像压倒这个路径里面
            print("success to save" + str(num) + "." + str1 + ".jpg")  # 保存成功
            print("------------")
            num += 1
        elif k == ord('1'):
            break;
    # 释放摄像头
    cap.release()
    # 释放内存
    cv2.destroyAllWindows()