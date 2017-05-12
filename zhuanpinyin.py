# -*- coding: utf-8 -*-
from pinyin import PinYin
import json

def load(file):
    with open(file) as json_file:
        # json.load可以将文件转化为字典，loads可以将字符串转化为字典
        data = json.load(json_file)
        return data



#这个程序的作用是，读取分好词的结果，转化成拼音
input = load('out.json')
print len(input)

test = PinYin()
test.load_word()
st=[]
for i in input:
    st.append(str(test.hanzi2pinyin(string=i)))

print len(st)

json_dic = json.dumps(st)
fo = open("out_pinyin.json", "wb")
fo.write(json_dic)
# 关闭打开的文件
fo.close()