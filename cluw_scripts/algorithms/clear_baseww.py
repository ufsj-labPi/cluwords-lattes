#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from langdetect import detect
from langdetect import detect_langs
import multiprocessing
import sys


def read(base_dir):
    file= open(base_dir, 'r')
    data = file.readlines()
    file.close()
    return data

def clear(data):
    english_list = []
    for line in data:
        try:
            if(detect(line) == 'en'):
                english_list.append(line)
        except:
            pass
    return english_list
        
def worker(data, return_num, return_dict):
    return_dict[return_num] = clear(data)

def main():
    base_dir = sys.argv[1]
    data = read(base_dir)
    n_threads = 20
    n_data = len(data)
    if(n_data%n_threads == 0):
            division = int(len(data)/n_threads)
    else:
        division = int(len(data)/n_threads)+1
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(n_threads):
        init = i*division
        end = (i+1)*division
        p = multiprocessing.Process(target=worker, args=(data[init:end], i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    file = open(sys.argv[2], 'w')
    for value in return_dict.values():
        for line in value:
            file.write(line)
    file.close()
    
if __name__ == "__main__":
    main()