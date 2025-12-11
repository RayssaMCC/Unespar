from xmlrpc.server import SimpleXMLRPCServer

# Estado Global do Jogo 
estado_jogo = {
    "pontuacao": 0,
    "vidas": 3,
    "nivel_atual": 1,
    "energizado": False # Estado se o astronauta comeu energizador
}
# Retorna o dicionário completo com o estado atual do jogo
def get_estado_jogo():
    print("Cliente solicitou o estado do jogo.")
    return estado_jogo

# Reinicia o jogo para o estado inicial
def reiniciar_jogo():
    estado_jogo["pontuacao"] = 0
    estado_jogo["vidas"] = 3
    estado_jogo["nivel_atual"] = 1
    estado_jogo["energizado"] = False
    print("O jogo foi reiniciado. Estado resetado.")
    return estado_jogo

# Chamada quando o jogador limpa o mapa
def venceu_nivel():
    estado_jogo["nivel_atual"] += 1
    estado_jogo["pontuacao"] += 500  # Bônus por vencer o nível / Finalizar jogo
    print(f"Nível concluído! Nível: {estado_jogo['nivel_atual']}, Pontos: {estado_jogo['pontuacao']}")
    return estado_jogo

# Chamada pelo cliente quando o astronauta colide com uma pastilha
def coletou_pastilha():
    estado_jogo["pontuacao"] += 10
    print(f"Pastilha coletada! Nova pontuação: {estado_jogo['pontuacao']}")
    return estado_jogo["pontuacao"]

# Chamada pelo cliente quando o astronauta colide com um item bônus
def coletou_item_bonus():
    estado_jogo["pontuacao"] += 50  # Um bônus maior
    print(f"ITEM DE BÔNUS COLETADO! Nova pontuação: {estado_jogo['pontuacao']}")
    return estado_jogo["pontuacao"]

# Chamada pelo cliente quando o astronauta colide com um alien
def colidiu_com_vilao():
    # Se o jogador estiver energizado, não perde vida
    if estado_jogo["energizado"]:
        estado_jogo["pontuacao"] += 100 # Comeu o alien
        print("Alien comido! Pontuação +100.")
    else:
        estado_jogo["vidas"] -= 1
        print(f"Colisão com alien! Vidas restantes: {estado_jogo['vidas']}")
    
    return get_estado_jogo() # Retorna o estado atualizado

# Chamada pelo cliente quando o astronauta colide com um energizador
def comeu_energizador():
    estado_jogo["energizado"] = True
    print("Astronauta está energizado!")
    return True

def fim_energizador():
    estado_jogo["energizado"] = False
    print("O efeito do energizador acabou.")
    return False

# Configuração e inicialização do servidor
try:
    host = 'localhost'
    port = 8000
    server = SimpleXMLRPCServer((host, port), allow_none=True)
    print(f"Servidor RPC iniciado em http://{host}:{port}/")

    # funções que o cliente pode acessar
    server.register_function(get_estado_jogo, "get_estado_jogo")
    server.register_function(reiniciar_jogo, "reiniciar_jogo")
    server.register_function(venceu_nivel, "venceu_nivel")
    server.register_function(coletou_pastilha, "coletou_pastilha")
    server.register_function(coletou_item_bonus, "coletou_item_bonus")
    server.register_function(colidiu_com_vilao, "colidiu_com_vilao")
    server.register_function(comeu_energizador, "comeu_energizador")
    server.register_function(fim_energizador, "fim_energizador")

    #Iniciar o servidor
    server.serve_forever()

except Exception as e:
    print(f"Erro ao iniciar o servidor: {e}")