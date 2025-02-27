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
        self.array = np.full((lin, col), val)#arange(30).reshape(5,6)

    def __str__(self):

        return str(self.array)

    def size(self):
        return self.array.shape

    def get(self, lin, col):
        return (self.array[lin, col])

    def put(self, lin, col, valor):
        self.array[lin][col] = valor

    def crop(self, lt = 0, ct = 0, lb = "a", cb = "b"):
        if lb == "a":
            lb = self.lin
        if cb == "b":
            cb = self.col

        npr = NumPymagem(lb - lt + 1, cb - ct + 1)
        npr.array = (self.array[lt:lb + 1, ct:cb + 1]).copy()

        return npr

    def paste(self, other, tlin, tcol):
        lother = 0
        cother = 0
        for lpaste in range(tlin, tlin + other.lin):
            for cpaste in range(tcol, tcol + other.col):
                if((lpaste >= 0 and lpaste < self.lin) and (cpaste >= 0 and cpaste < self.col)):
                    self.array[lpaste, cpaste] = other.array[lother, cother]
                cother += 1
            lother += 1
            cother = 0

    def __add__(self, other):
        npaddr = NumPymagem(self.lin, self.col, 0)

        for ladd in range(self.lin):
            for cadd in range(self.col):
                npaddr.array[ladd, cadd] = self.array[ladd, cadd] + other.array[ladd, cadd]

        return npaddr

    def __mul__(self, alpha):
        npmulr = NumPymagem(self.lin, self.col, 0)

        for lmul in range(self.lin):
            for cmul in range(self.col):
                npmulr.array[lmul, cmul] = self.array[lmul, cmul] * alpha

        return npmulr

    def pinte_disco(self, lin, col, raio, valor):
        for ldsc in range(self.lin):
            for cdsc in range(self.col):
                if(((ldsc - lin)**2 + (cdsc - col)**2 - raio**2) <= 0):
                    if((ldsc >= 0 and ldsc < self.lin) and (cdsc >= 0 and cdsc < self.col)):
                        self.array[ldsc, cdsc] = valor

    def pinte_retangulo(self, lTL, cTL, lBR, cBR, val):
        for lp_r in range(lTL, lBR + 1):
            for cp_r in range(cTL, cBR + 1):
                if ((lp_r >= 0 and lp_r < self.lin) and (cp_r >= 0 and cp_r < self.col)):
                    self.array[lp_r, cp_r] = val

    def transpoe(self):
        self.array = self.array.reshape(self.col, self.lin)

    def rearranja(self, nlin, ncol):
        if(nlin * ncol == self.lin * self.col):
            self.array = self.array.reshape(nlin, ncol)












