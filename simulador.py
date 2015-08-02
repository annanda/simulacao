# -*- coding: utf-8 -*-

"""
Ao fazer uma simulação, é preciso:

Definir variáveis de estados:
-- numero de pessoas na esteira -> quantidade_esteira [0, infinito]
-- numero de pessoas na bike -> quantidade_bike [0, infinito]


Definir eventos:
-- chegada de pessoas na academia -> chegada_academia
-- saída de pessoas depois da esteira -> saida_esteira
-- entrada de pessoa na bike -> entrada_bike
-- saída de pessoas depois da bike -> saida_bike
-- reentrada na esteira -> reentrada_esteira
"""

from collections import deque
from math import log
from random import *


def rodar_simulador():
    """
    Função principal que roda o simulador.
    Ao final imprime o tempo em que a simulação levou.
    """

    quantidade_esteira = 0
    quantidade_bike = 0
    tempo = 0
    eventos = deque([])
    # iniciar fila de eventos
    eventos.append(gerar_eventos())

    # tratar eventos
    cont = 1
    while eventos and cont <= 100:
        trata_evento(eventos.popleft())
        cont += 1
    print "tempo: {0}".format(tempo)

def gerar_amostra_chegada(taxa, fluxo):
    """
    Gera amostra de chegada de diferentes tipos de fluxo: poisson, deterministico ou uniforme
    Retorna o tempo amostrado para o fluxo dado, com a taxa dada.
    """

    u = random()
    if fluxo == "poisson":
        return (-1) * log(1 - u) / taxa
    if fluxo == "deterministico":
        return taxa
    if fluxo == "uniforme":
        return int((u * 100) + 50)

def trata_evento(evento):
    log = open('log.txt', 'w')
    tempo += evento[1]
