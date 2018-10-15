#!/usr/bin/env python
# coding: utf-8

# In[129]:


import csv
import os
import pandas as pd
from string import punctuation
pd.set_option('max_rows',2000)
pd.set_option('max_colwidth',100)
punctuation += '\"“”‘’—-–'

def list_documents(path): #將待處理的文件以list輸出
    list_txt = []
    list_file = os.listdir(path)
    list_file.remove('stopword.txt')
    for i in list_file:
        if i.find('.txt') != -1:
            list_txt.append(i)
    list_txt.sort()
    n = len(list_txt)
    return list_txt, n #n是文件數量

def kill_punctuations_capitals(text):
    text = text.replace("’s","")
    translator = str.maketrans("","",punctuation) 
    #translator = str.maketrans(punctuation,len(punctuation)*' ') #note:str.maketrans(input,output,delete)
    list_lowercase_without_punctuation = text.lower().translate(translator).split()
    return list_lowercase_without_punctuation
    #將大寫字母轉化為小寫，去除標點，列出單詞

def extract_meaningful(list): 
    list_meaningful_words = []
    with open ('stopword.txt','r') as s:
        list_stop_words = s.read().split() #讀取stoplist
    for m in list:
        if m not in list_stop_words:
            list_meaningful_words.append(m)
    return list_meaningful_words
    
def words_frequency(list):
    dict_words_frequency={}
    for m in list:
        dict_words_frequency[m]=list.count(m)
    return dict_words_frequency

def update_dict(dict0,dict1): #兩個txt中的frequency相加
    for k,v in dict1.items():
        if dict0.__contains__(k):
            dict0[k] += v
        else:
            dict0.update({k : dict1[k]})

def rank_frequency(dict): #根據frequency排序
    dict_frequency_rank={}
    rank = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for m in range(0,len(rank)):
        dict_frequency_rank.update({rank[m][0]:rank[m][1]})
    return dict_frequency_rank

def write_cvs(dict):
    with open('keywords_frequency.csv','w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        header = ['keyword','frequency']
        writer.writerow(header)
        writer.writerows(dict.items())


# In[130]:


path = "./"
list_txt,n = list_documents(path)
dict_accumulative_frequency = {}
dict_list_frequency = {}
for i in list_txt:
    with open(i,'r') as t:
        text = t.read()
    dict_list_frequency[i] = rank_frequency(words_frequency(extract_meaningful(kill_punctuations_capitals(text))))
    update_dict(dict_accumulative_frequency,dict_list_frequency[i])

dict_frequency_rank = rank_frequency(dict_accumulative_frequency)
write_cvs(dict_frequency_rank)
    
print(pd.DataFrame({'keywords in all files':pd.Series(dict_frequency_rank)}).head(15))


# In[131]:


def locate_word(word,text):
    list_paragraphs_contain_word = []
    list_paragraphs_text = text.lower().split('\n')
    while '' in list_paragraphs_text:
        list_paragraphs_text.remove('')
    for i in range(0,len(list_paragraphs_text)):
        if list_paragraphs_text[i].find(word) > -1:
            list_paragraphs_contain_word.append(i)
    return list_paragraphs_contain_word

word = input('you can inpu one word to locate it:')
path = "./"
list_txt, n = list_documents(path)
dict_words_location = {}
for i in list_txt:
    with open(i,'r') as t:
        text = t.read()
    dict_words_location[i] = locate_word(word,text)

data=pd.Series(dict_words_location)
print(pd.DataFrame({'paragraph':data}))

