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
            path = input("Entre com o path do arquivo que deseja processar: ")
            if answer == 1:
                answer_1(path)
            elif answer == 2:
                list_the_words(path)

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
                    option_1(list_the_words(path))
                elif option == 2:
                    option_2(list_the_words(path))
                elif option == 3:
                    option_3(list_the_words(path))
                elif option == 4:
                    option_4(list_the_words(path))
                elif option == 5:
                    continue
                elif option == 6:
                    print("Programa finalizado!")
                    break
                else:
                    print("Opção inválida. Volte do ínicio e tente novamente com um número válido.")
                print()
            elif answer == 3:
                answer_3(path)
            elif answer == 4:
                text = get_text(path)
                print("Escolha uma opção:\n")
                print("[1] -> Ver frequencia das palavras e frase mais provável")
                print("[2] -> Voltar ao menu principal")
                print("[3] -> Sair\n")

                option = int(input("Digite a sua opção: "))

                if option == 1:
                    show_all(text)
                elif option == 2:
                    continue
                elif option == 3:
                    print("Programa finalizado!")
                    break
                else:
                    print("Opção inválida. Volte do ínicio e tente novamente com um número válido.")
            elif answer == 9:
                print("Programa finalizado!")
                break
            else:
                print("Número inválido, tente novamente inserindo um válido.")
        except ValueError:
            print("Você não digitou um número inteiro, tente novamente.")


def answer_1(path):
    """
    lê o arquivo e retorna o conteúdo dele
    :param path: caminho do arquivo
    :return: conteúdo do arquivo
    """
    text = get_text(path)
    print("\n O arquivo foi carregado, veja abaixo o seu conteúdo: ")
    return print(text)


def option_1(func):
    """
    cria uma lista de palavras com o seu numero de aparições, as ordena e retorna elas ordenadas em ordem decrescente
    :param func: função da lista de palavras
    :return: palavras seguidas da sua quantidade de aparições em ordem decrescente de aparições.
    """
    words_count = [[word, func.count(word)] for word in set(func)]
    order_words = sorted(words_count, key=get_count, reverse=True)
    for word, count in order_words:
        print(f"{word} ({count})")


def option_2(func):
    """
    cria uma lista de palavras com o seu numero de aparições, as ordena e retorna elas ordenadas em ordem crescente
    :param func: função da lista de palavras
    :return: palavras seguidas da sua quantidade de aparições em ordem crescente de aparições.
    """
    words_count = [[word, func.count(word)] for word in set(func)]
    order_words = sorted(words_count, key=get_count)
    for word, count in order_words:
        print(f"{word} ({count})")


def option_3(func):
    """
    coloca a lista de palavras em ordem alfabética crescente e retorna a impressão delas
    :param func: lista de palavras
    :return: lista de palavras em ordem alfabética crescente
    """
    ordem_alfabetica_crescente = ascending_alphabetical_order(func)
    return print(ordem_alfabetica_crescente)


def option_4(func):
    """
    coloca a lista de palavras em ordem alfabética decrescente e retorna a impressão delas
    :param func: lista de palavras
    :return: lista de palavras em ordem alfabética decrescente
    """
    ordem_alfabetica_decrescente = descending_alphabetical_order(func)
    return print(ordem_alfabetica_decrescente)


def answer_3(path):
    """
    faz uma pesquisa da palavra que o usuário escolher e retorna o(s) índice(s) que ela aparece no texto
    :param path: caminho do arquivo
    :return: indice(s) da palavra escolhida
    """
    text = get_text(path)
    search = search_word(text)
    return print("\n", search, "\n")


def list_the_words(path):
    """
    lê o texto e retorna a lista de palavras dele
    :param path: caminho do arquivo
    :return: lista de palavras do texro
    """
    text = get_text(path)
    list_words = text_clean(text).split()
    return list_words


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
    Ordena as palavras em ordem alfabética crescente
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


def calculate_percentage(ocurrences, total):
    """
    Uma fórmula para calcular porcentagem
    :param ocurrences: total de ocorrencias de um certo valor no meio de outros
    :param total: total de valores possíveis
    :return: retorna o valor calculado da porcentagem
    """
    percentage_value = (ocurrences / total) * 100
    return percentage_value


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
        percentage_value = calculate_percentage(ocurrences, total_itens)
        print(item, "(", percentage_value, "%) \n")
    print('-' * 150)
    print("Porcentagem da frequencia dos posteriores: \n")
    for item in dict2:
        ocurrences = dict2.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens2)
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


def print_phrase(frase, words):
    """
    Essa função imprime as frases mais provaveis de acordo com a frequencia das palavras. O usuário pode continuar
    o programa e formar frases maiores de acordo com a sua vontade
    :param frase: frase que foi formada anteiormente, quando o usuário digitou a palavra que ele quis
    :param words: todas as palavras presentes no texto
    :return: Mensagem de programa encerrado
    """
    resp = 0
    while resp < 1:
        palavras = frase.split()
        palavra_inicial = palavras[0]
        palavra_final = palavras[-1]
        anterior = get_previous_in_phrase(palavra_inicial, words)
        posterior = get_subsequent_in_phrase(palavra_final, words)
        nova_frase = f"{anterior} {frase} {posterior}"

        frase = nova_frase

        try:
            resp = int(input("Digite 0 para continuar, e qualquer outro valor para sair: "))
            if resp != 0:
                print(nova_frase)
                break
            else:
                print(nova_frase)
        except ValueError:
            print("Digite um valor inteiro positivo")
    return print("Programa encerrado.")


def get_previous(lista1, word):
    """
    Essa função pega a palavra anterior mais frequente da palavra digitada pelo usuário
    :param lista1: lista de palavras anteriores mais frequentes
    :param word: palavra digitada pelo usuário
    :return: Mensagem de erro
    """
    if word:
        options = {
            True: (desempatar(lista1)),
            False: (lista1[0])
        }

        immediate_previous = options[len(lista1) > 1]
        return immediate_previous
    return print("Essa palavra não esta no documento")


def get_previous_in_phrase(word, words):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_previous para a palavra inicial da frase.
    :param word: palavra inicial da frase
    :param words: todas as palavras presentes no texto
    :return: a função get_previous, ou seja, palavra anterior mais frequente ou mensagem de erro
    """
    lista = []
    previous1 = {}
    subsequent1 = {}
    fill_itens(lista, word, words, previous1, subsequent1)
    check_tie(previous1, subsequent1, lista)
    lista1, lista2 = check_tie(previous1, subsequent1, lista)

    if word:
        options = {
            True: (desempatar(lista1)),
            False: (lista1[0])
        }

        immediate_previous = options[len(lista1) > 1]
        return immediate_previous
    return print("Essa palavra não esta no documento")


def get_subsequent(lista2, word):
    """
    Essa função pega a palavra posterior mais frequente da palavra digitada pelo usuário
    :param lista2: lista de palavras posteriores mais frequentes
    :param word: palavra digitada pelo usuário
    :return: Mensagem de erro
    """
    if word:
        options = {
            True: (desempatar(lista2)),
            False: (lista2[0])
        }

        immediate_subsequent = options[len(lista2) > 1]
        return immediate_subsequent
    return print("Essa palavra não esta no documento")


def get_subsequent_in_phrase(word, words):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_subsequent para a palavra final da frase.
    :param word: palavra final da frase
    :param words: todas as palavras presentes no texto
    :return: a função get_subsequent, ou seja, palavra posterior mais frequente ou mensagem de erro
    """
    lista = []
    previous2 = {}
    subsequent2 = {}
    fill_itens(lista, word, words, previous2, subsequent2)
    check_tie(previous2, subsequent2, lista)
    lista1, lista2 = check_tie(previous2, subsequent2, lista)

    if word:
        options = {
            True: (desempatar(lista2)),
            False: (lista2[0])
        }

        immediate_subsequent = options[len(lista2) > 1]
        return immediate_subsequent
    return print("Essa palavra não esta no documento")


def check_tie(dict1, dict2, lista):
    """
    Encontra as palavras mais frequentes e ve se tem empate de aparições
    :param dict1: dict das palavras anteriores
    :param dict2: dict das palavras posteriores
    :param lista: lista de indices da palavra escolhida pelo usuário
    :return: mensagem de erro
    """
    # Encontra a(s) palavra(s) mais frequente(s)
    previous_word = max(dict1, key=lambda k: dict1[k])
    subsequent_word = max(dict2, key=lambda k: dict2[k])

    # Verifica se há empate de palavras mais frequentes
    previous_word_tie = [word for word in dict1 if dict1[word] == dict1[previous_word]]
    subsequent_word_tie = [word for word in dict2 if dict2[word] == dict2[subsequent_word]]
    if len(lista) > 0:
        return previous_word_tie, subsequent_word_tie
    return print("não tem nenhuma palavra nas listas")


def check_print_tie(lista1, lista2, word):
    """
    Essa função imprime as listas de palavras mais frequentes e imprime a frase mais comum formada pela
    anteior mais frequente, pela palavra escolhida pelo usuário e pela palavra subsequente mais frequente
    :param lista1: lista de palavras anteriores com o maior número de aparições
    :param lista2: lista de palavras posteriores com o maior número de aparições
    :param word: palavra que o usuário digitou
    :return: retorna a frase mais comum
    """
    print('-' * 150)
    print("As seguintes listas conterão a mais frequente palavra de acordo com sua categoria, e se houver mais de "
          "uma é porque estão empatadas na frequencia.\n")
    print("Lista das mais frequentes anteriores:")
    print(lista1, "\n")
    print("Lista das mais frequentes posteriores:")
    print(lista2, "\n")
    anterior = get_previous(lista1, word)
    posterior = get_subsequent(lista2, word)
    comuns = f"{anterior} {word} {posterior}"
    if comuns:
        print(comuns, "\n")
        return comuns


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


def add_in_list(lista, word, words):
    """
    adiciona itens em uma lista se esse item for igual a palavra escolhida pelo usuário.
    :param lista: lista em que os itens serão adicionados
    :param word: palavra escolhida pelo usuário
    :param words: lista de palavras do documento
    :return: tamanho da lista
    """
    for i, item in enumerate(words):
        if item == word:
            lista.append(i)
    return len(lista)


def add_itens_in_dicts(func, dict1, dict2, word, words):
    """
    se existir ao menos 1 item na lista, adiciona esse item na sua respectiva dict e atribui
     valor a esses itens, que aumenta a medida que ele reaparece na contagem da lista
    :param func: função que retorna o tamanho da lista
    :param dict1: dicionário de palavras anteriores, que no início está vazio
    :param dict2: dicionário de palavras posteriores, que no início está vazio
    :param word: palavra escolhida pelo usuário
    :param words: lista de palavras
    :return: dicionarios de anteriores e posteriores, com os seus respectivos itens e valores,
    que agora não estará mais vazio, como no início
    """
    if func > 0:
        # Conta a frequencia das palavras anteriores e posteriores
        for j, item in enumerate(words):
            if item == word:
                if words[j] == words[0]:
                    previous_word = words[-1]
                else:
                    previous_word = words[j - 1]
                if words[j] == words[-1]:
                    subsequent_word = words[0]
                else:
                    subsequent_word = words[j + 1]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word in dict1:
                    dict1[previous_word] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict1[previous_word] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word in dict2:
                    dict2[subsequent_word] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict2[subsequent_word] = 1
    return dict1, dict2


def fill_itens(lista, word, words, dict1, dict2):
    """
    Preenche automaticamente as listas e os dicts de acordo com a palavra em análise
    :param lista: lista de índices da palavra em análise
    :param word: palavra em análise
    :param words: todas as palavras do texto
    :param dict1: lista de palavras anteriores à palavra em análise
    :param dict2: lista de palavras posteriores à palavra em análise
    :return: ela preenche as listas e os dicts
    """
    list_add = add_in_list(lista, word, words)
    add_itens_in_dicts(list_add, dict1, dict2, word, words)


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

    if word in words:
        fill_itens(lista_de_busca, word, words, previous, subsequent)
        frequency(previous, subsequent, lista_de_busca)
        print_percentage(previous, subsequent)
        check_tie(previous, subsequent, lista_de_busca)
        lista1, lista2 = check_tie(previous, subsequent, lista_de_busca)
        frase = check_print_tie(lista1, lista2, word)

        print_phrase(frase, words)
        return print("Todas as informações de frequencia foram mostradas acima")
    return print("A palavra que você buscou não está no documento lido.")


menu()
