def exists_word(word, instance):
    to_lower_word = word.lower()
    words_found = list()
    evidence = list()
    for item in instance.line:
        repeated_word = 0
        for text in item['linhas_do_arquivo']:
            repeated_word += 1
            if to_lower_word in text.lower():
                evidence.append({"linha": repeated_word})
        if len(evidence) == 0:
            return evidence
        res = {
            "palavra": word.lower(),
            "arquivo": item['nome_do_arquivo'],
            "ocorrencias": evidence
        }
        words_found.append(res)
    return words_found


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
