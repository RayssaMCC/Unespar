# 👽 Space Runner 

### Implementação de um jogo eletrônico distribuído  
**Autores:** Marielly Deise e Rayssa Mara  
**Disciplina:** Redes de Computadores e Sistemas Distribuídos – UNESPAR  

---

## 🧩 Sobre o Jogo
**Space Runner** é uma reinterpretação do clássico *Pac-Man* desenvolvida com uma arquitetura de sistemas distribuídos **(Cliente-Servidor)**.

### Funcionalidades Técnicas
* **Arquitetura:** O jogo é dividido em dois processos distintos. O **Cliente** gerencia a interface gráfica (Pygame), inputs e detecção inicial de colisões, enquanto o **Servidor** gerencia o estado global (pontuação, vidas, nível).
* **Comunicação:** A troca de mensagens entre cliente e servidor é realizada via **XML-RPC** (Remote Procedure Call).

### Jogabilidade
O jogador controla um astronauta que deve coletar todas as pastilhas no mapa para finalizar o jogo, enquanto foge de quatro tipos de alienígenas com comportamentos distintos (aleatório, perseguidor, patrulheiro e rápido).
* **Pastilhas:** Aumentam a pontuação.
* **Bônus (Gemas):** Fornecem pontuação extra.
* **Energizadores (Arma Laser):** Permitem que o astronauta derrote temporariamente os alienígenas.

---

## 🚀 Pré-requisitos

* Certifique-se de que o **Python 3** está instalado;
* Instale a biblioteca pygame utilizando `pip install pygame` no terminal do VSCode;
* Certifique-se de que todos os arquivos estão na mesma pasta dos códigos .py e em suas devidas pastas (assets e sprites).

---

## 👾 Como executar

* Inicie o servidor utilizando o comando `python servidor.py` no terminal do VSCode e o mantenha aberto;
* Abra um segundo terminal e execute o comando `python cliente_jogo.py` para iniciar o cliente;
* Após os procedimentos, uma janela do pygame deve abrir com o menu principal do jogo e ele estará pronto para ser jogado.

---