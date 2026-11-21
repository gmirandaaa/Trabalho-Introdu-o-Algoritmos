from src.config import TAMANHO_CELULA, DESLOCAMENTO_Y

# 1 = parede
# 0 = caminho livre

MAPA = [
    "11111111111111111111",
    "10000000001000000001",
    "10111101101011111011",
    "10000100000010000001",
    "11110111101010111101",
    "10000000100010000001",
    "10111110111011101111",
    "10000010000000100001",
    "11101011101110101101",
    "10001000001000100001",
    "10111011101011101111",
    "10000010000000000001",
    "11111111111111111111"
]

COLUNAS = len(MAPA[0])
LINHAS = len(MAPA)


def celula_para_pixel(coluna, linha):

    x = coluna * TAMANHO_CELULA
    y = DESLOCAMENTO_Y + linha * TAMANHO_CELULA

    return x, y


def caminho_livre(coluna, linha):

    if linha < 0 or linha >= LINHAS:
        return False

    if coluna < 0 or coluna >= COLUNAS:
        return False

    return MAPA[linha][coluna] == "0"


def obter_posicoes_livres():

    posicoes = []

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):

            if caminho_livre(coluna, linha):
                posicoes.append((coluna, linha))

    return posicoes