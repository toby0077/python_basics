# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:22:53 2020

Python入门经典（2K超清，博主录制）：http://dwz.date/cfKX
@author:231469242@qq.com
微信公众号：pythonEducation
"""

from tkinter import *
# 创建窗口对象的背景色
window=Tk()
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
animal=["cat","dog","pig"]
#listbox object of tkinter module
#Listbox 列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
listb  = Listbox(window)          #  创建两个列表框控件
listb2  = Listbox(window) 
listb3  = Listbox(window)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
    
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

for item in animal:              # 第二个小部件插入数据
    listb3.insert(0,item)
#几何管理：包装 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
listb3.pack()
window.mainloop()                 # 进入消息循环