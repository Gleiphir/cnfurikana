import json
import re

defaultText = ' '

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


class localePkg:
    def __init__(self,JSONfile):
        pass#self.