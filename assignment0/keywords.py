#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os #用於讀取文件列表
import pandas as pd
from string import punctuation
pd.set_option('max_rows',2000)
pd.set_option('max_colwidth',100)
punctuation += '\"“”‘’—-–'

def list_documents(path): #將待處理的文件以list輸出
    list_txt = []
    list_file = os.listdir(path) #讀取目錄下所有文件的路徑
    list_file.remove('stopword.txt')
    for i in list_file:
        if i.find('.txt') != -1: #如果文件是.txt文件
            list_txt.append(i)
    list_txt.sort()
    n = len(list_txt)
    return list_txt, n #n是文件數量


def count_frequency(text):
    def kill_punctuations_capitals(text): 
        text = text.replace("’s","") #需要先去除‘s，否則去除標點會留下如chinas，truups這樣的詞
        translator = str.maketrans("","",punctuation) 
        #等價於translator = str.maketrans(punctuation,len(punctuation)*' ')
        #note:str.maketrans(input,output,delete)，input,output長度必須相等
        list_lowercase_without_punctuation = text.lower().translate(translator).split()
        #將大寫字母轉化為小寫，去除標點，列出單詞
        return list_lowercase_without_punctuation


    def extract_meaningful(list): #去除無意義的單詞
        list_meaningful_words = []
        with open ('stopword.txt','r') as s:
            list_stop_words = s.read().split() #讀取stoplist
        for m in list:
            if m not in list_stop_words:
                list_meaningful_words.append(m)
        return list_meaningful_words

    def words_frequency(list): #統計一篇文章中的frequency
        dict_words_frequency={}
        for m in list:
            dict_words_frequency[m]=list.count(m)
        return dict_words_frequency
    return words_frequency(extract_meaningful(kill_punctuations_capitals(text)))


def update_dict(dict0,dict1): #兩個txt中的frequency相加
    for k,v in dict1.items():
        if dict0.__contains__(k):
            dict0[k] += v
        else:
            dict0.update({k : dict1[k]})

def rank_frequency(dict): #根據frequency排序，也可以最後用print(s.sort_values(ascending=False))，但是不方便寫cvs
    dict_frequency_rank={}
    rank = sorted(dict.items(), key=lambda item: item[1], reverse=True) 
    #將字典轉化爲二元數組，並根據字典中value排序
    for m in range(0,len(rank)):
        dict_frequency_rank.update({rank[m][0]:rank[m][1]})
    #再將字典重新整合起來
    return dict_frequency_rank

def write_cvs_1(dict):
    with open('keywords_frequency.csv','w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        header = ['keyword','frequency']
        writer.writerow(header)
        writer.writerows(dict.items())


path = "./" #在py文件所在根目錄操作
dict_accumulate_frequency = {} #所有文件中的frequency
dict_text_frequency = {} #單個文件中的frequency，方便日後分析每個文件

list_txt,n = list_documents(path) #讀取文件路徑，輸出文件列表
for i in list_txt: #依次讀取
    with open(i,'r') as t: #打開文件
        text = t.read() #讀取文件中的文本
    dict_text_frequency[i] = count_frequency(text) #計數一個文件
    update_dict(dict_accumulate_frequency,dict_text_frequency[i]) #累計到dict_accumulate_frequency
dict_frequency_rank = rank_frequency(dict_accumulate_frequency) #排序

write_cvs_1(dict_frequency_rank)

df = pd.read_csv('keywords_frequency.csv').head(15)
print(df)


def locate_word(word,text):
    list_paragraphs_contain_word = []
    list_paragraphs_text = text.lower().split('\n') #按段落分出列表
    while '' in list_paragraphs_text: 
        list_paragraphs_text.remove('') #去除空段落（由空行造成），確保段數的準確性
    for i in range(0,len(list_paragraphs_text)):
        if list_paragraphs_text[i].find(word) > -1: #如果找到了這個單詞
            list_paragraphs_contain_word.append(i) #把這個段落的序號加入list
    return list_paragraphs_contain_word

def write_cvs_2(word,dict):
    with open('keywords_location.csv','w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        title = 'keyword:'+str(word)
        header = [title,'paragraphs']
        writer.writerow(header)
        writer.writerows(dict.items())

word = input('please input a keyword:')
path = "./"
list_txt, n = list_documents(path)
dict_words_location = {}
for i in list_txt:
    with open(i,'r') as t:
        text = t.read()
    dict_words_location[i] = locate_word(word,text)
write_cvs_2(word,dict_words_location)
df=pd.read_csv('keywords_location.csv')
print(df)

