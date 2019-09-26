# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Guilherme Umemura
    NUSP: 9353592

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np

#-------------------------------------------------------------------------
# se você quiser a classe Queue feita na aula, coloque o seu arquivo queue.py
# na mesma pasta do EP e descomente a linha abaixo
# from queue import Queue

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto empty
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade n x m com todos os sítios inicialmente bloqueados.
    o parâmetro shape é a forma (n, m) do array que representa a grade.
    '''
    def __init__(self, size):
        if type(size) != tuple or len(size) != 2:
            print("Erro")
        else:
            self.shape = size
            self.lin = size[0]
            self.col = size[1]
            self.array = np.full((size), 0)

    def __str__(self):
        return str(self.array)

    def is_open(self, linIO, colIO):
        if (linIO >= 0 and linIO < self.lin) and (colIO >= 0 and colIO < self.col):
            if(self.array[linIO][colIO] == 1):
                return True
            else:
                return False
        else:
            print("Erro")

    def is_full(self, linIF, colIF):
        if (linIF >= 0 and linIF < self.lin) and (colIF >= 0 and colIF < self.col):
            if(self.array[linIF][colIF] == 2):
                return True
            else:
                return False
        else:
            print("Erro")

    #def percolates():

    def no_open(self):
        quantOpen = 0
        for lin in range(self.shape[0]):
            for col in range(self.shape[1]):
                if self.array[lin][col] == 1:
                    quantOpen += 1

        return quantOpen

    #def open(self, linO, colO):

    def get_grid(self):
        return (self.array).copy()

    def open(self):
        listaChecagem = []
        linhaOpena = 0
        for colO in range(self.col):
            if self.array[linhaOpena][colO] = 1:
                linhaVizinho = linhaOpena - 1
                colVizinho = col0












