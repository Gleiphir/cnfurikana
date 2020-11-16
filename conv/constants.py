#preferences

from dataclasses import dataclass
from enum import Enum
import configparser
import os
def isCNchar(uncchr) -> bool :
    return '\u4e00' <= uncchr <= '\u9fa5'


class display_style(Enum):
    katagana = 0 # default
    pin_yin = 1 #
    hiragana = 2 #
    eng_style = 3 # beta
    kanji = 4 # beta

"""
    “君子引而不发，跃如也。”
    
    katagana カタカナ
    ジュン　ズ　イン　ア　ブ　ファ　ユエ　ル　イエ
    
    hiragana 平仮名
    じゅん　ず　いん　あ　ぶ　ふぁ　ゆえ　る　いえ
    
    pin_yin
    jūn zi yǐn ér bù fā ， yuè rú yě 。 
    
    plain_pin_yin
    eng_style 英語(beta)
    june zu in er boo fah yue roo yeah
    
    kanji style (beta)
    順　ず　いん　あ　ぶ　ふぁ　故　る　家
    
    这里的都是我自己看着写的，实际以https://dokochina.com/fayin.htm为准
    暂不支持台湾地区的BOPOMOFO注音
"""

class ToneMark(Enum):
    std_style = 0 # no marks, as marks are inline with pinyin style
    num_style_follow = 1 # 1,2,3,4
    num_style_above = 2  # 1,2,3,4
    arrow_style = 3
    ascii_style = 4


#5：轻声
style_arrows = [
    "\u3000\u3000",# placeholder
    "→\u3000",
    "↗\u3000",
    "↘↗",
    "↘\u3000",
    "·\u3000"
]

style_ascii = [
    "\u3000",# placeholder
    r"—",
    r"/",
    r"V",
    "\\",
    "·"
]

symb_split = [
    '',
    ' ',
    '~',
    '|',
    '-',
    '\t'
]

@dataclass
class custom_prf:
    display_option:int
    ToneMark:int
    spliter:int




class _conf ( configparser.ConfigParser ):
    def __init__(self):
        super(_conf, self).__init__()
        self.valid = False


    def getVal(self, section, option, *, raw=False, vars=None,
                 fallback=configparser._UNSET, **kwargs):

        if section == 'Intval':
            return super()._get_conv(section, option, int, raw=raw, vars=vars,
                              fallback=fallback, **kwargs)
        elif section == 'Floatval':
            return super()._get_conv(section, option, float, raw=raw, vars=vars,
                              fallback=fallback, **kwargs)
        elif section == 'customFile':
            try:
                with open(
                        os.path.join(
                            os.getcwd(),
                            super()._get_conv(section, option,str, raw=raw, vars=vars,
                                            fallback=fallback, **kwargs))
                        , encoding='utf-8') as F:
                    s = ''.join(F.readlines())
                    return s
            except:
                return ''
        else:
            return super().get(section, option)


    def __getitem__(self, item):
        #print(item)
        if not self.valid:
            return None
        try :
            assert len(item ) ==2
        except AssertionError as e:
            print(e)
        return self.getVal(section=item[0],option=item[1])

    def getDictOf(self,section):
        return dict(self.items(section))

    def load(self,fpath):
        try:
            with open(fpath, encoding='utf-8') as F:
                self.read_file(F)
                self.valid = True
        except FileNotFoundError as eF:
            self.valid = False



class _coustomConfFile():
    def __init__(self):
        super(_coustomConfFile, self).__init__()
        self.valid = False


    def getFullText(self, section, option, *, raw=False, vars=None,
                 fallback=configparser._UNSET, **kwargs):

        if section == 'Intval':
            return super()._get_conv(section, option, int, raw=raw, vars=vars,
                              fallback=fallback, **kwargs)
        elif section == 'Floatval':
            return super()._get_conv(section, option, float, raw=raw, vars=vars,
                              fallback=fallback, **kwargs)
        elif section == 'customFile':
            try:
                print(os.path.join(
                    os.getcwd(),
                    super()._get_conv(section, option, raw=raw, vars=vars,
                                      fallback=fallback, **kwargs)))
                with open(os.path.join(
                        os.getcwd(),
                        super()._get_conv(section, option, raw=raw, vars=vars,
                              fallback=fallback, **kwargs)),encoding='utf-8') as F:
                    s = ''.join(F.readlines())
                    print(s)
                    return s
            except FileNotFoundError as eF:
                print(os.path.join(
                    os.getcwd(),
                    super()._get_conv(section, option, raw=raw, vars=vars,
                                      fallback=fallback, **kwargs)))
                return ''

        else:
            return super().get(section, option)




    def __getitem__(self, item):
        #print(item)
        assert isinstance(item,str)
        if item == 'stylish':
            pass

    def load(self, fpath):
        try:
            with open(fpath, encoding='utf-8') as F:
                self.read_file(F)
                self.valid = True
        except FileNotFoundError as eF:
            self.valid = False

config = _conf()
#config.getSection()
#coustomconf = _coustomConfFile()
#coustomconf(config.getDictOf('customFile'))

assert os.path.isfile(os.path.join(os.getcwd(), "settings/settings.ini"))
config.load(os.path.join(os.getcwd(), "settings/settings.ini"))
#print(config.sections())


# QML selectors: https://doc.qt.io/qt-5/stylesheet-syntax.html#selector-types