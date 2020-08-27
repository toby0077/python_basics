# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:01:06 2020

Python入门经典（2K超清，博主录制）：http://dwz.date/cfKX
@author:231469242@qq.com
微信公众号：pythonEducation
"""

import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x800')  # 这里的乘是小x
 
# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=800, width=800)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='1.png')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

canvas.pack()
# 第7步，主窗口循环显示
window.mainloop()