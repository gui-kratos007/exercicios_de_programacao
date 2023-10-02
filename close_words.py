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

        print()
        print("Palavras anteriores à que você escolheu e sua frequência de aparições: ")
        print(previous)
        print()
        print("Palavras posteriores à que você escreveu e sua frequência de aparições: ")
        print(subsequent, "\n")

        # Encontra a(s) palavra(s) mais frequente(s)
        previous_word = max(previous, key=lambda k: previous[k])
        subsequent_word = max(subsequent, key=lambda k: subsequent[k])
        # print(previous_word)
        # print(subsequent_word)

        total_itens_previous = sum(previous.values())
        print("Porcentagem da frequencia dos anteriores: \n")
        for item in previous:
            percentage_value = (previous.get(item, 0) / total_itens_previous) * 100
            print(item, "(", percentage_value, "%) \n")
            """for n, item in enumerate(previous):
                if item == l:
                    previous_name = previous[n]
                    print(previous_name, percentage_value, "%")"""

        total_itens_subsequent = sum(subsequent.values())
        print("Porcentagem da frequencia dos posteriores: \n")
        for item in subsequent:
            percentage_value = (subsequent.get(item, 0) / total_itens_subsequent) * 100
            print(item, "(", percentage_value, "%) \n")

        # Verifica se há empate de palavras mais frequentes
        previous_word_tie = [word for word in previous if previous[word] == previous[previous_word]]
        subsequent_word_tie = [word for word in subsequent if subsequent[word] == subsequent[subsequent_word]]
        print('-' * 150)
        print("As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
              "uma é porque estão empatadas na frequencia.")
        print()
        print("Lista das mais frequentes anteriores:")
        print(previous_word_tie)
        print()
        print("Lista das mais frequentes anteriores:")
        print(subsequent_word_tie)
        print()

        if len(previous_word_tie) > 0:
            imediate_previous = desempate(previous_word_tie)
        if len(subsequent_word_tie) > 0:
            imediate_subsequent = desempate(subsequent_word_tie)

        return print(f"{imediate_previous} {word} {imediate_subsequent}")


def desempate(lista):
    # Use a posição de memória da lista como semente
    seed = id(lista)  # Obtém o identificador único da lista como "semente"

    # Use o último dígito do identificador como semente
    seed = int(str(seed)[-1])

    # Calcule um índice "aleatório" usando a semente
    tamanho = len(lista)
    indice = seed % tamanho  # O índice é calculado usando o último dígito do identificador e o tamanho da lista

    # Retorne o item correspondente ao índice
    escolha = lista[indice]  # Retorna o item na lista correspondente ao índice

    return escolha


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
    frequency(text)
