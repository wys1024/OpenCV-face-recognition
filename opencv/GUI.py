from tkinter import *
from opencv.entry_information import func1
from opencv.data_processing import func2
from opencv.face_recognition import func3
from opencv.delete_message import func4

# 创建窗口：实例化一个窗口对象
root = Tk()
# 窗口大小
root.geometry("600x450+374+182")
# x代表*  宽乘高

# 窗口标题
root.title("人脸识别")
# #添加标签控件
label = Label(root, text="录入数据按三次空格"
                         " 录入完成按1 识别完成按3", font=("楷体", 20), fg="red")
# 定位
label.grid(row=0, column=0)
# 添加输入框并定位
# 放在第一行第二列的位置


label = Label(root, text="请输入姓名，只可输入英文", font=("楷体", 10), fg="red")
# 定位
label.grid(row=1, column=0)

entry = Entry(root, font=("宋体", 25), fg="blue")
entry.grid(row=2, column=0)



# 添加点击按钮
button = Button(root, text="信息录入", font=("楷体", 25), fg="blue", command=lambda: func1(str(entry.get())))
button.grid(row=3, column=0)
button = Button(root, text="分析数据", font=("楷体", 25), fg="blue", command=func2)
button.grid(row=4, column=0)
button = Button(root, text="开始识别", font=("楷体", 25), fg="blue", command=func3)
button.grid(row=5, column=0)
button = Button(root, text="删除信息", font=("楷体", 25), fg="blue", command=lambda: func4(str(entry.get())))
button.grid(row=6, column=0)
# 显示窗口
root.mainloop()
