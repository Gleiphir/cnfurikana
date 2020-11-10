from pypinyin import pinyin, lazy_pinyin, Style
print()



if __name__ == '__main__':
    print(lazy_pinyin('君子引而不发，跃如也。', style=Style.TONE3, neutral_tone_with_five=True,errors=lambda x : (x,)))
    print(pinyin('君子引而不发，跃如也。', style=Style.TONE3, neutral_tone_with_five=True,errors=lambda x : (x,)))
    print(''.join([x[0]+' ' for x in pinyin('君子引而不发，跃如也。', neutral_tone_with_five=True) ]))

    pinyin('君子引而不发，跃如也。',)
    print("\\")