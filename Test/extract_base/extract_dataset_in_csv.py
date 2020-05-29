import os
import string
import re
import pandas as pd
import langid
from nltk.corpus import stopwords

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def to_lower(text):
    text = [word.lower() for word in text.split()]
    return " ".join(text)

def remove_stopwords(text, sw):
    text = [word for word in text.split() if word not in sw]
    return " ".join(text)

def remove_invalid(text, sw):
    
    noise_file = open('../noise.txt', 'r')
    noise = noise_file.read()
    
    text = remove_punctuation(text)
    text = to_lower(text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
    text_no_sw = remove_stopwords(text, sw)
    
    text = text.split(' ')
    text_no_sw = text_no_sw.split(' ')
    
    text2 = ''
    text3 = ''
    
    for index, word in enumerate(text):
        if(len(word) < 2 or len(word) > 16):
            text.pop(index)
        elif word in noise:
            text.pop(index)
        elif re.search('\d+', word):
            text.pop(index)
    for word in text:
        text2 += word + ' '
    text2 = text2[:-1]
    
    for index, word in enumerate(text_no_sw):
        if(len(word) < 2 or len(word) > 16):
            text_no_sw.pop(index)
        elif word in noise:
            text_no_sw.pop(index)
        elif re.search('\d+', word):
            text_no_sw.pop(index)
    for word in text_no_sw:
        text3 += word + ' '
    text3 = text3[:-1]
    
    return text2, text3

def read_text(file, sw):
    data_sw = []
    data_text = []
    data = pd.read_csv(file,sep='|', encoding='utf-8', engine='python')
    for row in data.iterrows():
        if row[1][4] and row[1][5] == 'Inglês':  
            text, text_no_sw = remove_invalid(row[1][4], sw)
            data_sw.append(text)
            data_text.append(text_no_sw)
    return data_sw, data_text

def main():
    csv_file = '/home/antonio/lattes/artigos_22072019.csv'
    txt_dir = '../data/'

    sw_path = os.path.abspath("../stopwords.txt")
    sw = stopwords.words(sw_path)
    
    try:
        print("Open: " + str(csv_file))
        docs, docs_no_sw = read_text(csv_file, sw)

    except (RuntimeError, TypeError, NameError):
        print("error in "+ str(csv_file))
        pass
    
    data = ''
    for document in docs:
        lang, log_prob = langid.classify(document)
        if lang == 'en':
            data += document + '\n'
    
    file_txt = open(txt_dir+'titles_sw.txt', 'w')
    file_txt.write(data)
    file_txt.close()
    
    data = ''
    for document in docs_no_sw:
        lang, log_prob = langid.classify(document)
        if lang == 'en':
            data += document + '\n'
    
    file_txt = open(txt_dir+'titles.txt', 'w')
    file_txt.write(data)
    file_txt.close()
    
    

if __name__ == "__main__":
    main()
