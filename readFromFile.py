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

Label(root, text='将需要注音的内容逐行写入txt，在下面选择txt文件名\n将会在工作目录下output文件夹内生成文件名为原文件名+日期时间的注音txt文件\n请使用UTF-8编码\n').grid(row=0, column=0)

v2 = StringVar()

file_path = '[        ]'

SV_file_path = StringVar()
Lname = Label(root, text='将需要注音的内容逐行写入txt，在下面选择txt文件名\n将会在工作目录下output文件夹内生成文件名为原文件名+日期时间的注音txt文件\n请使用UTF-8编码\n',textvariable=SV_file_path)
Lname.grid(row=2, column=0, padx=2, pady=5)





def convert():
    cvr = conv.conventer.conventer(10)
    if not os.path.exists(file_path):
        messagebox.showwarning("File Not found","找不到文档")
        return
    name,suf = os.path.splitext(os.path.basename(file_path))

    tstamp = time.strftime("%y%m%d-%H%M", time.localtime())
    of_path = os.path.join(os.getcwd(),"output/",name + tstamp + suf)
    print(of_path)
    res = []
    with open(file_path,encoding="utf-8") as ifp:
            for iline in ifp.readlines():
                for oline in cvr.feed(iline[:-1]):
                    res.append(''.join(oline))
                    res.append(os.linesep)

    with open(of_path, "w", encoding="utf-8") as ofp:
        ofp.writelines(res)
    messagebox.showinfo('写入完成', '写入完成\n{}'.format(of_path))

def about():
    messagebox.showinfo('关于',about_text)

def browse():
    global file_path
    file_path = filedialog.askopenfilename()
    SV_file_path.set("source: [  "+ file_path + "  ]")

Button(root, text='浏览', width=10, command=browse) \
 \
    .grid(row=2, column=1, sticky=E, padx=50, pady=5)

Button(root, text='开始生成', width=10, command=convert) \
 \
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)

Button(root, text='关于', width=10, command=about) \
 \
    .grid(row=3, column=0, sticky=E, padx=30, pady=5)

Button(root, text='点击退出', width=10, command=root.quit) \
 \
    .grid(row=3, column=1, sticky=E, padx=50, pady=5)

# 退出按钮必须是双击打开.py文件才可以，而不是在IDLE下调试运行时


mainloop()