#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import multiprocessing
import os
import pandas as pd
import string
import re

import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold
from nltk.corpus import stopwords
from langdetect import detect


# In[ ]:


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


# In[ ]:


def remove_stopwords(text, sw):
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    return " ".join(text)


# In[ ]:


def remove_invalid(text):
    text = re.sub('[^A-Z a-z]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
    return text


# In[ ]:


def worker(data, sw, return_num, return_dict):
    lines = []
    for line in data:
        try:
            if(detect(line) == 'en'): 
                text = remove_punctuation(line)
                text = remove_stopwords(text, sw)
                text = remove_invalid(text)
                lines.append(text + '\n')
        except:
            pass
    return_dict[return_num] = lines


# In[ ]:


def main():
    file = open('titles/base_titulos.txt', 'r')
    data = file.readlines()
    file.close()
    n_threads = 6
    n_data = len(data)
    if(n_data%n_threads == 0):
        division = int(len(data)/n_threads)
    else:
        division = int(len(data)/n_threads)+1
    file.close()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    sw = stopwords.words('english')
    for i in range(n_threads):
        init = i*division
        end = (i+1)*division-1
        p = multiprocessing.Process(target=worker, args=(data[init:end], sw, i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    file = open('titles/base_english.txt', 'w')
    for value in return_dict.values():
        for line in value:
            file.write(line)
    file.close()

if __name__ == ‘__main__’:
    main()


# In[ ]:




