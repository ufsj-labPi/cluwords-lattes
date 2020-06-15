import os
import sys
import glob
import zipfile

BASE_DIR = '/home/pablo/base-lattes/Collection'

files_list = glob.glob("{}/*/*.zip".format(BASE_DIR))

n_files = len(files_list)
print('Arquivos ZIP Lattes: {}'.format(n_files))

for idx, file in enumerate(files_list):
    
    path = file[0:38]
    
    with zipfile.ZipFile(file) as zf:
        zf.extractall(path)
        os.rename(path + 'curriculo.xml', path + file[38:-4] + '.xml')
        os.remove(file)

    print('Processando... {:.2f}%'.format(idx * 100 / n_files))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line