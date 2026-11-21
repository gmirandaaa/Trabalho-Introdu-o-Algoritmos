import random
import pygame

from src.config import (
    PONTOS_VITORIA,
    TEMPO_LIMITE,
    VIDAS_INICIAIS,
    QUANTIDADE_ITENS
)

from src.mapa import (
    obter_posicoes_livres,
    caminho_livre
)


def calcular_pontos(pontos_atual, pontos_ganhos):
    """
    Soma os pontos ganhos à pontuação atual.
    """

    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """
    Reduz a quantidade de vidas.
    """

    return max(0, vida_atual - dano)


def jogador_perdeu(vidas):
    """
    Verifica se o jogador perdeu todas as vidas.
    """

    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """
    Mantém um valor dentro de um intervalo.
    """

    if valor < minimo:
        return minimo

    if valor > maximo:
        return maximo

    return valor


def criar_item(posicoes_ocupadas):
    """
    Cria um dado em uma posição livre.

    Tipos:
    - confiavel
    - falso
    - pessoal
    """

    posicoes_disponiveis = [
        posicao
        for posicao in obter_posicoes_livres()
        if posicao not in posicoes_ocupadas
    ]

    if not posicoes_disponiveis:
        return None

    posicao = random.choice(posicoes_disponiveis)

    tipo = random.choices(
        ["confiavel", "falso", "pessoal"],
        weights=[55, 25, 20],
        k=1
    )[0]

    return {
        "posicao": posicao,
        "tipo": tipo
    }


def iniciar_partida():
    """
    Inicializa os elementos da partida.
    """

    jogador = (1, 1)

    itens = []

    for _ in range(QUANTIDADE_ITENS):

        posicoes_ocupadas = (
            [jogador]
            + [item["posicao"] for item in itens]
        )

        item = criar_item(posicoes_ocupadas)

        if item is not None:
            itens.append(item)

    return {
        "jogador": jogador,
        "itens": itens,
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "inicio": pygame.time.get_ticks(),
        "tempo_restante": TEMPO_LIMITE,
        "estado": "jogando"
    }


def mover_jogador(partida, tecla):
    """
    Movimenta o robô pelas setas do teclado.
    """

    coluna, linha = partida["jogador"]

    movimentos = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0)
    }

    if tecla not in movimentos:
        return

    dx, dy = movimentos[tecla]

    nova_coluna = coluna + dx
    nova_linha = linha + dy

    if caminho_livre(nova_coluna, nova_linha):

        partida["jogador"] = (
            nova_coluna,
            nova_linha
        )

        verificar_coleta(partida)


def verificar_coleta(partida):
    """
    Verifica se o robô coletou algum dado.
    Aplica os pontos ou penalidades.
    """

    posicao_jogador = partida["jogador"]

    for item in partida["itens"][:]:

        if item["posicao"] == posicao_jogador:

            if item["tipo"] == "confiavel":

                partida["pontos"] = calcular_pontos(
                    partida["pontos"],
                    10
                )

            elif item["tipo"] == "falso":

                partida["pontos"] = max(
                    0,
                    partida["pontos"] - 5
                )

            elif item["tipo"] == "pessoal":

                partida["vidas"] = tomar_dano(
                    partida["vidas"],
                    1
                )

            # Remove o item coletado.
            partida["itens"].remove(item)

            # Cria um novo item em outra posição.
            posicoes_ocupadas = (
                [partida["jogador"]]
                + [i["posicao"] for i in partida["itens"]]
            )

            novo_item = criar_item(posicoes_ocupadas)

            if novo_item is not None:
                partida["itens"].append(novo_item)

            break


def atualizar_estado(partida):

    tempo_decorrido = (
        pygame.time.get_ticks() - partida["inicio"]
    ) // 1000

    partida["tempo_restante"] = max(
        0,
        TEMPO_LIMITE - tempo_decorrido
    )

    if partida["pontos"] >= PONTOS_VITORIA:

        partida["estado"] = "vitoria"

    elif (
        jogador_perdeu(partida["vidas"])
        or partida["tempo_restante"] <= 0
    ):

        partida["estado"] = "derrota"