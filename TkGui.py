"""
CNfurikana
v1.2.0

https://github.com/Gleiphir
All rights reserved

distributed under MIT license

It's a free software, do NOT pay for this.
此为自由软件，请不要为此付费。
これはフリーソフトであるので無料です。

"""



about_text = """ \
v1.2.0\n
https://github.com/Gleiphir\n
All rights reserved\n
\n
distributed under MIT license\n
\n
It's a free software, do NOT pay for this.\n
此为自由软件，请不要为此付费。\n
これはフリーソフトであるので無料です。\n
\n
辛苦了，字幕组的各位\n
时代变了，这也许能帮上忙
"""

import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


import conv.conventer
import os

root = Tk()

#ttk.Separator(root, orient=VERTICAL).grid(column=1, row=0, rowspan=5, sticky='ns')
ttk.Separator(root).grid(column=3, rowspan=2, sticky="ew",padx = 2)

root.title('中文假名注音程序')

v2 = StringVar()
v2.set('\n\n\n\n\n')

file_path = '[        ]'
SV_file_path = StringVar()

LoshiraseRT = Label(root, text='将需要注音的内容输入下方，点击右侧按钮注音')
LoshiraseRT.grid(row=0, column=0, padx=2, pady=5)

LRTIn = Entry(width=40)
LRTIn.grid(row=1, column=0, padx=2, pady=5)


LRTOut = Label(root, textvariable=v2)
LRTOut.grid(row=2, column=0, padx=2, pady=5)

LoshiraseF = Label(root, text='将需要注音的内容逐行写入txt，在下面选择txt文件名\n将会在工作目录下output文件夹内生成文件名为原文件名+日期时间的注音txt文件\n请使用UTF-8编码\n')
LoshiraseF.grid(row=4, column=0, padx=2, pady=5)


LFileName = Label(root,textvariable=SV_file_path)
LFileName.grid(row=5, column=0, padx=2, pady=5)





def convertRT():
    cvr = conv.conventer.conventer(10)
    res = cvr.feed(LRTIn.get())
    text = ''
    for ln in res:
        text += ''.join(ln) +'\n'
        print(text)
    v2.set('\n' + text+ '\n')


def convertFile():
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

Button(root, text='注音', width=10, command=convertRT) \
 \
    .grid(row=1, column=1, sticky=E, padx=10, pady=5)



Button(root, text='浏览', width=10, command=browse) \
 \
    .grid(row=5, column=1, sticky=E, padx=10, pady=5)

Button(root, text='生成文档', width=10, command=convertFile) \
 \
    .grid(row=4, column=1, sticky=E, padx=10, pady=5)

Button(root, text='关于', width=10, command=about) \
 \
    .grid(row=6, column=0, sticky=W, padx=10, pady=5)

Button(root, text='点击退出', width=10, command=root.quit) \
 \
    .grid(row=6, column=1, sticky=E, padx=50, pady=5)

# 退出按钮必须是双击打开.py文件才可以，而不是在IDLE下调试运行时


mainloop()