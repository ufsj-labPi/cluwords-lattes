from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division, absolute_import, print_function
import os
import sys
import re
import numpy as np
import pandas
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.decomposition import IncrementalPCA
from sklearn.manifold import TSNE
import fasttext
import argparse
import errno

def FastText(base_dir, embedding_path):
    model = fasttext.train_unsupervised(base_dir, model='skipgram', minn=2, maxn=15, dim=300, thread=10, minCount=3)
    model.save_model(embedding_path + ".bin")
    words = model.get_words()
    file = open(embedding_path + ".vec", "w")
    file.write(str(len(words)) + " " + str(model.get_dimension()) + '\n')
    for w in words:
        v = model.get_word_vector(w)
        vstr = ""
        for vi in v:
            vstr += " " + str(vi)
        try:
            file.write(w + vstr + '\n')
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass
    file.close()
def main():
    base_dir = sys.argv[1] #'/home/antonio/lattes/titles/all_english.txt'
    embedding_path = sys.argv[2] #'/home/antonio/lattes/embedding/all_titles/embedding'
    #accuracy_path = sys.argv[3] #'/home/antonio/lattes/embedding/all_titles/accuracy.csv'
    FastText(base_dir, embedding_path)

if __name__ == "__main__":
    main()