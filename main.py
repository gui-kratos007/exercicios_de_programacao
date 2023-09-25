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


if __name__ == "__main__":
    file_path = input("Entre com o path do arquivo que deseja processar: ")
    text = get_text(file_path)
    list_words = frequencia(text)
    print(list_words)
