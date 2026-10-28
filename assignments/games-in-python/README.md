
# 📘 Assignment: Games in Python

## 🎯 Objective

Pratique strings, seleção aleatória, condicionais e loops em Python construindo um jogo da forca jogável no terminal.

## 📝 Tasks

### 🛠️ Prepare the Game

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher a palavra secreta e preparar as variáveis que acompanham o progresso do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente da lista `words` usando o módulo `random`.
- Inicializar uma coleção de letras adivinhadas vazia.
- Definir e acompanhar o limite de palpites incorretos, começando com um máximo de 6.

### 🛠️ Implement the Guessing Loop

#### Descrição
Implemente o ciclo principal que recebe palpites de letras, atualiza o progresso e encerra o jogo quando o jogador vence ou fica sem tentativas.

#### Requisitos
O programa concluído deve:

- Mostrar a palavra como letras reveladas e espaços (`_`) para as letras ainda não adivinhadas.
- Solicitar um palpite de letra ao usuário e verificar se ele está na palavra secreta.
- Atualizar as letras adivinhadas em caso de acerto e reduzir as tentativas restantes em caso de erro.
- Encerrar quando todas as letras da palavra forem reveladas ou quando as tentativas incorretas se esgotarem.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.