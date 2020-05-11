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

def read(base_dir):
    f = open(base_dir, 'r')
    all_sentences = f.read()
    f.close()
    all_sentences = all_sentences.split('\n')
    for index, document in enumerate(all_sentences):
        all_sentences[index] = word_tokenize(document)
    return all_sentences

def word2vec(all_sentences, embedding_path, accuracy_path):
    model = Word2Vec(all_sentences, 
                 min_count=3,   # Ignore words that appear less than this
                 size=300,      # Dimensionality of word embeddings
                 workers=20,     # Number of processors (parallelisation)
                 window=5,      # Context window for words during training
                 iter=30)
    model.save(embedding_path)
    model.wv.save_word2vec_format(embedding_path+".bin",binary=True)
    accuracy = model.accuracy('/home/antonio/lattes/questions-words.txt')
    pandas.DataFrame(accuracy).to_csv(accuracy_path, sep = '|')
    
def main():
    base_dir = sys.argv[1] #'/home/antonio/lattes/titles/all_english.txt'
    embedding_path = sys.argv[2] #'/home/antonio/lattes/embedding/all_titles/embedding'
    #accuracy_path = sys.argv[3] #'/home/antonio/lattes/embedding/all_titles/accuracy.csv'
    all_sentences = read(base_dir)
    word2vec(all_sentences, embedding_path, accuracy_path)

if __name__ == "__main__":
    main()