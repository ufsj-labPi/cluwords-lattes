import os
import string
import re
import pandas as pd
import langid

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def to_lower(text):
    text = [word.lower() for word in text.split()]
    return " ".join(text)

def remove_invalid(text):
    noise_file = open('../noise.txt', 'r')
    noise = noise_file.read()
    text = remove_punctuation(text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.split(' ')
    text2 = ''
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
    return text2

def read_text(file):
    string = ''
    data = pd.read_csv(file,sep='|', encoding='utf-8', engine='python')
    for row in data.iterrows():
        if row[1][4] and row[1][5] == 'Inglês':  
            text = remove_punctuation(row[1][4])
            text = to_lower(text)
            text = remove_invalid(text)
            lang, log_prob = langid.classify(text)
            if lang == 'en':
                string += text + '\n'

    return string

def main():
    csv_file = '/home/antonio/lattes/artigos_22072019.csv'
    txt_dir = '../data/'

    try:
        print("Open: " + str(csv_file))
        string = read_text(csv_file)

    except (RuntimeError, TypeError, NameError):
        print("error in "+ str(csv_file))
        pass
    file_txt = open(txt_dir+'titles_sw.txt', 'w')
    file_txt.write(string)
    file_txt.close()

if __name__ == "__main__":
    main()
