"""

将舰长的名字每人一行写入txt，然后运行这个文件


"""

# 示例12：登陆框程序
import time
from tkinter import *
from tkinter import messagebox
import conv.conventer
import os

root = Tk()

root.title('中文假名注音程序')

Label(root, text='将需要注音的内容逐行写入txt，在下面输入txt文件名\n将会在工作目录下output文件夹内生成文件名为原文件名+日期时间的注音txt文件\n请使用UTF-8编码\n').grid(row=0, column=0)

v2 = StringVar()

e2 = Entry(root, textvariable=v2)



e2.grid(row=1, column=0, padx=2, pady=5)


def convert():
    cvr = conv.conventer.conventer(10)
    fn = e2.get()
    name,suf = os.path.splitext(os.path.basename(fn))

    tstamp = time.strftime("%y%m%d-%H%M", time.localtime())
    of_path = os.path.join(os.getcwd(),"output/",name + tstamp + suf)
    print(of_path)
    res = []
    with open(fn,encoding="utf-8") as ifp:
            for iline in ifp.readlines():
                for oline in cvr.feed(iline[:-1]):
                    res.append(''.join(oline))
                    res.append(os.linesep)

    with open(of_path, "w", encoding="utf-8") as ofp:
        ofp.writelines(res)
    messagebox.showinfo('写入完成', '写入完成\n{}'.format(of_path))

def about():
    messagebox.showinfo('关于','v1.0.1\nhttps://github.com/Gleiphir\nAll rights reserved\n\nNov 11,2020\n\n\n请不要为本软件付费\n\n\n辛苦了，绯赤艾莉欧组\n时代变了，这也许能帮上忙')

Button(root, text='开始生成', width=10, command=convert) \
 \
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)

Button(root, text='关于', width=10, command=about) \
 \
    .grid(row=3, column=0, sticky=S, padx=30, pady=5)

Button(root, text='点击退出', width=10, command=root.quit) \
 \
    .grid(row=3, column=0, sticky=E, padx=50, pady=5)

# 退出按钮必须是双击打开.py文件才可以，而不是在IDLE下调试运行时


mainloop()