#!/bin/bash
for folder in *
do
    for f in $folder/*.zip
    do 
        unzip -d "${f%*.zip}" "$f"
    done
    rm $folder/*.zip
    
done