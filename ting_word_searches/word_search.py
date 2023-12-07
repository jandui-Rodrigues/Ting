def exists_word(word, instance):
    result_search = list()

    for index in range(len(instance)):
        search_word_file = dict()
        data_file = instance.search(index)
        phares = data_file['linhas_do_arquivo']
        ocurrences = list()
        index = 1
        for phare in phares:
            if word in phare.lower():
                ocurrences.append({"linha": index})
                search_word_file["palavra"] = word
                search_word_file["arquivo"] = data_file['nome_do_arquivo']
            index += 1
        print(ocurrences)
        if len(ocurrences) != 0:
            search_word_file["ocorrencias"] = ocurrences
            result_search.append(search_word_file)

    return result_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
