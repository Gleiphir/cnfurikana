# CNfurikana

Auto mark Chinese pronunciation by marking furikana on characters.

轻量级的用假名标注中文音调与读音的软件。

基于pypinyin以及jieba等库。

便于阅读某些不熟练而又不得不快速准确读出的东西，例如直播间的superchat等。

同时也是日语母语者学习中文的助力。


# Release
## Latest
### 1.3.1-qt
自行完成了界面的日语翻译。
如有相关建议请随时提出，如有志参与也欢迎联系。

整理了UI界面。

现在主程序改为使用PyQt5构建，为下一个小版本的界面美化打下基础。

https://github.com/Gleiphir/cnfurikana/raw/main/CNfurikana-1.3.1-qt.zip

## Legacy
### 1.2.0
使用制表符，在大多数情况下解决了可能存在的对齐问题。

增加了实时短句翻译功能。与原本的文档翻译整合在一起。

整理了UI界面。

现在主程序名为CNfurikana了。

https://github.com/Gleiphir/cnfurikana/raw/main/CNfurikana%20v1.2.0.zip


### 1.1.0
基于Tkinter的UI现在可以选择原始文件而非输入路径了。

换用全角空格，大幅优化了对齐问题。

这是第一个实用化版本，之后的中版本号将在重大更新发表时更新。

https://github.com/Gleiphir/cnfurikana/raw/main/CNfurikana%20v1.1.0.zip


### 1.0.0
基于Tkinter的轻量级UI，用于文本处理。

https://github.com/Gleiphir/cnfurikana/raw/main/CNfurikana%20v1.0.0.zip

# Dependency

pypinyin>=0.39.1
jieba>=0.42.1
python>=3.8.0
PyQt5 >= 5.15.1

# License
MIT License
