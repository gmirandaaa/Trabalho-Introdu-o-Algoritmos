# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> Caça Dados

## 2. Integrantes do grupo

- Nome 1: Guilherme Miranda

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Inteligência Artificial no cotidiano e uso responsável de dados.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> Um pequeno robô precisa coletar dados para alimentar um sistema de inteligência artificial. Entretanto, nem todos os dados são confiáveis: alguns são úteis e outros contêm informações falsas ou pessoais que não deveriam ser compartilhadas.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Coleta de itens e labirinto.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> O jogador controla um robô usando as setas do teclado.
  Existem itens espalhados pela tela.
  "Dados confiáveis" dão pontos.
  "Dados falsos" fazem o jogador perder pontos.
  "Dados pessoais" representam um risco e devem ser evitados.
  Ao alcançar uma pontuação mínima, o jogador vence.
  Se o tempo acabar ou as vidas chegarem a zero, perde.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Coletar "Dados confiáveis", evitar "Dados falsos" e "Dados pessoais"

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: O jogador controla um robô utilizando as setas do teclado.
- Regra 2: Cada dado confiável coletado acrescenta 10 pontos à pontuação.
- Regra 3: Cada dado falso coletado retira 5 pontos.
- Regra 4: Coletar dados pessoais faz o jogador perder uma vida.
- Regra 5: O jogador começa com 3 vidas e tem 180 segundos para completar o objetivo.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> O jogador vence ao alcançar 100 pontos coletando dados confiáveis antes que o tempo termine ou que suas vidas acabem.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> O jogador perde se ficar sem vidas ou se o tempo de 60 segundos acabar antes de alcançar a pontuação necessária. Ao final da partida, será exibida uma mensagem informando se houve vitória ou derrota e a pontuação obtida.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal: Um pequeno robô controlado pelo jogador.**
- **Obstáculos ou desafios: Dados falsos e dados pessoais que devem ser evitados, além das limitações de tempo e vidas.** 
- **Itens ou objetos de interação (se houver): Dados confiáveis, dados falsos e dados pessoais espalhados pelo cenário.**
- **Pontuação, vidas, tempo ou progresso: Pontuação acumulada, três vidas iniciais e cronômetro de 60 segundos.**

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> As setas do teclado serão utilizadas para movimentar o robô para cima, baixo, esquerda e direita. A tecla ESC poderá ser utilizada para encerrar a partida.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Implementar a movimentação do personagem e detectar colisões com os itens.
- Dificuldade 2: Desenvolver o sistema de pontuação, vidas e controle do tempo.
- Dificuldade 3: Organizar o código em funções e implementar testes para as principais regras do jogo.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> O jogo deverá apresentar uma janela funcional com um robô controlado pelo teclado e itens distribuídos pelo cenário. O jogador deverá coletar dados confiáveis para acumular pontos, evitando dados falsos e pessoais, que provocam penalidades. A partida terá três vidas e duração de 60 segundos, com condições de vitória e derrota definidas. Também deverá apresentar a pontuação durante a partida e salvar o recorde em um arquivo.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Adicionar efeitos sonoros para coleta de itens e situações de vitória ou derrota.
- Melhoria 2: Criar novas fases com diferentes distribuições de itens e desafios.
- Melhoria 3: Adicionar um menu inicial e uma tela de recordes.
