import sys


def txt_importer(path_file: str):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)

        file = open(path_file, 'r')
        content = file.read()
        list_words = content.split('\n')

        return list_words
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
