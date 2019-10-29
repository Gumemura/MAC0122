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

class MarkovModel:
    def __init__(self, k, corpus):
        self.k = k
        self.corpus = corpus
        self.listCorpus = list(corpus)

    def alphabet(self):
        def mergeSort(alist):
            if len(alist)>1:
                mid = len(alist)//2
                lefthalf = alist[:mid]
                righthalf = alist[mid:]
        
                mergeSort(lefthalf)
                mergeSort(righthalf)
        
                i=0
                j=0
                k=0
        
                while i < len(lefthalf) and j < len(righthalf):
                    if lefthalf[i] < righthalf[j]:
                        alist[k]=lefthalf[i]
                        i=i+1
                    else:
                        alist[k]=righthalf[j]
                        j=j+1
                    k=k+1
        
                while i < len(lefthalf):
                    alist[k]=lefthalf[i]
                    i=i+1
                    k=k+1
        
                while j < len(righthalf):
                    alist[k]=righthalf[j]
                    j=j+1
                    k=k+1

        def rmv_rptds(lista):
            a = []
            for i in lista:
                if i not in a:
                    a.append(i)
            return a

        mergeSort(self.listCorpus)
        listaAlfabeto = rmv_rptds(self.listCorpus)

        stringRet = ""
        for elem in listaAlfabeto:
            stringRet += elem

        return stringRet

    def N(self, fatia):
        indice = 0
        contador = 0

        if len(fatia) == self.k or len(fatia) == self.k + 1:
            while indice < len(self.corpus):
                if indice + len(fatia) - 1 >= len(self.corpus):
                    if fatia == self.corpus[indice: len(self.corpus)] + self.corpus[0: indice + len(fatia) - len(self.corpus)]:
                        contador += 1
                else:
                    if fatia == self.corpus[indice:indice + len(fatia)]:
                        contador += 1
                indice += 1

            if contador > 0:
                return contador

    def laplace(self, t):
        if self.N(t) == None:
            nt = 0
        else:
            nt = self.N(t)

        if self.N(t[:-1]) == None:
            ntz = 0
        else:
            ntz = self.N(t[:-1])

        return (nt + 1)/(ntz + len(self.alphabet()))














'''
modelo1 = MarkovModel(2, "aabcabaacaac")

modelo3 = MarkovModel(0, "Como é bom estudar MAC0122!")




>>> modelo1.N("aa")
3
>>> modelo1.N("aab")
1
>>> modelo1.N("aac")
2
>>> modelo1.N("aaa")
>>> modelo1.N("aaaa")
>>> modelo1.N("a")

>>> modelo1.laplace("aaa")
0.16666666666666666
>>> modelo1.laplace("aab")
0.3333333333333333
>>> modelo1.laplace("aac")
0.5



'''
