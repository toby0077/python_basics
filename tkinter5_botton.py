# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:39:54 2020

Python入门经典（2K超清，博主录制）：http://dwz.date/cfKX
@author:231469242@qq.com
微信公众号：pythonEducation
"""

import tkinter
from tkinter import messagebox

mysite='https://study.163.com/provider/400000000398149/index.htm?share=2&shareId=400000000398149' 
window = tkinter.Tk()
#窗口大小
window.geometry('400x200') 
def press():
    messagebox.showinfo("python_studio",mysite)
 
B = tkinter.Button(window, text ="press", command = press)
 
B.pack()
window.mainloop()