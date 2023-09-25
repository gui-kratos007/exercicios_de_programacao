def get_text(file_path):
    print(file_path)
    with open(file_path, 'r', encoding="utf-8") as file:
        dados = file.read()
        print(dados)
        if dados:
            return dados
    return "arquivo vazio"


def text_clean(text):
    return (text.replace(",", "")
            .replace(".", "")
            .lower()
            )


def frequencia(data):
    # Retorna uma lista de todas as palavras seguidas do número de vezes que ela aparece no texto.
    return [(name, text_clean(data).split().count(name)) for name in text_clean(data).split()]


def search_word(txt):
    word = input("digite a palavra que que pesquisar: ")
    lista_de_busca = []
    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)
    if len(lista_de_busca) > 0:
        return lista_de_busca
    return "essa palavra não está no texto"


if __name__ == "__main__":
    file_path = input("Entre com o path do arquivo que deseja processar: ")
    text = get_text(file_path)
    list_words = frequencia(text)
    print(list_words)
    busca = search_word(text)
    print(busca)
