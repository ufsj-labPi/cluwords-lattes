#!/bin/bash

data_path="/home/antonio/lattes/titles/"
data=("all_english_stemmerPre" "all_englishPre" "titles_stemPre" "titles_with_swPre" "titlesPre")
data_out="/home/antonio/lattes/google_translate/data/"

embedding_path="/home/antonio/lattes/google_translate/embeddings/"
embedding="embeddings/"
#embeddings=("titles" "titles_with_sw" "titles_stem" "all_english" "all_english_stemmer" "abstracts")
embeddings=("abstracts")
#embeddings=('wiki-news-300d-1M.vec')
embedding_file="/embedding.bin"


base=("titles" "titles_with_sw" "titles_stem" "all_english" "all_english_stemmer")
base_path=("/home/antonio/lattes/google_translate/data/")

mkdir -p data
mkdir -p embeddings
mkdir -p logs
mkdir -p resultados

#for i in ${data[@]}
#do
#    script -c "python3 clear_baseww.py $data_path$i'.txt' $data_out$i'.txt'" 'logs/'$i'_clear_log.txt'
#done

for i in ${base[@]}
do
    mkdir -p $embedding_path$i
    script -c "python3 embeddings.py $base_path$i'Pre.txt' $embedding_path$i/'embedding' $embedding_path$i'/accuracy.csv'" 'logs/'$i'_embedding_log.txt'
done

for i in ${embeddings[@]}
do
    script -c "python3 main.py $embedding$i$embedding_file 'resultados/'$i'_titles' titles" 'logs/'$i"_cluwords_titles_log.txt"
    script -c "python3 main.py $embedding$i$embedding_file 'resultados/'$i'_titles_stem' titles_stem" 'logs/'$i"cluwords_stem_log.txt"
    
done
