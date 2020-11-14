"""
data originate from https://dokochina.com/fayin.htm
"""
import json
import jieba
import conv.constants as C
from pypinyin import lazy_pinyin, Style
import os

class conventer():
    def __init__(self,linewidth):
        self.linewidth = linewidth
        self.toneSymbols = C.style_arrows
        self.splSymbol = C.symb_split[5]
        #TODO:更换注音符号
        with open(os.path.join(os.getcwd(),"conv/table.json"),encoding='utf-8') as f:
            self.trans2kana = json.load(f)
            #print(self.trans2kana)


    def toSign(self, pinyin:str):
        # style = Style.TONE3, strict =True
        #print(pinyin)
        if not isinstance(pinyin,str):
            return [ 0,self.toneSymbols[0], pinyin[0] ] # non-CN
        #print(pinyin[:-2])
        return [ int(pinyin[-1]),self.toneSymbols[int(pinyin[-1])], self.trans2kana[pinyin[:-1]] ]#声调+注音


    def kanaify(self,s:str):
        pinyinLst = lazy_pinyin(s, style=Style.TONE3, neutral_tone_with_five=True,errors=lambda x : (x,))
        CNchrLst = [x for x in s if C.isCNchar(x)]# generator
        #print(pinyinLst)
        res  = []
        for _ in pinyinLst:
            tmp = self.toSign(_)
            if tmp[0] == 0:
                tmp.append(tmp[1])
            else:
                tmp.append(CNchrLst.pop(0))
            #print(tmp)
            res.append( tmp.copy() )# 声调+ 注音 + 汉字
        return res

    def showInLine(self,kanalist:list):
        #避免将注音标记等在行尾截断。
        #TODO:↑
        text = [[],[],[]]
        for char in kanalist:
            char[2] = ''.join(char[2])
            if char[0] == 0:
                for n in (0, 1, 2):
                    text[n].append(char[2])
                continue
            del char[0]
            # 任何注音方式都不会比汉字本身更短
            maxlen = max([len(part) for part in char ])

            for n in (0,1,2):

                #print(char, maxlen,(maxlen - len(char[n])))
                char[n] = ''.join([char[n],'\u3000'* (maxlen - len(char[n])),self.splSymbol ])

                text[n].append( char[n])
        #TODO:添加对其他注音风格的支持
        #TODO:行间分割线
        #text.append(C.config['Text','btwLine'])
        return text

    def feed(self,text:str):
        return self.showInLine(self.kanaify(text))

    def setlinewidth(self,width):
        self.linewidth = width

if __name__ =='__main__':
    conv = conventer(10)
    T = "孟武伯问：“子路仁乎？”子曰：“不知也。”又问，子曰：“由也，千乘之国，可使治其赋也，不知其仁也。”“求也何如？”子曰：“求也，千室之邑、百乘之家，可使为之宰也，不知其仁也。”“赤也何如？”子曰：“赤也，束带立于朝，可使与宾客言也，不知其仁也。”"
    res = conv.feed(T)
    for i in range(3):
        print(res[i])

