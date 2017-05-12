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

zhongwen=load('out.json')
pinyin=load('out_pinyin.json')


length=len(zhongwen)

list_zhongwen=[]#中文词表
tf=[]#对应词频
dict_zhongwen={}#记录词的位置
dict_pinyin={}#记录拼音对应的词的位置

num=0

for i in range(0,length):
    if dict_zhongwen.has_key(zhongwen[i]):
        #计数词频
        tf[dict_zhongwen[zhongwen[i]]] = tf[dict_zhongwen[zhongwen[i]]]+1
    else:
        #添加到中文词表中
        list_zhongwen.append(zhongwen[i])
        tf.append(1)
        dict_zhongwen[zhongwen[i]]=num

        if dict_pinyin.has_key(pinyin[i]):
            dict_pinyin[pinyin[i]].append(num)
        else:
            dict_pinyin[pinyin[i]] = [num]

        num = num + 1

print dict_pinyin
for i in tf:
    i=math.log(i)+1
save('list_zhongwen.json',list_zhongwen)
save('tf.json',tf)
save('dict_zhongwen.json',dict_zhongwen)
save('dict_pinyin.json',dict_pinyin)
