import pygame
import sys
import xmlrpc.client 
import os
import random
from collections import deque

pygame.init()

# Resolução 
LARGURA_TELA = 1024
ALTURA_TELA = 768
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("SPACE RUNNER")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
AZUL_SELECAO = (0, 150, 255)


# Fonte
NOME_ARQUIVO_FONTE = os.path.join("assets", "PressStart2P-Regular.ttf")

# Tenta carregar o arquivo da fonte
try:
    FONTE_TITULO = pygame.font.Font(NOME_ARQUIVO_FONTE, 40) # Tamanho Título
    FONTE_MENU = pygame.font.Font(NOME_ARQUIVO_FONTE, 24)  # Tamanho Menu
    FONTE_VOLTAR = pygame.font.Font(NOME_ARQUIVO_FONTE, 18) # Tamanho Voltar
    print(f"Fonte pixel '{NOME_ARQUIVO_FONTE}' carregada com sucesso!")

# Se falhar (arquivo não encontrado), usa a fonte padrão do sistema
except FileNotFoundError:
    print(f"AVISO: Arquivo da fonte '{NOME_ARQUIVO_FONTE}' não encontrado.")
    print("Usando fonte padrão do sistema (pode não ser pixelada).")
    FONTE_TITULO = pygame.font.SysFont(None, 80)
    FONTE_MENU = pygame.font.SysFont(None, 50)
    FONTE_VOLTAR = pygame.font.SysFont(None, 40)
except Exception as e:
    print(f"Erro ao carregar fonte: {e}")
    FONTE_TITULO = pygame.font.SysFont(None, 80)
    FONTE_MENU = pygame.font.SysFont(None, 50)
    FONTE_VOLTAR = pygame.font.SysFont(None, 40)

# Efeitos sonoros
try:
    SOM_COLETA = pygame.mixer.Sound(os.path.join("assets", "coleta.mp3")) 
    SOM_MORTE = pygame.mixer.Sound(os.path.join("assets", "morte.wav"))   

    print("Efeitos sonoros (SFX) carregados com sucesso!")
except pygame.error as e:
    print(f"AVISO: Erro ao carregar SFX. {e}")
    # Cria sons falsos para o jogo não travar se o arquivo faltar
    try:
        SOM_COLETA = pygame.mixer.Sound(buffer=b"")
        SOM_MORTE = pygame.mixer.Sound(buffer=b"")
    except Exception:
        SOM_COLETA = None
        SOM_MORTE = None

MUSICA_MENU = os.path.join("assets", "menu.mp3")
MUSICA_POWERUP = os.path.join("assets", "powerup.wav")
MUSICA_VITORIA = os.path.join("assets", "win.wav")
MUSICA_GAME_OVER = os.path.join("assets", "game_over.wav")

IMAGEM_FUNDO_MENU = None # Variável global para a imagem de fundo do menu

# Carrega a imagem de fundo e a redimensiona para o tamanho da tela
def carregar_imagem_fundo(caminho_imagem):
    global IMAGEM_FUNDO_MENU
    try:
        imagem = pygame.image.load(caminho_imagem).convert_alpha()
        IMAGEM_FUNDO_MENU = pygame.transform.scale(imagem, (LARGURA_TELA, ALTURA_TELA))
        
        # Define o nível de transparência (0 = invisível, 255 = opaco)
        IMAGEM_FUNDO_MENU.set_alpha(128) 
        
        print(f"Imagem de fundo '{caminho_imagem}' carregada com sucesso!")
    except pygame.error as e:
        print(f"Erro ao carregar a imagem de fundo '{caminho_imagem}': {e}")
        IMAGEM_FUNDO_MENU = None 

# Função genérica que desenha uma tela preta com conteúdo e um botão "voltar" clicável
def desenhar_tela_simples(textos_conteudo):
    
    # Prepara o texto e o retângulo do botão
    texto_str_voltar = "VOLTAR"
    texto_voltar_render = FONTE_VOLTAR.render(texto_str_voltar, True, CINZA)

    pos_voltar_x = LARGURA_TELA // 2 - texto_voltar_render.get_width() // 2
    pos_voltar_y = ALTURA_TELA - 100
    
    # Cria o retângulo clicável para o botão
    voltar_rect = pygame.Rect(pos_voltar_x, pos_voltar_y, texto_voltar_render.get_width(), texto_voltar_render.get_height())

    esperando = True
    while esperando:
        # Pega a posição do mouse a cada frame
        mouse_pos = pygame.mouse.get_pos()
        
        TELA.fill(PRETO) # Fundo preto para telas secundárias
        
        # Desenha o conteúdo específico
        for texto_renderizado, pos_y in textos_conteudo:
            pos_x = LARGURA_TELA // 2 - texto_renderizado.get_width() // 2
            TELA.blit(texto_renderizado, (pos_x, pos_y))
            
        # Define a cor do botão (muda no hover)
        cor_voltar = CINZA
        if voltar_rect.collidepoint(mouse_pos):
            cor_voltar = BRANCO

        # Renderiza e desenha o botão
        texto_voltar_final = FONTE_VOLTAR.render(texto_str_voltar, True, cor_voltar)
        TELA.blit(texto_voltar_final, (pos_voltar_x, pos_voltar_y))
        
        pygame.display.flip()
        
        # Loop de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Evento de teclado (Voltar)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    esperando = False
            
            # Evento de clique do mouse (Voltar)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Botão esquerdo
                    if voltar_rect.collidepoint(mouse_pos):
                        esperando = False 
# Telas específicas
def iniciar_jogo():
    print("Iniciando conexão RPC...")

    pygame.mixer.music.stop() # Para a música do menu quando inicia o nível

    try:
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") # Conecta ao servidor
        print("Resetando estado do servidor para nova partida...")
        estado = proxy.reiniciar_jogo()         
        print(f"Conectado! Estado inicial: {estado}")
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
        return

    # Grupos de Sprites
    todos_sprites = pygame.sprite.Group()
    paredes = [] # Lista de Rects para colisão
    pastilhas = pygame.sprite.Group()
    itens_bonus = pygame.sprite.Group()
    energizadores = pygame.sprite.Group()
    viloes = pygame.sprite.Group()
    
    # Carregar Imagens
    imgs_player_normal = carregar_animacoes_separadas("Astronauta")     
    imgs_player_power = carregar_animacoes_separadas("AstronautaPower") 
    img_pastilha = carregar_sprite_item("pastilha.png")
    img_bonus = carregar_sprite_item("item_bonus.png")
    img_energizador = carregar_sprite_item("energizador.png")
    imgs_vilao1 = carregar_animacoes_separadas("Vilão1")
    imgs_vilao2 = carregar_animacoes_separadas("Vilão2")
    imgs_vilao3 = carregar_animacoes_separadas("Vilão3")
    imgs_vilao4 = carregar_animacoes_separadas("Vilão4")
    lista_animacoes_viloes = [imgs_vilao1, imgs_vilao2, imgs_vilao3, imgs_vilao4]

    # --- Mapeamento fixo de spawns para tipos de vilão ---
    mapeamento_viloes = {(14, 11): 0, (15, 11): 1, (16, 11): 2, (17, 11): 3 }

    # Se o mapeamento não for definido manualmente, popula automaticamente
    if not mapeamento_viloes:
        ordem_spawns = []
        for r_idx, r in enumerate(MAPA_LAYOUT):
            for c_idx, ch in enumerate(r):
                if ch == 'V':
                    ordem_spawns.append((c_idx, r_idx))
        for idx, pos in enumerate(ordem_spawns):
            mapeamento_viloes[pos] = idx % len(lista_animacoes_viloes)

    # Construção do Mapa
    player = None
    
    # Reinicia o contador de vilões para garantir a ordem certa (1, 2, 3, 4)
    indice_vilao_atual = 0 
    
    for row_idx, row in enumerate(MAPA_LAYOUT):
        for col_idx, tile in enumerate(row):
            x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
            
            if tile == "1": # Parede
                parede_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                paredes.append(parede_rect)
            
            elif tile == "P": # Player
                spawn_x, spawn_y = x, y 
                player = Jogador(col_idx, row_idx, imgs_player_normal, imgs_player_power)
                todos_sprites.add(player)
            
            elif tile == "V": # Vilão
                # Seleciona o conjunto de imagens
                tipo_indice = indice_vilao_atual % 4
                imgs_da_vez = lista_animacoes_viloes[tipo_indice]
                
                # Cada vilão sai 100 frames depois do anterior (aprox 5 segundos)
                delay_frames = tipo_indice * 100 
                
                # Cria o vilão passando o delay
                v = Vilao(col_idx, row_idx, imgs_da_vez, tipo_indice, delay_frames)
                
                viloes.add(v)
                todos_sprites.add(v)
                
                print(f"Vilão {tipo_indice} criado na pos {col_idx},{row_idx}. Sairá em {delay_frames} frames.")
                indice_vilao_atual += 1
                
            elif tile == ".": # Pastilha
                spr = pygame.sprite.Sprite()
                spr.image = img_pastilha
                spr.rect = spr.image.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                pastilhas.add(spr)
                todos_sprites.add(spr)
            
            elif tile == "B": # Bônus
                spr = pygame.sprite.Sprite()
                spr.image = img_bonus
                spr.rect = spr.image.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                itens_bonus.add(spr)
                todos_sprites.add(spr)
            
            elif tile == "E": # Energizador
                spr = pygame.sprite.Sprite()
                spr.image = img_energizador
                spr.rect = spr.image.get_rect(center=(x + TILE_SIZE//2, y + TILE_SIZE//2))
                energizadores.add(spr)
                todos_sprites.add(spr)

    clock = pygame.time.Clock()
    run = True

    foi_energizado = False
    
    # --- LOOP DO JOGO ---
    while run:
        clock.tick(20) # 20 FPS
        
        # 1 - Eventos (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False # Volta pro menu
        
        # 2 - Atualização local (movimento e colisão com parede)
        player.update(paredes)
        viloes.update(paredes, player.rect)
        
        # Sincronia do fim do Power-Up 
        esta_energizado = player.tempo_power > 0
        
        # Estava energizado antes, mas o tempo acabou (é 0 ou menor)
        if foi_energizado and not esta_energizado:
            try:
                proxy.fim_energizador()
                print("Power-up expirou. Servidor atualizado.")
                pygame.mixer.music.stop() # Para a música do power-up
            except:
                print("Erro ao avisar fim do power-up")
            foi_energizado = False # Reseta o estado local
        
        # Se está energizado agora, atualiza a variável para o próximo frame
        if esta_energizado:
            foi_energizado = True

        # 3 - Colisões (envio pro servidor) 
        # Colisão com Pastilhas
        hit_pastilha = pygame.sprite.spritecollide(player, pastilhas, True) 
        if hit_pastilha:
            SOM_COLETA.play()
            try:
                nova_pont = proxy.coletou_pastilha()
                estado["pontuacao"] = nova_pont
            except:
                print("Erro de conexão RPC (Pastilha)")

        # Colisão com Item Bônus
        hit_bonus = pygame.sprite.spritecollide(player, itens_bonus, True) 
        if hit_bonus:
            SOM_COLETA.play()
            try:
                nova_pont = proxy.coletou_item_bonus() 
                estado["pontuacao"] = nova_pont
                print("Bônus coletado!")
            except:
                print("Erro de conexão RPC (Bônus)")

        ## Colisão com Vilões
        hit_viloes_lista = pygame.sprite.spritecollide(player, viloes, False)
        
        for vilao in hit_viloes_lista:
            # Se o jogador estiver energizado
            if player.tempo_power > 0:
                SOM_COLETA.play() # Som de comer fantasma como se fosse uma pastilha
                vilao.respawn()   # Manda o vilão de volta pra casa
                
                try:
                    estado = proxy.colidiu_com_vilao()
                    print(f"Vilão derrotado! Pontuação atualizada no servidor: {estado['pontuacao']}")
                except Exception as e:
                     print(f"Erro de conexão RPC (Comer Vilão): {e}")
                
            # Se o jogador estiver normal (morre)
            else:
                try:
                    estado = proxy.colidiu_com_vilao() # Avisa servidor que perdeu vida
                    SOM_MORTE.play()

                    # Chama a tela com a pontuação final caso acabem as vidas
                    if estado["vidas"] <= 0:
                        print("Vidas esgotadas. Game Over.")                        
                        mostrar_game_over(estado["pontuacao"])
                        run = False # Encerra o loop do jogo para voltar ao menu
                    else:
                        print("Vida perdida! Respawn do jogador")
                        player.rect.topleft = (spawn_x, spawn_y) # Volta o player para o início

                        # Reseta os vilões para suas casas (evita morrer instantaneamente de novo)
                        for v in viloes:
                            v.respawn()
                except:
                    print("Erro de conexão RPC (Vilão)")

        # Colisão com Energizador
        hit_energ = pygame.sprite.spritecollide(player, energizadores, True)
        if hit_energ:
            try:
                proxy.comeu_energizador() 
                player.ativar_poder()     
                SOM_COLETA.play()         

                pygame.mixer.music.load(MUSICA_POWERUP)
                pygame.mixer.music.play(-1) # O -1 faz a música tocar em loop infinito
                print("Música de Power-up iniciada!")

            except Exception as e: 
                print(f"Erro ao tocar música powerup: {e}")

        # --- CONDIÇÃO DE VITÓRIA ---
        # Verifica se acabaram as pastilhas e os bônus
        if len(pastilhas) == 0 and len(itens_bonus) == 0:
            try:
                # Chama o servidor para atualizar nível e ganhar bônus de pontuação
                estado = proxy.venceu_nivel()
                print("Nível concluído com sucesso!")

                # Mostra a tela e encerra o jogo atual voltando ao menu
                mostrar_vitoria(estado["pontuacao"])
                run = False 
                
            except Exception as e:
                print(f"Erro ao computar vitória: {e}")
                run = False

        # 4. Desenho
        TELA.fill(PRETO)
        
        # Desenhar Paredes
        for parede in paredes:
            pygame.draw.rect(TELA, AZUL_SELECAO, parede) # Paredes azuis 
            
        todos_sprites.draw(TELA)
        
        # HUD (placar e vidas vindos do servidor)
        placar_texto = FONTE_VOLTAR.render(f"PONTUAÇÃO: {estado.get('pontuacao', 0)}", True, BRANCO)
        vidas_texto = FONTE_VOLTAR.render(f"VIDAS: {estado.get('vidas', 3)}", True, BRANCO)
        TELA.blit(placar_texto, (10, 10))
        TELA.blit(vidas_texto, (LARGURA_TELA - 150, 10))
        
        pygame.display.flip()

def mostrar_vitoria(pontuacao_final):
    print("Tela de Vitória exibida.")
    
    try:
        pygame.mixer.music.load(MUSICA_VITORIA)
        pygame.mixer.music.play(0) 
        print(f"Tocando música de vitória: {MUSICA_VITORIA}")
    except Exception as e:
        print(f"Erro ao tocar música de vitória: {e}")

    # Textos da vitória
    texto1 = FONTE_TITULO.render("VITÓRIA!", True, (0, 255, 0)) # Verde
    texto2 = FONTE_MENU.render(f"Pontuação Final: {pontuacao_final}", True, BRANCO)
    texto3 = FONTE_VOLTAR.render("Pressione ENTER para voltar ao menu", True, CINZA)
    
    # Loop de exibição simples
    esperando = True
    while esperando:
        TELA.fill(PRETO)
        
        # Centraliza os textos
        TELA.blit(texto1, (LARGURA_TELA//2 - texto1.get_width()//2, 200))
        TELA.blit(texto2, (LARGURA_TELA//2 - texto2.get_width()//2, 300))
        TELA.blit(texto3, (LARGURA_TELA//2 - texto3.get_width()//2, 500))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    esperando = False
    
def mostrar_game_over(pontuacao_final):
    print("Tela de Game Over exibida.")

    try:
        pygame.mixer.music.load(MUSICA_GAME_OVER)
        pygame.mixer.music.play(0) 
        print(f"Tocando música de game over: {MUSICA_GAME_OVER}")
    except Exception as e:
        print(f"Erro ao tocar música de game over: {e}")
    
    # Textos do Game Over
    texto1 = FONTE_TITULO.render("GAME OVER", True, (255, 0, 0)) # Vermelho
    texto2 = FONTE_MENU.render(f"Pontuação Final: {pontuacao_final}", True, BRANCO)
    texto3 = FONTE_VOLTAR.render("Pressione ENTER para voltar ao menu", True, CINZA)
    
    # Loop de exibição
    esperando = True
    while esperando:
        TELA.fill(PRETO)
        
        # Centraliza os textos
        TELA.blit(texto1, (LARGURA_TELA//2 - texto1.get_width()//2, 200))
        TELA.blit(texto2, (LARGURA_TELA//2 - texto2.get_width()//2, 300))
        TELA.blit(texto3, (LARGURA_TELA//2 - texto3.get_width()//2, 500))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    esperando = False

def mostrar_ajuda():
    print("Tela 'Ajuda' aberta.")
    texto1 = FONTE_MENU.render("Use as SETAS para mover o Astronauta", True, BRANCO)
    texto2 = FONTE_MENU.render("Colete todas as pastilhas", True, BRANCO)
    texto3 = FONTE_MENU.render("Evite os Aliens!", True, BRANCO)
    
    desenhar_tela_simples([(texto1, 200), (texto2, 260), (texto3, 320)])

def mostrar_sobre():
    print("Tela 'Sobre' aberta.")
    texto1 = FONTE_MENU.render("Jogo criado por: Marielly e Rayssa", True, BRANCO)
    texto2 = FONTE_MENU.render("Disciplina: Sistemas Distribuídos", True, BRANCO)
    texto3 = FONTE_MENU.render("UNESPAR - Ciência da Computação", True, BRANCO)
    
    desenhar_tela_simples([(texto1, 150), (texto2, 220), (texto3, 290)])

class Entidade(pygame.sprite.Sprite):
    def __init__(self, x, y, animacoes_dict):
        super().__init__()
        self.animacoes = animacoes_dict
        self.direcao = 'down' # Começa olhando para baixo
        
        # Define a lista de sprites atual baseada na direção
        self.sprites = self.animacoes[self.direcao]
        self.index_sprite = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.velocidade = 4
    
    def animar(self):
        # Atualiza a lista de sprites se mudou de direção
        self.sprites = self.animacoes[self.direcao]
        
        self.index_sprite += 0.2 # Velocidade da animação
        if self.index_sprite >= len(self.sprites):
            self.index_sprite = 0
        self.image = self.sprites[int(self.index_sprite)]

class Jogador(Entidade):
    def __init__(self, x, y, anims_normal, anims_power):
        # Inicia com a animação padrão (branca)
        super().__init__(x, y, anims_normal)
        
        self.anims_normal = anims_normal
        self.anims_power = anims_power
        
        self.tempo_power = 0 # Contador de tempo do efeito (em frames)

    def ativar_poder(self):
        self.tempo_power = 300 # 300 frames (aprox 10 segundos)
        
    def update(self, paredes_rects):
        # Lógica do Power-Up 
        if self.tempo_power > 0:
            self.tempo_power -= 1
            self.animacoes = self.anims_power # Usa sprites AMARELOS
        else:
            self.animacoes = self.anims_normal # Usa sprites BRANCOS

        # Movimentação
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT]: 
            dx = -self.velocidade
            self.direcao = 'left'
        elif keys[pygame.K_RIGHT]: 
            dx = self.velocidade
            self.direcao = 'right'
        elif keys[pygame.K_UP]: 
            dy = -self.velocidade
            self.direcao = 'up'
        elif keys[pygame.K_DOWN]: 
            dy = self.velocidade
            self.direcao = 'down'
        
        # Colisão X
        self.rect.x += dx
        for parede in paredes_rects:
            if self.rect.colliderect(parede):
                if dx > 0: self.rect.right = parede.left
                if dx < 0: self.rect.left = parede.right
                
        # Colisão Y
        self.rect.y += dy
        for parede in paredes_rects:
            if self.rect.colliderect(parede):
                if dy > 0: self.rect.bottom = parede.top
                if dy < 0: self.rect.top = parede.bottom
        
        # Animação
        if dx != 0 or dy != 0:
            self.animar()
        else:
            self.image = self.animacoes[self.direcao][0]

class Vilao(Entidade):
    def __init__(self, x, y, anims, tipo_ia, delay_inicio=0):
        super().__init__(x, y, anims)
        self.tipo_ia = tipo_ia # 0: Aleatório, 1: Perseguidor, 2: Patrulheiro, 3: Rápido
        
        # Controle de Saída
        self.delay_inicio = delay_inicio
        self.tempo_vida = 0 
        self.em_casa = True 
        
        self.velocidade_base = 4 if self.tipo_ia == 3 else 3
        self.velocidade = self.velocidade_base
        
        self.direcao_atual = (0, 0)
        
        self.zona_patrulha = pygame.Rect(0, 0, 544, 320) # Zona de patrulha (pra IA tipo 2)
        
        self.rect_porta_casa = pygame.Rect(15 * TILE_SIZE, 10 * TILE_SIZE, 2 * TILE_SIZE, TILE_SIZE) # Porta da casa dos vilões


    def respawn(self):
        print("Vilão comido! Respawn do vilão")
        self.em_casa = True
        self.tempo_vida = 0
        self.delay_inicio = 100 
        self.rect.x = 15 * TILE_SIZE
        self.rect.y = 11 * TILE_SIZE
        self.direcao_atual = (0, 0)
    
    # Faz os vilões sairem da casa pra começar a perseguição
    def sair_da_casa(self):
        alvo_x = 15 * TILE_SIZE + 16 
        alvo_y = 9 * TILE_SIZE
        
        dx, dy = 0, 0
        margem = 4
        
        if abs(self.rect.centerx - alvo_x) > margem:
            if self.rect.centerx < alvo_x: dx = self.velocidade
            else: dx = -self.velocidade
            dy = 0 
        else:
            if self.rect.y > alvo_y:
                dy = -self.velocidade
                dx = 0
            else:
                self.em_casa = False 
                self.rect.y = alvo_y 
                return

        self.rect.x += dx
        self.rect.y += dy
        
        if dx > 0: self.direcao = 'right'
        elif dx < 0: self.direcao = 'left'
        elif dy < 0: self.direcao = 'up'
        self.animar()

    def obter_direcoes_validas(self, paredes_rects):
        opcoes = [
            (0, -self.velocidade), (0, self.velocidade), 
            (-self.velocidade, 0), (self.velocidade, 0)
        ]
        validas = []
        
        for dx, dy in opcoes:
            # Cria o retângulo futuro (onde ele vai estar se der esse passo)
            teste_rect = pygame.Rect(self.rect.x + dx, self.rect.y + dy, self.rect.width, self.rect.height)
            
            bateu = False
            
            # Verifica paredes
            for p in paredes_rects:
                if teste_rect.colliderect(p):
                    bateu = True
                    break
            
            # Verifica porta da casa (se estiver fora)
            if not self.em_casa and teste_rect.colliderect(self.rect_porta_casa):
                bateu = True

            # Verifica zona de patrulha
            if self.tipo_ia == 2:
                if not self.zona_patrulha.contains(teste_rect):
                    bateu = True

            if not bateu:
                validas.append((dx, dy))
                
        return validas

    def ia_aleatoria(self, validas):
        if not validas: return (0, 0)
        oposta = (-self.direcao_atual[0], -self.direcao_atual[1])
        opcoes_filtradas = [d for d in validas if d != oposta]
        if opcoes_filtradas: return random.choice(opcoes_filtradas)
        return random.choice(validas)

    def ia_perseguidora(self, validas, player_rect, paredes_rects):
        if not validas:
            return (0, 0)
        if not player_rect:
            return self.ia_aleatoria(validas)

        tentativa = self.buscar_proximo_passo(player_rect, paredes_rects)
        if tentativa and tentativa in validas:
            return tentativa

        melhor_dir = (0, 0)
        menor_distancia = float('inf')
        for dx, dy in validas:
            novo_x = self.rect.centerx + dx
            novo_y = self.rect.centery + dy
            dist = (player_rect.centerx - novo_x)**2 + (player_rect.centery - novo_y)**2
            if dist < menor_distancia:
                menor_distancia = dist
                melhor_dir = (dx, dy)
        return melhor_dir

    def buscar_proximo_passo(self, player_rect, paredes_rects):

        # Coordenadas de tile (col, linha)
        inicio = (self.rect.centerx // TILE_SIZE, self.rect.centery // TILE_SIZE)
        objetivo = (player_rect.centerx // TILE_SIZE, player_rect.centery // TILE_SIZE)

        if inicio == objetivo:
            return (0, 0)

        # Monta conjunto de tiles bloqueados a partir das paredes
        bloqueados = set()
        for p in paredes_rects:
            tx = p.x // TILE_SIZE
            ty = p.y // TILE_SIZE
            bloqueados.add((tx, ty))

        # Bloqueia a porta da casa pros vilões não entrarem de novo
        left_t = self.rect_porta_casa.left // TILE_SIZE
        right_t = max(0, (self.rect_porta_casa.right - 1) // TILE_SIZE)
        top_t = self.rect_porta_casa.top // TILE_SIZE
        bottom_t = max(0, (self.rect_porta_casa.bottom - 1) // TILE_SIZE)
        for tx in range(left_t, right_t + 1):
            for ty in range(top_t, bottom_t + 1):
                bloqueados.add((tx, ty))

        # Se for patrulheiro (tipo 2), limita pra zona de patrulha
        zona_limits = None
        if self.tipo_ia == 2:
            zx1 = max(0, self.zona_patrulha.left // TILE_SIZE)
            zy1 = max(0, self.zona_patrulha.top // TILE_SIZE)
            zx2 = (self.zona_patrulha.right - 1) // TILE_SIZE
            zy2 = (self.zona_patrulha.bottom - 1) // TILE_SIZE
            zona_limits = (zx1, zy1, zx2, zy2)

        # Limites do mapa
        try:
            max_lin = len(MAPA_LAYOUT)
            max_cols = len(MAPA_LAYOUT[0])
        except Exception:
            max_cols = 100
            max_lin = 100

        q = deque()
        q.append(inicio)
        veio = {inicio: None}

        dirs = [ (0, -1), (0, 1), (-1, 0), (1, 0) ]

        encontrado = False
        while q:
            atual = q.popleft()
            if atual == objetivo:
                encontrado = True
                break
            for dx_t, dy_t in dirs:
                nx = atual[0] + dx_t
                ny = atual[1] + dy_t
                if nx < 0 or ny < 0 or nx >= max_cols or ny >= max_lin:
                    continue
                if zona_limits:
                    zx1, zy1, zx2, zy2 = zona_limits
                    if not (zx1 <= nx <= zx2 and zy1 <= ny <= zy2):
                        continue
                if (nx, ny) in bloqueados:
                    continue
                if (nx, ny) in veio:
                    continue
                veio[(nx, ny)] = atual
                q.append((nx, ny))

        if not encontrado:
            return None

        # Reconstrói o caminho até o início e pega o próximo tile 
        no = objetivo
        caminho = []
        while no is not None:
            caminho.append(no)
            no = veio.get(no)
        caminho.reverse()
        if len(caminho) < 2:
            return None
        prox_tile = caminho[1]

        alvo_cx = prox_tile[0] * TILE_SIZE + TILE_SIZE // 2
        alvo_cy = prox_tile[1] * TILE_SIZE + TILE_SIZE // 2

        dx_pixel = alvo_cx - self.rect.centerx
        dy_pixel = alvo_cy - self.rect.centery
        step_x = 0
        step_y = 0
        if dx_pixel > 0: step_x = self.velocidade
        elif dx_pixel < 0: step_x = -self.velocidade
        if dy_pixel > 0: step_y = self.velocidade
        elif dy_pixel < 0: step_y = -self.velocidade

        return (step_x, step_y)

    def update(self, paredes_rects, player_rect=None):
        self.tempo_vida += 1
        
        if self.tempo_vida < self.delay_inicio:
            self.animar() 
            return

        if self.em_casa:
            self.sair_da_casa()
            return 

        # IA Normal
        no_centro_x = (self.rect.x % TILE_SIZE) < self.velocidade
        no_centro_y = (self.rect.y % TILE_SIZE) < self.velocidade
        
        teste_colisao = self.rect.move(self.direcao_atual)
        vai_bater = False
        for p in paredes_rects:
            if teste_colisao.colliderect(p):
                vai_bater = True
                break
        
        if not self.em_casa and teste_colisao.colliderect(self.rect_porta_casa):
             vai_bater = True
        
        # Verificação extra no update pra garantir que não saia da zona de patrulha
        if self.tipo_ia == 2 and not self.zona_patrulha.contains(teste_colisao):
             vai_bater = True

        if (no_centro_x and no_centro_y) or vai_bater or self.direcao_atual == (0,0):
            validas = self.obter_direcoes_validas(paredes_rects)
            
            if validas:
                if self.tipo_ia == 1:
                    self.direcao_atual = self.ia_perseguidora(validas, player_rect, paredes_rects)
                else:
                    self.direcao_atual = self.ia_aleatoria(validas)
            else:
                self.direcao_atual = (-self.direcao_atual[0], -self.direcao_atual[1])

        # Movimento com verificação de colisão
        teste_seguranca = self.rect.move(self.direcao_atual)
        bloqueado = False
        for p in paredes_rects:
            if teste_seguranca.colliderect(p):
                bloqueado = True
                break
        
        if not self.em_casa and teste_seguranca.colliderect(self.rect_porta_casa):
            bloqueado = True
        
        if not bloqueado:
            self.rect.x += self.direcao_atual[0]
            self.rect.y += self.direcao_atual[1]
        else:
            self.direcao_atual = (0,0) 
            self.rect.center = (
                (self.rect.centerx // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2,
                (self.rect.centery // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
            )

        if self.direcao_atual[0] < 0: self.direcao = 'left'
        elif self.direcao_atual[0] > 0: self.direcao = 'right'
        elif self.direcao_atual[1] < 0: self.direcao = 'up'
        elif self.direcao_atual[1] > 0: self.direcao = 'down'
        
        self.animar()

# Função principal que desenha e gerencia o menu inicial
def main_menu():

    opcoes_menu = ["INICIAR JOGO", "AJUDA", "SOBRE", "SAIR"]
    opcao_selecionada = 0
    opcoes_rects = [] # Lista para guardar os retângulos de cada opção
    
    carregar_imagem_fundo(os.path.join("sprites", "galaxia.png"))
    
    try:
        pygame.mixer.music.load(MUSICA_MENU)
        pygame.mixer.music.set_volume(0.5) # Volume de 0.0 a 1.0
        pygame.mixer.music.play(-1) # O -1 faz a música tocar em loop infinito
    except pygame.error as e:
        print(f"AVISO: Não foi possível carregar a música do menu '{MUSICA_MENU}': {e}")

    while True:
        opcoes_rects = [] # Limpa a lista de retângulos a cada frame
        mouse_pos = pygame.mouse.get_pos() # Pega a posição do mouse a cada frame

        TELA.fill(PRETO) # Desenha a imagem de fundo se ela foi carregada
        
        if IMAGEM_FUNDO_MENU:
            TELA.blit(IMAGEM_FUNDO_MENU, (0, 0))

        # Desenha o título
        texto_titulo = FONTE_TITULO.render("SPACE RUNNER", True, BRANCO)
        # desenha um retângulo semi-transparente atrás do título
        s = pygame.Surface((texto_titulo.get_width() + 20, texto_titulo.get_height() + 20), pygame.SRCALPHA)
        s.fill((0,0,0,128)) # Preto com 50% de transparência
        TELA.blit(s, (LARGURA_TELA // 2 - s.get_width() // 2, 90))
        TELA.blit(texto_titulo, (LARGURA_TELA // 2 - texto_titulo.get_width() // 2, 100))

        # Desenha as opções do menu
        for i, opcao in enumerate(opcoes_menu):
            cor = BRANCO
            if i == opcao_selecionada:
                cor = AZUL_SELECAO # Destaca a opção selecionada
            
            texto_opcao = FONTE_MENU.render(opcao, True, cor)
            
            # Calcula a posição e cria o retângulo
            pos_x = LARGURA_TELA // 2 - texto_opcao.get_width() // 2
            pos_y = 300 + i * 60
            texto_rect = pygame.Rect(pos_x, pos_y, texto_opcao.get_width(), texto_opcao.get_height())
            
            opcoes_rects.append(texto_rect)
            
            # desenha um retângulo semi-transparente atrás das opções
            s_opcao = pygame.Surface((texto_opcao.get_width() + 20, texto_opcao.get_height() + 10), pygame.SRCALPHA)
            s_opcao.fill((0,0,0,96)) # Preto com 38% de transparência
            TELA.blit(s_opcao, (pos_x - 10, pos_y - 5))
            
            # Desenha o texto na tela
            TELA.blit(texto_opcao, (pos_x, pos_y))

        pygame.display.flip()

        # Processa eventos (teclado e mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Eventos de teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    opcao_selecionada = (opcao_selecionada + 1) % len(opcoes_menu)
                elif event.key == pygame.K_UP:
                    opcao_selecionada = (opcao_selecionada - 1) % len(opcoes_menu)
                elif event.key == pygame.K_RETURN: # Tecla ENTER
                    if opcao_selecionada == 0:
                        iniciar_jogo()
                    elif opcao_selecionada == 1:
                        mostrar_ajuda()
                    elif opcao_selecionada == 2:
                        mostrar_sobre()
                    elif opcao_selecionada == 3:
                        pygame.quit()
                        sys.exit()

            # Eventos de mouse (Hover)
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                # Verifica se o mouse está sobre algum dos retângulos
                for i, rect in enumerate(opcoes_rects):
                    if rect.collidepoint(mouse_pos):
                        opcao_selecionada = i # Atualiza a seleção para o hover

            # Eventos de mouse (Clique)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Botão esquerdo
                    mouse_pos = event.pos
                    # Verifica em qual retângulo o clique ocorreu
                    for i, rect in enumerate(opcoes_rects):
                        if rect.collidepoint(mouse_pos):
                            # Age como se a tecla ENTER fosse pressionada
                            if i == 0:
                                iniciar_jogo()
                            elif i == 1:
                                mostrar_ajuda()
                            elif i == 2:
                                mostrar_sobre()
                            elif i == 3:
                                pygame.quit()
                                sys.exit()

# --- CONFIGURAÇÕES DO MAPA E SPRITES ---
TILE_SIZE = 32  # Tamanho de cada quadrado da grade

def carregar_animacoes_separadas(pasta):
    animacoes = {
        'up': [], 'down': [], 'left': [], 'right': []
    }
    
    caminho_completo = os.path.join("sprites", pasta)
    
    if os.path.exists(caminho_completo):
        arquivos = sorted(os.listdir(caminho_completo))
        
        for arquivo in arquivos:
            if arquivo.lower().endswith(".png"):
                try:
                    caminho_arquivo = os.path.join(caminho_completo, arquivo)
                    img = pygame.image.load(caminho_arquivo).convert_alpha()
                    
                    # 1. Remove bordas invisíveis
                    try:
                        mask = pygame.mask.from_surface(img)
                        rect_visivel = mask.get_bounding_rects()
                        if rect_visivel:
                            rect_final = rect_visivel[0].unionall(rect_visivel)
                            img = img.subsurface(rect_final).copy()
                    except: pass

                    # 2. Estica 28x28 (menor que o corredor de 32 para não travar)
                    img = pygame.transform.scale(img, (28, 28))
                    
                    nome = arquivo.lower()
                    if "costa" in nome: animacoes['up'].append(img)
                    elif "frente" in nome: animacoes['down'].append(img)
                    elif "esq" in nome: animacoes['left'].append(img)
                    elif "dir" in nome: animacoes['right'].append(img)
                        
                except Exception as e:
                    print(f"Erro imagem {arquivo}: {e}")

    for chave in animacoes:
        if not animacoes[chave]:
            surf = pygame.Surface((28, 28))
            surf.fill((255, 0, 255))
            animacoes[chave] = [surf]
            
    return animacoes

# Função para carregar imagem única (itens)
def carregar_sprite_item(nome_arquivo):
    caminho = os.path.join("sprites", nome_arquivo)
    try:
        img = pygame.image.load(caminho).convert_alpha()
        
        # 1. Remove bordas invisíveis (mantém o desenho focado)
        try:
            mask = pygame.mask.from_surface(img)
            rect_visivel = mask.get_bounding_rects()
            if rect_visivel:
                rect_final = rect_visivel[0].unionall(rect_visivel)
                img = img.subsurface(rect_final).copy()
        except Exception:
            pass 

        # 2. Define tamanho baseado no tipo de item
        if "pastilha" in nome_arquivo.lower():
            novo_tamanho = 12  # Pastilha 
        else:
            novo_tamanho = 24  # Energizador e Bônus

        return pygame.transform.scale(img, (novo_tamanho, novo_tamanho))
        
    except Exception as e:
        print(f"Erro ao carregar item {nome_arquivo}: {e}")
        surf = pygame.Surface((10, 10))
        surf.fill((255, 255, 0))
        return surf

# 1 = Parede, . = Pastilha, E = Energizador, B = Bônus, P = Player, V = Vilão, 0 = Vazio (Túnel)
MAPA_LAYOUT = [
    "11111111111111111111111111111111",
    "1......E.......11.......B......1", 
    "1.1111.1111111.11.1111111.1111.1", 
    "1.1111.1111111.11.1111111.1111.1", 
    "1..........B.............E.....1", 
    "1.1111.11.111111111111.11.1111.1", 
    "1.1111.11.111111111111.11.1111.1", 
    "1..B...11......11......11......1",
    "111111.1111111.11.1111111.111111", 
    "1..............................1", 
    "1.1111.111.1111001111.111.1111.1", 
    "1.1111.....100VVVV001..B..1111.1", # Spawn dos Vilões
    "1.1111.111.1111111111.111.1111.1", 
    "1.....B........11..............1", 
    "111111.1111111.11.1111111.111111", 
    "1..............11..............1", 
    "1.1111.1111111.11.1111111.1111.1", 
    "1.1111.1111111.11.1111111.1111.1", 
    "1......11....E.P.B.....11......1", # Spawn do Player
    "111.11.11.111111111111.11.11.111", 
    "111.11.11.111111111111.11.11.111", 
    "1......11...B..11......11......1",
    "1E............................B1", 
    "11111111111111111111111111111111"  
]

if __name__ == "__main__":
    main_menu()