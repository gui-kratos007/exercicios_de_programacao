def contar_palavras(file_path):
    print(file_path)
    # numero_de_palavras = 0
    with open(file_path, 'r') as file:
        dados = file.read()
        linhas = dados.split()
        if len(linhas) > 0:
            return len(linhas)
    return "arquivo vazio"


def frequencia():
    text = ("Na vida, a perseverança é essencial. Perseverança nos desafios, perseverança nas conquistas. Com "
            "dedicação e perseverança, alcançamos nossos objetivos. A perseverança nos impulsiona, nos inspira e nos "
            "torna resilientes diante das adversidades.").replace(",", "").replace(".", "").lower()
    # print(text.split().count("que"))
    max_min = [(name, text.split().count(name)) for name in text.split()]
    print(max_min)
    """new_list = []
    for name in text.split():
        new_list.append(name)
        #print(f"{name} ({text.split().count(name)})")"""


if __name__ == "__main__":
    """file_path = input("Entre com o path do arquivo que deseja processar: ")
    numero_de_palavras = contar_palavras(file_path)
    print(numero_de_palavras)"""

    frequencia()

