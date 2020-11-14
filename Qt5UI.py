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
from conv.constants import config as conf

from PyQt5.QtWidgets import  QApplication,\
    QWidget, QMainWindow, QMessageBox, \
    QFileDialog, QPushButton, QLabel, \
    QGridLayout,QLineEdit
from PyQt5.QtGui import QFont
import conv.conventer
import os
import sys


#breakpoint()
font_size = conf['Intval','fontsize']


def HTMLify(text:str)-> str:
    return text.replace('\n','<br />')

class mainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFont(QFont('microsoft Yahei',font_size))
        self.setWindowTitle(conf['Text','windowtitle'])

        self.file_path = ''
        #self.maxLineWidthpx = QApplication.desktop().availableGeometry().width() // 2
        #self.maxLineWidth = self.maxLineWidthpx // (font_size * 4 //3)
        # 1px = 0.75point

        self.maxLineWidth = conf['Intval','LineWidth'] # in char

        self.LoshiraseRT = QLabel(self)
        self.LoshiraseRT.setText(conf['Text','hintRT'])

        self.LRTIn = QLineEdit(self)

        self.LRTOut = QLabel(self)
        #self.LRTOut.setMaximumWidth(self.maxLineWidth)
        #self.LRTOut.setWordWrap(True)

        self.LoshiraseF = QLabel(self)
        self.LoshiraseF.setText(conf['Text','hintFile'])

        self.LFileName = QLabel(self)

        self.markBtn = QPushButton(conf['Text','Bmark'], self)
        self.markBtn.clicked.connect(self.convertRT)

        self.browseBtn = QPushButton(conf['Text','Bbrowse'], self)
        self.browseBtn.clicked.connect(self.browse)

        self.genFileBtn = QPushButton(conf['Text','Bgenerate'], self)
        self.genFileBtn.clicked.connect(self.convertFile)


        self.aboutBtn = QPushButton(conf['Text','Babout'], self)
        self.aboutBtn.clicked.connect(self.about)

        self.QuitBtn = QPushButton(conf['Text','Bquit'], self)
        self.QuitBtn.clicked.connect(self.close)

        self.Cwidget = QWidget(self)

        self.initUI()

    def initUI(self):

        self.setCentralWidget(self.Cwidget)

        grid = QGridLayout()
        grid.setSpacing(5)
        self.Cwidget.setLayout(grid)


        grid.addWidget(self.LoshiraseRT, 0, 0)
        grid.addWidget(self.LRTIn, 1, 0)
        grid.addWidget(self.markBtn, 1, 1)
        grid.addWidget(self.LRTOut, 2, 0)

        grid.addWidget(self.LoshiraseF, 4, 0)
        grid.addWidget(self.LFileName, 5, 0)

        grid.addWidget(self.browseBtn, 5, 1)

        grid.addWidget(self.genFileBtn, 4, 1)
        grid.addWidget(self.aboutBtn, 6, 0)
        grid.addWidget(self.QuitBtn, 6, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)


    def convertRT(self):
        cvr = conv.conventer.conventer(self.maxLineWidth)
        res = cvr.feed(self.LRTIn.text())

        text = ''
        line3 = [''.join(l) for l in res]
        lines = []
        pos = [x for x in range(0, len(line3[1]),self.maxLineWidth)];pos.append(len(line3[1]))
        print("linewidth",self.maxLineWidth)
        for ind in range(len(pos)-1):
            for i in range(3):
                lines.append( "".join([ line3[i][ pos[ind]:pos[ind+1] ] ]) + "\n" )
        text = "".join(lines)
        print(text)
        self.LRTOut.setText(text)

    def convertFile(self):
        cvr = conv.conventer.conventer(self.maxLineWidth)
        if len(self.file_path) <= 0:
            QMessageBox.warning(self, "File required", "请输入文档")
            return
        if not os.path.exists(self.file_path):
            QMessageBox.warning(self, "File Not found", "找不到文档")
            return
        name, suf = os.path.splitext(os.path.basename(self.file_path))

        tstamp = time.strftime("%y%m%d-%H%M", time.localtime())
        os.makedirs(os.path.join(os.getcwd(), "output/"),exist_ok=True)
        of_path = os.path.join(os.getcwd(), "output/", name + tstamp + suf)
        print(of_path)
        res = []
        with open(self.file_path, encoding="utf-8") as ifp:
            for iline in ifp.readlines():
                for oline in cvr.feed(iline[:-1]):
                    res.append(''.join(oline))
                    res.append(os.linesep)

        with open(of_path, "w", encoding="utf-8") as ofp:
            ofp.writelines(res)
        QMessageBox.information(self, 'convert done', '写入完成\n{}'.format(of_path))

    def about(self):
        QMessageBox.about(self, 'about', '<p align=\"center\">'+ HTMLify(about_text) + "</p>")

    def browse(self):

        self.file_path,filetype= QFileDialog.getOpenFileName(self,"Source File")
        #if filetype
        self.LFileName.setText(self.file_path)
        #SV_file_path.set("source: [  " + file_path + "  ]")








if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = mainWindow()
    mainW.show()
    sys.exit(app.exec_())
