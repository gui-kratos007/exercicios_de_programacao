def contar_palavras(file_path):
    print(file_path)
    # numero_de_palavras = 0
    with open(file_path, 'r') as file:
        dados = file.read()
        linhas = dados.split()
        if len(linhas) > 0:
            return len(linhas)
    return "arquivo vazio"


if __name__ == "__main__":
    file_path = input("Entre com o path do arquivo que deseja processar: ")
    numero_de_palavras = contar_palavras(file_path)
    print(numero_de_palavras)
