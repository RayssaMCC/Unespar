from xmlrpc.server import SimpleXMLRPCServer

acervo = {
    1:{
        "Título": "Sistemas Distribuídos",
        "Ano": 2007,
        "Edição": 4,
        "Autor": "Coulouris",
        "Exemplares_total": 5,
        "Exemplares_emprestados": 2
    }
}

def listar_livros():
    lista = []
    for livro in acervo.values():
        disponivel = livro["Exemplares_total"] - livro["Exemplares_emprestados"]
        lista.append({
            "Título": livro["Título"],
            "Autor": livro["Autor"],
            "Edição": livro["Edição"],
            "Disponível": disponivel
        })
    return lista

def buscar_autor(str_busca):
    resultado = []
    for l in acervo.values():
        if str_busca.lower() in l["Autor"].lower():
            disponivel = l["Exemplares_total"] - l["Exemplares_emprestados"]
            resultado.append({
                "Título": l["Título"],
                "Autor": l["Autor"],
                "Edição": l["Edição"],
                "Disponível": disponivel
            })
    return resultado

#criar o processo
server = SimpleXMLRPCServer(("localhost", 9876))
print("Servidor criado na porta 9876")

server.register_function(listar_livros, "listar_livros")
server.register_function(buscar_autor, "buscar_autor")
server.serve_forever()