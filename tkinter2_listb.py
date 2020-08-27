# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:43:09 2020
Python入门经典（2K超清，博主录制）：http://dwz.date/cfKX
@author:231469242@qq.com
微信公众号：pythonEducation
"""

from tkinter import *
# 创建窗口对象的背景色
window=Tk()
language=['C','python','php','html','SQL','java']
#listbox object of tkinter module
#Listbox 列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
listb  = Listbox(window)         

for item in language:                 #插入数据
    listb.insert(0,item)

#几何管理：包装 
listb.pack()                    # 将小部件放置到主窗口中
window.mainloop()                 # 进入消息循环