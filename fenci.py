# -*- coding: utf-8 -*-
import jieba
import json


#这个程序可以将中文语料库分词，然后保存为json格式
input = open('10.txt','r')
all_the_text = input.read()
input.close()
seg_list = list(jieba.cut(all_the_text)) # 默认是精确模式


json_dic = json.dumps(list(seg_list))
fo = open("out.json", "wb")
fo.write(json_dic)
# 关闭打开的文件
fo.close()
