# -*- coding: utf-8 -*-

import numpy as np
import random

class Grid:
    def __init__(self):
        self.grid = np.array([
            [0, 0, -1],
            [0, 0, 0],
            [0, 0, 1]
        ])
        self.estado_inical = (1, 1)
        self.estado = self.estado_inical

    def reset(self):
        self.estado = self.estado_inical
        return self.estado

    def is_terminal(self, estado):
        return self.grid[estado] == 1 or self.grid[estado] == -1

    def get_proximo_estado(self, estado, acao):
        proximo_estado = list(estado)
        if acao == 0:  # cima
            proximo_estado[0] = max(0, estado[0] - 1)
        elif acao == 1:  # direita
            proximo_estado[1] = min(2, estado[1] + 1)
        elif acao == 2:  # baixo
            proximo_estado[0] = min(2, estado[0] + 1)
        elif acao == 3:  # esquerda
            proximo_estado[1] = max(0, estado[1] - 1)
        return tuple(proximo_estado)

    def passo(self, acao):
        proximo_estado = self.get_proximo_estado(self.estado, acao)
        recompensa = self.grid[proximo_estado]
        self.estado = proximo_estado
        terminal = self.is_terminal(proximo_estado)
        return proximo_estado, recompensa, terminal

class QLearningAgente:
    def __init__(self, taxa_aprendizado=0.1, fator_desconto=0.9, taxa_e=0.1):
        self.tabela_q= np.zeros((3, 3, 4))
        self.taxa_aprendizado = taxa_aprendizado
        self.fator_desconto = fator_desconto
        self.taxa_e = taxa_e

    def escolhe_acao(self, estado):
        num_sorteado = random.uniform(0, 1)
        if num_sorteado < self.taxa_e:
            return random.randint(0, 3)
        else:
            return np.argmax(self.tabela_q[estado])

    def update_q(self, estado, acao, recompensa, proximo_estado):
        valor_q_antigo = self.tabela_q[estado][acao]
        proximo_max_q = np.max(self.tabela_q[proximo_estado])
        novo_valor_q = valor_q_antigo + self.taxa_aprendizado * (recompensa + self.fator_desconto * proximo_max_q - valor_q_antigo)
        self.tabela_q[estado][acao] = novo_valor_q

env = Grid()
agente = QLearningAgente()

epocas = 1000

for epoca in range(epocas):
    estado = env.reset() #posicione novamente o agente no estado inicial
    terminal = False

    while not terminal:
        acao = agente.escolhe_acao(estado)
        proximo_estado, recompensa, terminal = env.passo(acao)
        agente.update_q(estado, acao, recompensa, proximo_estado)
        estado = proximo_estado

print("Tabela Q final:")
print(agente.tabela_q)