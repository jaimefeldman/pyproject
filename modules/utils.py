# -*- coding: utf-8 -*-
"""
    modules.utils
    ~~~~~~~~~~~~~

    UTILITARIOS VARIOS.

    :copyright: (c) 2023 by Jaime Feldman.
    :license: MIT, see LICENSE for more details.
"""
import os, shutil
from termcolor import colored

def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
        #if os.path.isdir(dir_name):
        #    fp = open(f"{dir_name}/__init__.py", 'w')
        #    fp.close()
    except:
        print(colored('Fail', 'red'), "]")
        print(colored('Reason:', 'blue'), f"directory \"{dir_name}\" alredy exists.")
        exit(1)

# copia el archivo de licencia elegido y agrega el nombre del autor.
def copy_license(license_name, author, project_name):

    # comprueba que exista el archivo que se quiere copiar.
    if os.path.isdir(f"resources/licenses/{str(license_name).lower}"):
        print(colored('Reason:', 'blue'), f"the license \"{license_name}\" does't exists.")
        exit(1)
    else:
         shutil.copyfile(f"resources/licenses/{license_name.lower()}/LICENSE", f"{project_name}/LICENSE")
         replace_in_file(f"{project_name}/LICENSE", "<author>", author)
         


# remplaza toda ocurrencia en algun archivo.
def replace_in_file(file_path, ocurrence, replace):
        #read input file
        fin = open(file_path, "rt")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace(ocurrence, replace)
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open(file_path, "wt")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()

