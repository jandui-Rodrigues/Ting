from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    text_data = txt_importer(path_file)
    for index in range(len(instance)):
        data_file = instance.search(index)
        if data_file['nome_do_arquivo'] == path_file:
            return
    data = dict()
    data['nome_do_arquivo'] = path_file
    data['qtd_linhas'] = len(text_data)
    data["linhas_do_arquivo"] = text_data
    instance.enqueue(data)
    print(data, file=sys.stdout)

    return data


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)
    data_remove = instance.dequeue()
    path_file = data_remove['nome_do_arquivo']
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
        return data
    except IndexError:
        print("Posição inválida", file=sys.stderr)
