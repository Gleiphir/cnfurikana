"""

将舰长的名字每人一行写入txt，然后运行这个文件


"""
about_text = """ \
v1.1.0\n
https://github.com/Gleiphir\n
All rights reserved\n
\nNov 11,2020\n
\n\n
请不要为本软件付费\n
\n\n
辛苦了，绯赤艾莉欧组\n
时代变了，这也许能帮上忙
"""

import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import conv.conventer
import os

root = Tk()

root.title('中文假名注音程序')

Label(root, text='将需要注音的内容复制贴入下方输入框\n请使用UTF-8编码\n').grid(row=0, column=0)

v2 = StringVar()

file_path = '[        ]'

SV_file_path = StringVar()
LIn = Entry()
LIn.grid(row=2, column=0, padx=2, pady=5)

LOut = Label(root, textvariable=v2)
LOut.grid(row=3, column=0)




def convert():
    cvr = conv.conventer.conventer(10)
    res = cvr.feed(LIn.get())
    text = ''
    for ln in res:
        text += ''.join(ln) +'\n'
        print(text)
    v2.set(text)



def about():
    messagebox.showinfo('关于',about_text)

def browse():
    global file_path
    file_path = filedialog.askopenfilename()
    SV_file_path.set("source: [  "+ file_path + "  ]")

Button(root, text='转换', width=10, command=convert) \
 \
    .grid(row=3, column=1, sticky=E, padx=50, pady=5)

Button(root, text='关于', width=10, command=about) \
 \
    .grid(row=4, column=0, sticky=E, padx=30, pady=5)

Button(root, text='点击退出', width=10, command=root.quit) \
 \
    .grid(row=4, column=1, sticky=E, padx=50, pady=5)

# 退出按钮必须是双击打开.py文件才可以，而不是在IDLE下调试运行时


mainloop()