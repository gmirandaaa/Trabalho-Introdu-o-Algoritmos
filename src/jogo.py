import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    TAMANHO_CELULA,
    DESLOCAMENTO_Y,
    PONTOS_VITORIA,
    BRANCO,
    PRETO,
    FUNDO,
    PAREDE,
    CHAO,
    AZUL,
    VERDE,
    AMARELO,
    VERMELHO,
    CAMINHO_RECORDE
)

from src.mapa import (
    MAPA,
    LINHAS,
    COLUNAS,
    celula_para_pixel
)

from src.funcoes import (
    iniciar_partida,
    mover_jogador,
    atualizar_estado
)

from src.dados import (
    salvar_recorde,
    carregar_recorde
)


def desenhar_texto(tela, mensagem, fonte, cor, posicao):
    """
    Exibe um texto na janela.
    """

    imagem = fonte.render(mensagem, True, cor)

    retangulo = imagem.get_rect(center=posicao)

    tela.blit(imagem, retangulo)


def desenhar_mapa(tela):
    """
    Desenha o labirinto na tela.
    """

    for linha in range(LINHAS):

        for coluna in range(COLUNAS):

            x, y = celula_para_pixel(coluna, linha)

            if MAPA[linha][coluna] == "1":

                cor = PAREDE

            else:

                cor = CHAO

            pygame.draw.rect(
                tela,
                cor,
                (x, y, TAMANHO_CELULA, TAMANHO_CELULA),
                border_radius=5
            )


def desenhar_itens(tela, itens, fonte_pequena):
    """
    Desenha os dados espalhados pelo labirinto.
    """

    aparencia = {
        "confiavel": (VERDE, "+"),
        "falso": (AMARELO, "!"),
        "pessoal": (VERMELHO, "X")
    }

    for item in itens:

        coluna, linha = item["posicao"]

        x, y = celula_para_pixel(coluna, linha)

        cor, simbolo = aparencia[item["tipo"]]

        centro = (
            x + TAMANHO_CELULA // 2,
            y + TAMANHO_CELULA // 2
        )

        pygame.draw.circle(
            tela,
            cor,
            centro,
            13
        )

        desenhar_texto(
            tela,
            simbolo,
            fonte_pequena,
            PRETO,
            centro
        )



def desenhar_jogador(tela, partida):
    coluna, linha = partida["jogador"]

    x, y = celula_para_pixel(coluna, linha)

    centro_x = x + TAMANHO_CELULA // 2
    centro_y = y + TAMANHO_CELULA // 2

    # Antena
    pygame.draw.line(
        tela, PRETO,
        (centro_x, centro_y - 12),
        (centro_x, centro_y - 18), 2
    )
    pygame.draw.circle(
        tela, AMARELO,
        (centro_x, centro_y - 19), 3
    )

    # Cabeça
    pygame.draw.rect(
        tela, AZUL,
        (centro_x - 12, centro_y - 13, 24, 17),
        border_radius=5
    )

    # Olhos
    pygame.draw.circle(
        tela, BRANCO,
        (centro_x - 5, centro_y - 7), 3
    )
    pygame.draw.circle(
        tela, BRANCO,
        (centro_x + 5, centro_y - 7), 3
    )

    # Corpo
    pygame.draw.rect(
        tela, AZUL,
        (centro_x - 9, centro_y + 5, 18, 12),
        border_radius=3
    )

    # Braços
    pygame.draw.line(
        tela, PRETO,
        (centro_x - 9, centro_y + 8),
        (centro_x - 14, centro_y + 13), 3
    )
    pygame.draw.line(
        tela, PRETO,
        (centro_x + 9, centro_y + 8),
        (centro_x + 14, centro_y + 13), 3
    )

    # Pernas
    pygame.draw.line(
        tela, PRETO,
        (centro_x - 5, centro_y + 17),
        (centro_x - 7, centro_y + 20), 3
    )
    pygame.draw.line(
        tela, PRETO,
        (centro_x + 5, centro_y + 17),
        (centro_x + 7, centro_y + 20), 3
    )

def desenhar_interface(
    tela,
    partida,
    recorde,
    fonte,
    fonte_pequena
):
    """
    Exibe pontuação, recorde, vidas e tempo.
    """

    pygame.draw.rect(
        tela,
        FUNDO,
        (0, 0, LARGURA_TELA, DESLOCAMENTO_Y)
    )

    desenhar_texto(
        tela,
        "CAÇA DADOS",
        fonte,
        BRANCO,
        (100, 25)
    )

    desenhar_texto(
        tela,
        f"Pontos: {partida['pontos']}/{PONTOS_VITORIA}",
        fonte_pequena,
        BRANCO,
        (290, 25)
    )

    desenhar_texto(
        tela,
        f"Recorde: {recorde}",
        fonte_pequena,
        BRANCO,
        (440, 25)
    )

    desenhar_texto(
        tela,
        f"Vidas: {partida['vidas']}",
        fonte_pequena,
        BRANCO,
        (560, 25)
    )

    desenhar_texto(
        tela,
        f"Tempo: {partida['tempo_restante']}s",
        fonte_pequena,
        BRANCO,
        (690, 25)
    )

    desenhar_texto(
        tela,
        "+ confiavel     ! falso     X pessoal",
        fonte_pequena,
        BRANCO,
        (LARGURA_TELA // 2, 58)
    )


def desenhar_tela_final(
    tela,
    estado,
    pontos,
    fonte,
    fonte_pequena
):
    """
    Exibe a mensagem de vitória ou derrota.
    """

    tela.fill(FUNDO)

    if estado == "vitoria":

        titulo = "Voce venceu!"
        detalhe = "Voce reuniu dados confiaveis para a IA."
        cor = VERDE

    else:

        titulo = "Fim de jogo!"
        detalhe = "Nem todos os dados eram seguros..."
        cor = VERMELHO

    desenhar_texto(
        tela,
        titulo,
        fonte,
        cor,
        (LARGURA_TELA // 2, 220)
    )

    desenhar_texto(
        tela,
        detalhe,
        fonte_pequena,
        BRANCO,
        (LARGURA_TELA // 2, 290)
    )

    desenhar_texto(
        tela,
        f"Pontuacao final: {pontos}",
        fonte,
        BRANCO,
        (LARGURA_TELA // 2, 350)
    )

    desenhar_texto(
        tela,
        "Pressione R para jogar novamente",
        fonte_pequena,
        BRANCO,
        (LARGURA_TELA // 2, 420)
    )

    desenhar_texto(
        tela,
        "Pressione ESC para sair",
        fonte_pequena,
        BRANCO,
        (LARGURA_TELA // 2, 455)
    )


def desenhar_partida(
    tela,
    partida,
    recorde,
    fonte,
    fonte_pequena
):
    """
    Organiza o desenho de todos os elementos.
    """

    tela.fill(FUNDO)

    desenhar_interface(
        tela,
        partida,
        recorde,
        fonte,
        fonte_pequena
    )

    desenhar_mapa(tela)

    desenhar_itens(
        tela,
        partida["itens"],
        fonte_pequena
    )

    desenhar_jogador(
        tela,
        partida
    )


def executar_jogo():
    """
    Inicializa o Pygame e executa o loop principal.
    """

    pygame.init()

    tela = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )

    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    fonte = pygame.font.SysFont("arial", 36)

    fonte_pequena = pygame.font.SysFont("arial", 17)

    partida = iniciar_partida()

    recorde = carregar_recorde(CAMINHO_RECORDE)

    rodando = True

    while rodando:

        relogio.tick(FPS)

        # Captura os eventos.
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                rodando = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    rodando = False

                elif partida["estado"] == "jogando":

                    mover_jogador(
                        partida,
                        evento.key
                    )

                elif evento.key == pygame.K_r:

                    partida = iniciar_partida()

        # Atualiza a situação da partida.
        if partida["estado"] == "jogando":

            atualizar_estado(partida)

        # Atualiza o recorde.
        if partida["pontos"] > recorde:

            recorde = partida["pontos"]

            salvar_recorde(
                CAMINHO_RECORDE,
                recorde
            )

        # Desenha a tela.
        if partida["estado"] == "jogando":

            desenhar_partida(
                tela,
                partida,
                recorde,
                fonte_pequena,
                fonte_pequena
            )

        else:

            desenhar_tela_final(
                tela,
                partida["estado"],
                partida["pontos"],
                fonte,
                fonte_pequena
            )

        pygame.display.flip()

    pygame.quit()