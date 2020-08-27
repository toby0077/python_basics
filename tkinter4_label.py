# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:46:56 2020
Python入门经典（2K超清，博主录制）：http://dwz.date/cfKX
@author:231469242@qq.com
微信公众号：pythonEducation
"""

import tkinter as tk
#创建窗口对象
window=tk.Tk()
#窗口名字
window.title('肥猫和大熊熊')
#窗口大小
window.geometry('400x200')
#窗口里创建标签
label=tk.Label(window,text='welcome to python_studio!',bg='red',
           font=('Arial',15),width=30,height=5)
#放置
label.pack()
#窗口不断刷新循环
window.mainloop()