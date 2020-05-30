#!/usr/bin/env python
# coding: utf-8


from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

dataset = ['all_titles', 'titles']
lemmatizer = WordNetLemmatizer()

for name in dataset:
    file = open('data/' + name + '.txt', 'r')
    data = file.readlines()
    file.close()
    file = open('data/' + name + 'lem.txt', 'w')
    for line in data:
        text = word_tokenize(line)
        for index, word in enumerate(text):
            text[index] = lemmatizer.lemmatize(word)
        text = ' '.join(text) + '\n'
        file.write(text)
    file.close()
    
    
    
