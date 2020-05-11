#!/bin/bash

embedding_path="/home/antonio/lattes/2.0/fasttext/embeddings/"
embedding="embeddings/"
#embeddings=("titles" "titles_sw" "titles_lem" "all_titles" "all_titles_lem" "wiki")
embeddings=("wiki")
#embeddings=("wiki-news-300d-1M.vec")
#embeddings=('GoogleNews-vectors-negative300.bin')
embedding_file="/embedding.vec"

base=("titles" "titles_sw" "titles_lem" "all_titles" "all_titles_lem")
base_path=("/home/antonio/lattes/2.0/data/")

mkdir -p data
mkdir -p resultados
mkdir -p logs
mkdir -p embeddings

for i in ${base[@]}
do
    mkdir -p $embedding_path$i
    script -c "python3 embeddings.py $base_path$i'.txt' $embedding_path$i/'embedding'" 'logs/'$i'_embedding_log.txt'
done

for i in ${embeddings[@]}
do
    script -c "python3 main.py $embedding$i$embedding_file 'resultados/'$i'_titles' titles" 'logs/'$i"_cluwords_titles_log.txt"
    script -c "python3 main.py $embedding$i$embedding_file 'resultados/'$i'_titles_lem' titles_lem" 'logs/'$i"cluwords_lem_log.txt"
    
done
