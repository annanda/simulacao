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


class VariaveisDeEstados(object):
    """Aqui contém as variáveis de estado do simulador"""

    def __init__(self):
        super(VariaveisDeEstados, self).__init__()
        self.quantidade_esteira = 0
        self.quantidade_bike = 0
        self.tempo = 0
        self.eventos = deque([])


def rodar_simulador():
    """
    Função principal que roda o simulador.
    Ao final imprime o tempo em que a simulação levou.
    """
    variaveis_de_estados = VariaveisDeEstados()

    # iniciar fila de eventos
    variaveis_de_estados.eventos.append(gerar_evento(variaveis_de_estados))

    # tratar eventos
    cont = 1
    while eventos and cont <= 100:
        trata_evento(variaveis_de_estados.eventos.popleft())
        cont += 1
    print "tempo: {0}".format(variaveis_de_estados.tempo)

def gerar_evento(variaveis_de_estados):
    amostra_chegada_academia = gerar_amostra_chegada_academia(taxa_chegada)
    amostra_saida_esteira = gerar_amostra_saida_esteira(taxa_saida_esteira)
    amostra_entrada_bike = gerar_amostra_entrada_bike(taxa_entrada_bike)
    amostra_saida_bike = gerar_amostra_saida_bike(taxa_saida_bike)
    amostra_reentrada_esteira = gerar_amostra_reentrada_esteira(taxa_reentrada_esteira)

    if variaveis_de_estados.quantidade_bike + variaveis_de_estados.quantidade_esteira == 0:
        return [1, amostra_chegada_academia]
    else:



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
