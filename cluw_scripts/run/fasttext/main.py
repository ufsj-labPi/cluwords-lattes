from script_functions import create_embedding_models, generate_topics
import os
import sys

# wpp_slice_2 11
# wpp_slice 31

# Paths and files paths
MAIN_PATH='/home/antonio/lattes/2.0/fasttext'
# EMBEDDING_RESULTS = 'fasttext_wiki_mahalanobis'
EMBEDDING_RESULTS = sys.argv[2]
PATH_TO_SAVE_RESULTS = '{}/{}/results'.format(MAIN_PATH, EMBEDDING_RESULTS)
PATH_TO_SAVE_MODEL = '{}/{}/datasets/gn_w2v_models'.format(MAIN_PATH, EMBEDDING_RESULTS)
DATASETS_PATH = '/home/antonio/lattes/2.0/data'
# DATASETS_PATH = '/mnt/d/Work/textual_datasets'
CLASS_PATH = ''
HAS_CLASS = False
EMBEDDINGS_FILE_PATH = str(sys.argv[1]).format(MAIN_PATH)
EMBEDDINGS_BIN_TYPE = False
#EMBEDDINGS_FILE_PATH = '{}/wiki-news-300d-1M.vec'.format(MAIN_PATH)
#EMBEDDINGS_FILE_PATH = '{}/wiki-news-300d-sentiment-vocab.vec'.format(MAIN_PATH)
#EMBEDDINGS_BIN_TYPE = False
DATASET = sys.argv[3]
N_THREADS = 15
N_COMPONENTS = 50
# ALGORITHM_TYPE = 'knn_mahalanobis'
ALGORITHM_TYPE = 'knn_cosine'

# Creates directories if they don't exist
try:
    os.mkdir('{}/{}'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/{}/results'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/{}/datasets'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/{}/datasets/gn_w2v_models'.format(MAIN_PATH, EMBEDDING_RESULTS))
except FileExistsError:
    pass

# Create the word2vec models for each dataset
print('Filter embedding space to {} dataset...'.format(DATASET))
n_words = create_embedding_models(dataset=DATASET,
                                  embedding_file_path=EMBEDDINGS_FILE_PATH,
                                  embedding_type=EMBEDDINGS_BIN_TYPE,
                                  datasets_path=DATASETS_PATH,
                                  path_to_save_model=PATH_TO_SAVE_MODEL)


print('Build topics...')
results = generate_topics(dataset=DATASET,
                          word_count=n_words,
                          path_to_save_model=PATH_TO_SAVE_MODEL,
                          datasets_path=DATASETS_PATH,
                          path_to_save_results=PATH_TO_SAVE_RESULTS,
                          n_threads=N_THREADS,
                          algorithm_type=ALGORITHM_TYPE,
                          # k=n_words,
                          k=500,
                          threshold=0.4,
                          cossine_filter=0.9,
                          class_path=CLASS_PATH,
                          has_class=HAS_CLASS,
                          n_components=N_COMPONENTS)
