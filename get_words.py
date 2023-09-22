def get_text(path):
    with open(path, 'r') as file:
        dados = file.read()
        if dados:
            return dados.encode("latin1").decode()
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


if __name__ == "__main__":
    path = input("Entre com o path do arquivo que deseja processar: ")
    text = get_text(path)
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
