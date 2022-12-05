from .file_management import txt_importer
import sys



def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    new_file = txt_importer(path_file)
    file_length = len(new_file)
    new_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_length ,
        "linhas_do_arquivo": new_file,
    }
    sys.stdout.write(str(new_data))
    instance.enqueue(new_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
