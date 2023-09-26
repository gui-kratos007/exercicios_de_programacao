def menu():
    while True:
        print("-" * 20)
        print("Menu interativo")
        print("-" * 20)
        print()
        print("Opções: ")
        print("[1] -> Carregar arquivo")
        print("[2] -> Exibir lista")
        print("[3] -> Buscar palavra")
        print("[9] -> Sair")

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
        elif answer == 9:
            break


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
    word = input("digite a palavra que quer pesquisar as posições (índices): ")
    lista_de_busca = []
    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)
    if len(lista_de_busca) > 0:
        return lista_de_busca
    return "essa palavra não está no texto"


def ascending_alphabetical_order(list_words):
    word_sorted = [word for word in set(list_words)]
    return sorted(word_sorted)


def descending_alphabetical_order(list_words):
    word_sorted = [word for word in set(list_words)]
    return sorted(word_sorted, reverse=True)


menu()
