import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9876/")


def listar_livros():
    lista = proxy.listar_livros()
    print("Título | Autor | Edição | Disponível?")
    for l in lista:
        disponivel = "Sim" if l['Disponível'] else "Não"
        print(f"{l['Título']} | {l['Autor']} | {l['Edição']} | {disponivel}")
    input("Digite uma tecla para continuar")

def buscar_autor():
    str_busca = input("Digite o nome do autor: ")
    resultado = proxy.buscar_autor(str_busca)

    if len(resultado) == 0:
        print("Nenhum livro encontrado com esse autor")
    else:
        for r in resultado:
            disponivel = "Sim" if r['Disponível'] else "Não"
            print(f"{r['Título']} | {r['Autor']} | {r['Edição']} | {disponivel}")
    input("Digite uma tecla para continuar")

while True:
    print("\n\n===Biblioteca da UNESPAR===")
    print("[1] - Listar livros")
    print("[2] - Buscar por autor")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        buscar_autor()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")