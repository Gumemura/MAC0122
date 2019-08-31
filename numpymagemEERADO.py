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
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
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
from pymagem import Pymagem

#--------------------------------------------------------------------------

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, lin = 0, col =0, val = 0):
        self.lin = lin
        self.col = col
        self.list = [val] * (lin * col)
        self.table = ([[val] * col]) * lin

    def __str__(self):
        arrayRet = np.array(self.list).reshape(self.lin, self.col)

        return str(arrayRet)

    def test(self):
        #Uso interno
        a = 0
        for i in range(self.lin * self.col):
            self.list[i] = a
            a += 1

    def pegaIndice(self, l, c):
        #uso interno
        return (self.lin * l + c)

    def size(self):
        sizeRet = (self.lin, self.col)

        return sizeRet

    def get(self, lin, col):
        return self.list[lin * self.col + col]

    def put(self, lin, col, valor):
        self.list[lin * self.col + col] = valor

    def crop(self, lt = 0, ct = 0, lb = "a", cb = "b"):
        if lb == "a":
            lb = self.lin
        if cb == "b":
            cb = self.col

        pmRet = Pymagem(lb, cb, 0)

        return pmRet

    def paste(self, other, tlin, tcol):
        indOther = 0
        for lp_r in range(tlin, tlin + other.lin):
            for cp_r in range(tcol, tcol + other.col):
                if ((lp_r >= 0 and lp_r < self.lin) and (cp_r >= 0 and cp_r < self.col)):
                    self.list[self.pegaIndice(lp_r, cp_r)] = other.list[indOther]
                    indOther += 1

    def __add__(self, other):
        if(self.lin == other.lin):
            lR = self.lin
        else:
            if(self.lin > other.lin):
                lR = other.lin
            else:
                lR = self.lin

        if(self.col == other.col):
            cR = self.col
        else:
            if(self.col > other.col):
                cR = other.col
            else:
                cR = self.col

        if(len(self.list) == len(other.list)):
            limit = len(self.list)
        else:
            if(len(self.list) > len(other.list)):
                limit = len(other.list)
            else:
                limit = len(self.list)

        npR = NumPymagem(lR, cR, 0)

        for indR in range(limit):
            npR.list[indR] = self.list[indR] + other.list[indR]

        return npR

    def __mul__(self, alpha):
        npmR = NumPymagem(self.lin, self.col, 0)

        for imul in range(len(self.list)):
            npmR.list[imul] = self.list[imul] * alpha

        return npmR

    def pinte_disco (self, lin, col, raio, valor):
        for ldsc in range(self.lin):
            for cdsc in range(self.col):
                if(((ldsc - lin)**2 + (cdsc - col)**2 - raio**2) <= 0):
                    if((ldsc >= 0 and ldsc < self.lin) and (cdsc >= 0 and cdsc < self.col)):
                        self.list[self.pegaIndice(ldsc, cdsc)] = valor

    def pinte_retangulo(self, lTL, cTL, lBR, cBR, val):
        for lp_r in range(lTL, lBR + 1):
            for cp_r in range(cTL, cBR + 1):
                if ((lp_r >= 0 and lp_r < self.lin) and (cp_r >= 0 and cp_r < self.col)):
                    self.list[self.pegaIndice(lp_r, cp_r)] = val










