# -*- coding: utf-8 -*-
import json
import math

def load(file):
    with open(file) as json_file:
        # json.load可以将文件转化为字典，loads可以将字符串转化为字典
        data = json.load(json_file)
        return data

def save(file,st):
    json_dic = json.dumps(st)
    fo = open(file, "wb")
    fo.write(json_dic)
    # 关闭打开的文件
    fo.close()


#本程序的目的是得到二元统计概率
zhongwen=load('out.json')
pinyin=load('out_pinyin.json')

dict_zhongwen=load('dict_zhongwen.json')#使用中文词的位置作为该词的代号
dict_pinyin=load('dict_pinyin.json')#使用拼音的第一位中文词的代码作为代号

bi_zhongwen={}
bi_pinyin={}
#由于要建立索引，因此这里使用元组来表示对
#元组(a,b)表示前面为a后面为b出现的次数
pre=-1
for i in zhongwen:
    if pre==-1:
        pre=dict_zhongwen[i]
    else:
        now=dict_zhongwen[i]
        t=(pre,now)
        a=str(t)
        if bi_zhongwen.has_key(a):
            bi_zhongwen[a]=bi_zhongwen[a]+1
        else:
            bi_zhongwen[a]=1
        pre=now


pre=-1
for i in pinyin:
    if pre==-1:
        pre=dict_pinyin[i][0]
    else:
        now=dict_pinyin[i][0]
        t = (pre, now)
        a = str(t)
        if bi_pinyin.has_key(a):
            bi_pinyin[a]=bi_pinyin[a]+1
        else:
            bi_pinyin[a]=1
        pre=now

for i in bi_pinyin.keys():
    bi_pinyin[i]=math.log(bi_pinyin[i])+1

for i in bi_zhongwen.keys():
    bi_zhongwen[i]=math.log(bi_zhongwen[i])+1
save('bi_zhongwen.json',bi_zhongwen)
save('bi_pinyin.json',bi_pinyin)






