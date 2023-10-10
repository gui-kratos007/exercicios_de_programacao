import random

def get_text(path):
    with open(path, 'r', encoding="utf-8") as file:
        dados = file.read()
        if dados:
            return dados
    return "arquivo vazio"


def text_clean(text):
    """
    Limpa o texto e garante a similaridade das palavras.
    :return text: Texto limpo e corrigido.
    """
    return (text.replace(",", "")
            .replace(".", "")
            .lower()
            )


def get_count(item):
    """
    Obtém o segundo elemento (contagem) de cada itém.

    :param item: Uma tupla ou lista de dois elementos onde o segundo elemento é a contagem.
    :return: A contagem (segundo elemento) do item.
    """
    return item[1]


def search_word(txt):
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)
    if len(lista_de_busca) > 0:
        return lista_de_busca
    return "essa palavra não está no texto"


def print_percentage(dict1, dict2):
    total_itens = sum(dict1.values())
    total_itens2 = sum(dict2.values())
    print('-' * 150)
    print("Palavras anteriores e sua frequencia de aparição: \n")
    for item in dict1:
        percentage_value = (dict1.get(item, 0) / total_itens) * 100
        print(item, "(", percentage_value, "%) \n")
    print('-' * 150)
    print("Palavras posteriores e sua frequencia de aparição: \n")
    for item in dict2:
        percentage_value = (dict2.get(item, 0) / total_itens2) * 100
        print(item, "(", percentage_value, "%) \n")
    return 0


def desempatar(lista):
    escolha = random.choice(lista)
    return escolha


def print_most_commons(lista1, lista2, word):
    if len(lista1) > 1 and len(lista2) > 1:
        immediate_previous = desempatar(lista1)
        immediate_subsequent = desempatar(lista2)
        print("A frase mais comum que pode ser formada é:")
        return f"{immediate_previous} {word} {immediate_subsequent}"
    elif len(lista1) > 1 >= len(lista2):
        immediate_previous = desempatar(lista1)
        immediate_subsequent = lista2[0]
        print("A frase mais comum que pode ser formada é:")
        return f"{immediate_previous} {word} {immediate_subsequent}"
    elif len(lista1) <= 1 < len(lista2):
        immediate_previous = lista1[0]
        immediate_subsequent = desempatar(lista2)
        print("A frase mais comum que pode ser formada é:")
        return f"{immediate_previous} {word} {immediate_subsequent}"
    else:
        print("A frase mais comum que pode ser formada é:")
        return f"{lista1[0]} {word} {lista2[0]}"


#  def print_most_commons_2()


"""def print_most_commons_2(lista3, lista4, **kwargs):
    # print(lista3, lista4, kwargs)
    if len(lista3) > 1 and len(lista4) > 1:
        immediate_previous = desempatar(lista3)
        immediate_subsequent = desempatar(lista4)
        return f"{immediate_previous} {print_most_commons(**kwargs)} {immediate_subsequent}"
    elif len(lista3) > 1 >= len(lista4):
        immediate_previous = desempatar(lista3)
        immediate_subsequent = lista4[0]
        return f"{immediate_previous} {print_most_commons(**kwargs)} {immediate_subsequent}"
    elif len(lista3) <= 1 < len(lista4):
        immediate_previous = lista3[0]
        immediate_subsequent = desempatar(lista4)
        return f"{immediate_previous} {print_most_commons(**kwargs)} {immediate_subsequent}"
    else:
        return f"{lista3[0]} {print_most_commons(**kwargs)} {lista4[0]}" """


def frequency(txt):
    words = text_clean(txt).split()
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    previous = {}
    subsequent = {}

    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)

    if len(lista_de_busca) > 0:
        # Conta a frequencia das palavras anteriores e posteriores
        for j, item in enumerate(words):
            if item == word:
                previous_word = words[j - 1]
                subsequent_word = words[j + 1]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word in previous:
                    previous[previous_word] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    previous[previous_word] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word in subsequent:
                    subsequent[subsequent_word] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    subsequent[subsequent_word] = 1

        print_percentage(previous, subsequent)

        # Encontra a(s) palavra(s) mais frequente(s)
        previous_word = max(previous, key=lambda k: previous[k])
        subsequent_word = max(subsequent, key=lambda k: subsequent[k])
        # print(previous_word)
        # print(subsequent_word)

        # Verifica se há empate de palavras mais frequentes
        previous_word_tie = [word for word in previous if previous[word] == previous[previous_word]]
        subsequent_word_tie = [word for word in subsequent if subsequent[word] == subsequent[subsequent_word]]
        print('-' * 150)
        print("As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
              "uma é porque estão empatadas na frequencia. \n")
        print("Lista das mais frequentes anteriores:")
        print(previous_word_tie, "\n")
        print("Lista das mais frequentes posteriores:")
        print(subsequent_word_tie, "\n")
        print('-' * 150, "\n")

        # desempat = desempatar(subsequent_word_tie)
        # desempa = desempatar(previous_word_tie)
        # print(desempa)
        # print(desempat)

        print(print_most_commons(previous_word_tie, subsequent_word_tie, word), "\n")
    return "A palavra que você buscou não está no documento lido."


def frequency_2(txt):
    words = text_clean(txt).split()
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    previous = {}
    subsequent = {}

    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)

    if len(lista_de_busca) > 0:
        # Conta a frequencia das palavras anteriores e posteriores
        for j, item in enumerate(words):
            if item == word:
                previous_word = words[j - 2]
                subsequent_word = words[j + 2]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word in previous:
                    previous[previous_word] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    previous[previous_word] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word in subsequent:
                    subsequent[subsequent_word] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    subsequent[subsequent_word] = 1

        print_percentage(previous, subsequent)

        # Encontra a(s) palavra(s) mais frequente(s)
        previous_word = max(previous, key=lambda k: previous[k])
        subsequent_word = max(subsequent, key=lambda k: subsequent[k])
        # print(previous_word)
        # print(subsequent_word)

        # Verifica se há empate de palavras mais frequentes
        previous_word_tie = [word for word in previous if previous[word] == previous[previous_word]]
        subsequent_word_tie = [word for word in subsequent if subsequent[word] == subsequent[subsequent_word]]
        print('-' * 150)
        print("As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
              "uma é porque estão empatadas na frequencia. \n")
        print("Lista das mais frequentes anteriores:")
        print(previous_word_tie, "\n")
        print("Lista das mais frequentes posteriores:")
        print(subsequent_word_tie, "\n")
        print('-' * 150, "\n")

        print(print_most_commons(previous_word_tie, subsequent_word_tie, word), "\n")
    return "A palavra que você buscou não está no documento lido."


"""def frequency_2(txt):
    words = text_clean(txt).split()
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    previous_1 = {}
    previous_2 = {}
    subsequent_1 = {}
    subsequent_2 = {}

    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)

    if len(lista_de_busca) > 0:
        # Conta a frequencia das 2 palavras anteriores e das 2 posteriores
        for j, item in enumerate(words):
            if item == word:
                previous_word_1 = words[j - 1]
                previous_word_2 = words[j - 2]
                subsequent_word_1 = words[j + 1]
                subsequent_word_2 = words[j + 2]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word_1 in previous_1:
                    previous_1[previous_word_1] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    previous_1[previous_word_1] = 1

                if previous_word_2 in previous_2:
                    previous_2[previous_word_2] += 1
                else:
                    previous_2[previous_word_2] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word_1 in subsequent_1:
                    subsequent_1[subsequent_word_1] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    subsequent_1[subsequent_word_1] = 1

                if subsequent_word_2 in subsequent_2:
                    subsequent_2[subsequent_word_2] += 1
                else:
                    subsequent_2[subsequent_word_2] = 1

        print("\nPalavras anteriores em uma casa à que você escreveu e sua frequência de aparições: ")
        print(previous_1)
        print("\nPalavras anteriores em duas casas à que você escreveu e sua frequência de aparições: ")
        print(previous_2)
        print("\nPalavras posteriores em uma casa à que você escreveu e sua frequência de aparições: ")
        print(subsequent_1)
        print("\nPalavras posteriores em duas casas à que você escreveu e sua frequência de aparições: ")
        print(subsequent_1, "\n")

        print("porcentagem das palavras de uma casa de diferença:")
        print_percentage(previous_1, subsequent_1)

        print("porcentagem das palavras de duas casas de diferença:")
        print_percentage(previous_2, subsequent_2)

        # Encontra a(s) palavra(s) mais frequente(s)
        previous_word_1 = max(previous_1, key=lambda k: previous_1[k])
        previous_word_2 = max(previous_2, key=lambda k: previous_2[k])
        subsequent_word_1 = max(subsequent_1, key=lambda k: subsequent_1[k])
        subsequent_word_2 = max(subsequent_2, key=lambda k: subsequent_2[k])
        # print(previous_word)
        # print(subsequent_word)

        # Verifica se há empate de palavras mais frequentes
        previous_word_tie_1 = [word for word in previous_1 if previous_1[word] == previous_1[previous_word_1]]
        previous_word_tie_2 = [word for word in previous_2 if previous_2[word] == previous_2[previous_word_2]]
        subsequent_word_tie_1 = [word for word in subsequent_1 if subsequent_1[word] == subsequent_1[subsequent_word_1]]
        subsequent_word_tie_2 = [word for word in subsequent_2 if subsequent_2[word] == subsequent_2[subsequent_word_2]]
        print('-' * 150)
        print(
            "As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
            "uma é porque estão empatadas na frequencia.")
        print()
        print("Lista das mais frequentes de uma casa anterior:")
        print(previous_word_tie_1)
        print()
        print("Lista das mais frequentes de duas casas anteriores:")
        print(previous_word_tie_2)
        print()
        print("Lista das mais frequentes de uma casa posterior:")
        print(subsequent_word_tie_1)
        print()
        print("Lista das mais frequentes de duas casas posteriores:")
        print(subsequent_word_tie_2)
        print()
        print('-' * 150)
        print()

        # desempat = desempatar(subsequent_word_tie)
        # desempa = desempatar(previous_word_tie)
        # print(desempa)
        # print(desempat)

        print("A frase mais provável que poderá se formar de acordo com a frequência das anteriores e posteriores é:")
        params = {"lista1": previous_word_tie_1, "lista2": subsequent_word_tie_1, "word": word}
        print(print_most_commons_2(previous_word_tie_2, subsequent_word_tie_2, **params))
        print()
    return "A palavra que você buscou não está no documento lido." """


if __name__ == "__main__":
    path = input("Entre com o path do arquivo que deseja processar: ")
    text = get_text(path)

    # print(text.split()[7:22])

    # Divide a string em palavras
    list_words = text_clean(text).split()
    # print(set(list_words))

    # Cria um lista de listas para contar as palavras
    words_count = [[word, list_words.count(word)] for word in set(list_words)]
    # print(words_count)

    # Ordena as palavras em ordem decrescente de contagem sem lambda
    order_words = sorted(words_count, key=get_count, reverse=True)
    # print(order_words)

    # Imprime as palavras e as suas contagens em ordem decrescente
    for word, count in order_words:
        print(f"{word} ({count})")

    # busca os índices das palavras iguais as escolhidas pelo usuário
    busca = search_word(text)
    # imprime os índices das palavras iguais as escolhidas pelo usuário
    print(busca)

    # frequency_calculation(text)
    frequency_2(text)
