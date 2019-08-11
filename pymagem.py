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
        https://runestone.academy/runestone/books/published/thinkcspy/index.html

'''
#-------------------------------------------------------------------------- 

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, nlins, ncols, valor = 0):
        self.nlins = nlins
        self.ncols = ncols
        self.valor = valor
        self.tabela = []

        transporte = list()
        for l in range(self.nlins):
            for c in range(self.ncols):
                transporte.append(self.valor)
            self.tabela.append(transporte.copy())
            transporte.clear()

    def __str__(self):
        for col in self.tabela:
            print(col)
        return " "

    def size(self):
        tuple_return = (self.nlins, self.ncols)
        return "%d X %d" %(tuple_return[0], tuple_return[1])

    def get(self, lGet, cGet):
        return self.tabela[lGet][cGet]

    def put(self, lPut, cPut, vPut):
        self.tabela[lPut][cPut] = vPut

    def crop(self, tlL, tlC, brL, brC):
        if tlL > self.nlins - 1 or tlL < 0:
            tlL = 0

        if tlC > self.ncols - 1 or tlC < 0:
            tlC = 0

        if brL > self.nlins - 1 or brL < 0:
            brL = self.nlins - 1

        if brC > self.ncols - 1 or brC < 0:
            brC = self.ncols - 1

        pymagem_return = Pymagem((brL - tlL) + 1,  (brC - tlC) + 1, 0)
        linha_Pyr = 0
        coluna_Pyr = 0
        for line in range(tlL, brL + 1):
            for col in range(tlC, brC + 1):
                pymagem_return.tabela[linha_Pyr][coluna_Pyr] = self.tabela[line][col]
                coluna_Pyr += 1
            linha_Pyr += 1
            coluna_Pyr = 0

        return print(pymagem_return)






























