from script_functions import create_embedding_models, generate_topics
import os
DATASETS = {
    '2017lattes': 78432,
    '2016lattes': 85709,
    '2015lattes': 94285,
    '2014lattes': 94797,
}

# wpp_slice_2 11
# wpp_slice 31

# Paths and files paths
MAIN_PATH='/home/cecilio/Projetos/cluwords-lattes'
EMBEDDING_RESULTS = 'word2vec_lattes'
PATH_TO_SAVE_RESULTS = '{}/clulattes/{}/results'.format(MAIN_PATH, EMBEDDING_RESULTS)
PATH_TO_SAVE_MODEL = '{}/clulattes/{}/datasets/gn_w2v_models'.format(MAIN_PATH, EMBEDDING_RESULTS)
DATASETS_PATH = '{}/data'.format(MAIN_PATH)
CLASS_PATH = ''
HAS_CLASS = False
EMBEDDINGS_FILE_PATH = '{}/models/word2vec.model'.format(DATASETS_PATH)
EMBEDDINGS_BIN_TYPE = True
DATASET = '2017lattes'
N_THREADS = 4
N_COMPONENTS = 7
ALGORITHM_TYPE = 'knn_cosine'

# Creates directories if they don't exist
try:
    os.mkdir('{}/clulattes/{}'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/clulattes/{}/results'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/clulattes/{}/datasets'.format(MAIN_PATH, EMBEDDING_RESULTS))
    os.mkdir('{}/clulattes/{}/datasets/gn_w2v_models'.format(MAIN_PATH, EMBEDDING_RESULTS))
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
