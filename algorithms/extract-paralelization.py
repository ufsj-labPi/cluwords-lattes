import os
import xml.etree.ElementTree as ET
import lxml.etree as etree
import multiprocessing

def read_file(path):
    tree =  ET.parse(path + '/curriculo.xml')
    root = tree.getroot()
    title_class = root.find('PRODUCAO-BIBLIOGRAFICA')
    if title_class:
        title_class = title_class.find('ARTIGOS-PUBLICADOS')
    text = ''
    if title_class:
        for element in title_class.findall('ARTIGO-PUBLICADO'):
            if element:
                value = element.find('DADOS-BASICOS-DO-ARTIGO')
                if(value.attrib['IDIOMA'] == 'Inglês'):
                    text += value.attrib['TITULO-DO-ARTIGO'] + '\n'
    return text

def worker(base_dir, files, return_num, return_dict):
    text = ''
    for file in files:
        text += read_file(file)
    return_dict[return_num] = text

def main():
    text = ''
    files_list = []
    base_dir = '/home/antonio/lattes-base/Collection'
    for folder in os.listdir(base_dir):
        path = os.path.join(base_dir, folder)
        if(os.path.isdir(path) == True and not folder.startswith('.')):
            for files in os.listdir(path):
                if not files.startswith('.'):
                    file = os.path.join(path, files)
                    files_list.append(file)
    n_threads = 10
    n_data = len(files_list)
    if(n_data%n_threads == 0):
            division = int(n_data/n_threads)
    else:
        division = int(n_data/n_threads)+1
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(n_threads):
        init = i*division
        end = (i+1)*division
        p = multiprocessing.Process(target=worker, args=(base_dir, files_list[init:end], i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    file = open('titles/base_titulos_english.txt', 'w')
    for value in return_dict.values():
        for line in value:
            file.write(line)
    file.close()

    
if __name__ == "__main__":
    main()