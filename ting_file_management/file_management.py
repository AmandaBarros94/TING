import sys


def txt_importer(path_file):
    new_file = path_file.endswith('txt')
    if not new_file:
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, mode="r") as data:
            new_list = data.read().split('\n')
            return new_list
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
