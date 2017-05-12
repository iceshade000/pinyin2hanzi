# -*- coding: utf-8 -*-
import json

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

def dfs(input,a):
    a.append(input[0])
    return freq,result

#加载数据
zhongwen=load('out.json')
pinyin=load('out_pinyin.json')
dict_zhongwen=load('dict_zhongwen.json')
dict_pinyin=load('dict_pinyin.json')
tf=load('tf.json')
bi_zhongwen=load('bi_zhongwen.json')
bi_pinyin=load('bi_pinyin.json')

#读入拼音，这里就直接用字符串了
input='yi jia gang gang cheng li liang nian de wang luo zhi fu gong si'

input=input.split(' ')

length=len(input)

a=[]
a.append('bao')
a.append('zheng')
print tf[dict_pinyin[str(a)][0]]

#采用枚举法求出最大概率的拼音分词,写一个深度优先搜索

freq,result = dfs(input,n)





