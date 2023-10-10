import random


def menu():
    while True:
        print("-" * 150)
        print("Menu interativo")
        print("-" * 150)
        print()
        print("Opções: ")
        print("[1] -> Carregar arquivo")
        print("[2] -> Exibir lista")
        print("[3] -> Buscar palavra")
        print("[4] -> Buscar palavras próximas mais frequetes")
        print("[9] -> Sair")

        try:
            answer = int(input("Digite sua opção: "))
            if answer == 1:
                path = input("Entre com o path do arquivo que deseja processar: ")
                text = get_text(path)
                print()
                print("O arquivo foi carregado, veja abaixo o seu conteúdo: ")
                print(text)
                print()
            elif answer == 2:
                path = input("Entre com o path do arquivo que deseja processar: ")
                text = get_text(path)
                list_words = text_clean(text).split()
                print()
                print(list_words)
                print()
                print("-" * 5, "Escolha uma opção para interagir com essa lista", "-" * 5)
                print("Opções:")
                print("[1] -> Ordenar por palavras mais frequentes")
                print("[2] -> Ordenar por palavras menos frequentes")
                print("[3] -> Ordem alfabética (crescente)")
                print("[4] -> Ordem alfabética (decrescente)")
                print("[5] -> Voltar ao Menu principal")
                print("[6] -> Sair")

                option = int(input("Digite sua opção: "))
                print()
                if option == 1:
                    words_count = [[word, list_words.count(word)] for word in set(list_words)]
                    order_words = sorted(words_count, key=get_count, reverse=True)
                    for word, count in order_words:
                        print(f"{word} ({count})")
                elif option == 2:
                    words_count = [[word, list_words.count(word)] for word in set(list_words)]
                    order_words = sorted(words_count, key=get_count)
                    for word, count in order_words:
                        print(f"{word} ({count})")
                elif option == 3:
                    ordem_alfabetica_crescente = ascending_alphabetical_order(list_words)
                    print(ordem_alfabetica_crescente)
                elif option == 4:
                    ordem_alfabetica_decrescente = descending_alphabetical_order(list_words)
                    print(ordem_alfabetica_decrescente)
                elif option == 5:
                    continue
                elif option == 6:
                    print("Programa finalizado!")
                    break
                else:
                    print("Opção inválida. Volte do ínicio e tente novamente com um número válido.")
                print()
            elif answer == 3:
                path = input("Entre com o path do arquivo que deseja processar: ")
                text = get_text(path)
                search = search_word(text)
                print()
                print(search)
                print()
            elif answer == 4:
                path = input("Entre com o path do arquivo que deseja processar: ")
                text = get_text(path)
                show_all(text)
            elif answer == 9:
                print("Programa finalizado!")
                break
            else:
                print("Número inválido, tente novamente inserindo um válido.")
        except ValueError:
            print("Você não digitou um número inteiro, tente novamente.")


def get_text(path):
    """
    Esta função lê o arquivo e retorna o seu conteúdo, mas caso não exista ele retorna uma mensagem de erro.
    :param path: caminho ou path para o documento a ser lido
    :return: mensagem de erro
    """
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
    Obtém o segundo elemento (contagem) de cada item.

    :param item: Uma tupla ou lista de dois elementos onde o segundo elemento é a contagem.
    :return: A contagem (segundo elemento) do item.
    """
    return item[1]


def search_word(txt):
    """
    Pesquisa a palavra escolhida pelo usuário e retorna uma lista com os indices de todas
    as aparições dessa palavra no texto
    :param txt: texto do documento
    :return: mensagem de erro
    """
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)
    if len(lista_de_busca) > 0:
        return lista_de_busca
    return "essa palavra não está no texto"


def ascending_alphabetical_order(list_words):
    """
    ordena as palavras em ordem alfabética crescente
    :param list_words: lista de palavras do texto
    :return: as palavras ordenadas em ordem alfabética crescente
    """
    word_sorted = [word for word in set(list_words)]
    return sorted(word_sorted)


def descending_alphabetical_order(list_words):
    """
        ordena as palavras em ordem alfabética decrescente
        :param list_words: lista de palavras do texto
        :return: as palavras ordenadas em ordem alfabética decrescente
        """
    word_sorted = [word for word in set(list_words)]
    return sorted(word_sorted, reverse=True)


def print_percentage(dict1, dict2):
    """
    imprime as porcentagens de aparições das palavras de cada dict
    :param dict1: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :param dict2: dicionário das palavras que aparecem depois da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    total_itens = sum(dict1.values())
    total_itens2 = sum(dict2.values())
    print('-' * 150)
    print("Porcentagem da frequencia dos anteriores: \n")
    for item in dict1:
        ocurrences = dict1.get(item, 0)
        percentage_value = (ocurrences / total_itens) * 100
        print(item, "(", percentage_value, "%) \n")
    print('-' * 150)
    print("Porcentagem da frequencia dos posteriores: \n")
    for item in dict2:
        ocurrences = dict2.get(item, 0)
        percentage_value = (ocurrences / total_itens2) * 100
        print(item, "(", percentage_value, "%) \n")
    return 0


def desempatar(lista):
    """
    escolhe um item aleatório da lista
    :param lista: lista de palavras a serem sorteadas
    :return: a escolha, ou seja, o item que foi sorteado
    """
    escolha = random.choice(lista)
    return escolha


"""def print_most_commons(lista1, lista2, word):
    ""
    imprime a frase mais provável
    :param lista1: lista das anteriores mais freuquentes
    :param lista2: lista das posteriores mais freuquentes
    :param word: palavra escolhida pelo usuário
    :return: frase mais provável
    ""
    print("A frase mais provável é: ")
    if len(lista1) > 1 and len(lista2) > 1:
        immediate_previous = desempatar(lista1)
        immediate_subsequent = desempatar(lista2)
        return f"{immediate_previous} {word} {immediate_subsequent}"
    elif len(lista1) > 1 >= len(lista2):
        immediate_previous = desempatar(lista1)
        immediate_subsequent = lista2[0]
        return f"{immediate_previous} {word} {immediate_subsequent}"
    elif len(lista1) <= 1 < len(lista2):
        immediate_previous = lista1[0]
        immediate_subsequent = desempatar(lista2)
        return f"{immediate_previous} {word} {immediate_subsequent}"
    else:
        return f"{lista1[0]} {word} {lista2[0]}" """


def check_tie(dict1, dict2, lista):
    """
    Encontra as palavras mais frequentes e ve se tem empate de aparições
    :param dict1: dict das palavras anteriores
    :param dict2: dict das palavras posteriores
    :return: mensagem de erro
    """
    # Encontra a(s) palavra(s) mais frequente(s)
    previous_word = max(dict1, key=lambda k: dict1[k])
    subsequent_word = max(dict2, key=lambda k: dict2[k])

    # Verifica se há empate de palavras mais frequentes
    previous_word_tie = [word for word in dict1 if dict1[word] == dict1[previous_word]]
    subsequent_word_tie = [word for word in dict2 if dict2[word] == dict2[subsequent_word]]
    if len(lista) > 0:
        print('-' * 150)
        print("As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
              "uma é porque estão empatadas na frequencia.\n")
        print("Lista das mais frequentes anteriores:")
        print(previous_word_tie, "\n")
        print("Lista das mais frequentes posteriores:")
        print(subsequent_word_tie, "\n")
        print('-' * 150, "\n")
    return "não tem nenhuma palavra nas listas"


def frequency(dict1, dict2, lista):
    """
    Imprime a frequencia de aparições no texto das palavras anteriores e posteriores à escolhida pelo usuário
    :param dict1: dict de palavras anteriores à escolhida pelo usuário
    :param dict2: dict de palavras posteriores à escolhida pelo usuário
    :param lista: lista de indices da palavra escolhida pelo usuário
    :return: mensagem de erro
    """

    if len(lista) > 0:
        print("\nPalavras anteriores à que você escolheu e sua frequência de aparições: ")
        print(dict1)
        print("\nPalavras posteriores à que você escreveu e sua frequência de aparições: ")
        print(dict2, "\n")
    return "não tem palavras nas listas"


def show_all(txt):
    """
    Calcula a frequencia de aparições das palavras
    :param txt: texto do documento
    :return: mensagem de erro
    """
    words = text_clean(txt).split()
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    previous = {}
    subsequent = {}

    for i, item in enumerate(words):
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

    frequency(previous, subsequent, lista_de_busca)
    print_percentage(previous, subsequent)
    check_tie(previous, subsequent, lista_de_busca)
    return "A palavra que você buscou não está no documento lido."


menu()
