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


def frequency_previous(txt, words):
    list_of_words = search_word(txt)
    indices = []
    frequency = {}
    for i in list_of_words:
        if i > 0:
            indice_anterior = i - 1
            previous_word = words[indice_anterior]
            indices.append(indice_anterior)
            frequency[previous_word] = frequency.get(previous_word, 0) + 1
    return indices, frequency



"""def frequency_calculation(txt):
    words = text_clean(txt).split()
    word = input("digite a palavra que quer pesquisar: ")
    previous_frequency = {}
    subsequent_frequency = {}

    for i, item in enumerate(words):
        if item == word:
            if i > 0:
                previous_word = words[i - 1]
                previous_frequency[previous_word] = previous_word.get(previous_word, 0) + 1
                print(f"a frequencia dessa palavra é: {previous_frequency}")
            if i < len(words) - 1:
                subsequent_word = words[i + 1]
                subsequent_frequency[subsequent_word] = subsequent_frequency.get(subsequent_word, 0) + 1
                print(f"a frequencia dessa palavra é: {subsequent_frequency}")

    total_previous = sum(previous_frequency.values())
    total_subsequent = sum(subsequent_frequency.values())

    percentage_previous = {word: (freq / total_previous) * 100 for word, freq in previous_frequency.items()}
    percentage_subsequent = {word: (freq / total_subsequent) * 100 for word, freq in subsequent_frequency.items()}

    return percentage_previous, percentage_subsequent
"""

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
    frequency_previous(text, list_words)
