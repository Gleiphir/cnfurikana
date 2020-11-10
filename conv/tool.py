from pypinyin import pinyin, lazy_pinyin,Style
from conv.constants import isCNchar
import json
if __name__ =='__main__':
    with open(r'D:\Github\cnfurikana\conv\allpronunce.txt',encoding='utf-8') as F:
        L = [ c for c in F.read() if isCNchar(c) ]
        print(len(L))
        T = ''.join(L)
        for i in range(5):
            print(T[i*100 : i*100 +100])

    with open(r'D:\Github\cnfurikana\conv\kanalist0.txt',encoding='utf-8') as F:
        Ls = [ l for l in F.readlines() ]
        for l in Ls:
            if len(l.strip()) ==0 :Ls.remove(l)
            else:print(len(l.strip()),l)
        with open(r'D:\Github\cnfurikana\conv\kanalist.txt','w', encoding='utf-8') as f:
            f.writelines(Ls)

    with open(r'D:\Github\cnfurikana\conv\kanalist0.txt', encoding='utf-8') as F:
        dic = {}
        Ls = [l for l in F.readlines()]
        for ind,l in enumerate(Ls):
            if isCNchar(l[0]):
                dic [lazy_pinyin(l[0], style=Style.NORMAL, neutral_tone_with_five=True)[0]] = list(set(Ls[ind-2].strip().split('/')))
        dic['den'] = dic['deng'].copy()
        for key in dic:
            if len(dic[key]) > 1:
                print(key,dic[key])
        #手动去多音
        del dic['can'][1]
        del dic['ga'][0]
        del dic['ga'][1]
        del dic['chuo'][0]
        del dic['hai'][1]
        del dic['le'][1]
        del dic['mo'][0]
        del dic['o'][1]
        #del dic['zha'][0]
        del dic['zhuai'][0]
        dic['di'] = "ディ"
        #########
        for key in dic:
            pass#print(key,dic[key])

        with open(r'D:\Github\cnfurikana\conv\table.json','w', encoding='utf-8') as of:
            json.dump(dic,of)

    with open(r'D:\Github\cnfurikana\conv\table.json', encoding='utf-8') as of:
        print(json.load(of))