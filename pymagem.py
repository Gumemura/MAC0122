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

        EP03 A partir da linha 110

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
        matriz = ''

        '''Aula de 22/08/19: como fazer o __str__ que faz o retorno independentemente do valor da lista: 
            variavel_tip_str = str(self.tabela[0])
            dane-se o tipo do objeto, ele sera convertido para string!
            nao precisava de todos esses ifs
        '''
        for linS in range(len(self.tabela)):
            matriz += '['
            for colS in range(len(self.tabela[0])):
                if(type(self.tabela[linS][colS]) == int):
                    matriz += ("%d") %self.tabela[linS][colS]
                elif(type(self.tabela[linS][colS]) == str):
                    matriz += ("%c") %self.tabela[linS][colS]
                elif(type(self.tabela[linS][colS]) == float):
                    matriz += ("%.1f") %self.tabela[linS][colS]

                if colS != len(self.tabela[0]) - 1:
                    matriz += ", "
            matriz += ']\n'

        return matriz

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

########################## EP 03 ##########################

    def __add__(self, pymagem_soma):
        linhasAdd = int()
        colunasAdd = int()

        linhasAdd = len(self.tabela)
        colunasAdd = len(self.tabela[0])

        pymagem_somada = Pymagem(linhasAdd, colunasAdd, 0)

        for l in range(linhasAdd):
            for c in range(colunasAdd):
                pymagem_somada.put(l, c, self.tabela[l][c] + pymagem_soma.tabela[l][c])

        return pymagem_somada

    def __mul__(self, alpha):
        linhasMul = int()
        colunasMul = int()

        linhasMul = len(self.tabela)
        colunasMul = len(self.tabela[0])

        pymagem_Mul = Pymagem(linhasMul, colunasMul, 0)

        for l in range(linhasMul):
            for c in range(colunasMul):
                pymagem_Mul.put(l, c, self.tabela[l][c]*alpha)

        return pymagem_Mul

    def paste(self, other, tlin, tcol):
        coordL = tlin
        coordC = tcol

        for lo in range(len(other.tabela)):
            for co in range(len(other.tabela[0])):
                if lo < len(self.tabela) and co < (self.tabela[0]):
                    if (coordL >= 0 and coordC >= 0) and (coordL < len(self.tabela) and coordC < len(self.tabela[0])):
                        self.tabela[coordL][coordC] = other.tabela[lo][co]
                    coordC += 1
            coordL += 1
            coordC = tcol

    def pinte_disco(self, lin, col, raio, val):

        for lPD in range(len(self.tabela)):
            for cPD in range(len(self.tabela[0])):
                if(((lPD - lin)**2 + (cPD - col)**2 - raio**2) <= 0):
                    if((lPD >= 0 and lPD < len(self.tabela)) and (cPD >= 0 and cPD < len(self.tabela[0]))):
                        self.tabela[lPD][cPD] = val

    def pinte_retangulo(self, lTL, cTL, lBR, cBR, val):

        for lp_r in range(lTL, lBR + 1):
            for cp_r in range(cTL, cBR + 1):
                if ((lp_r >= 0 and lp_r < len(self.tabela)) and (cp_r >= 0 and cp_r < len(self.tabela[0]))):
                    self.tabela[lp_r][cp_r] = val





































