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
        
        Função mergesort() baseada na contida na página https://panda.ime.usp.br/pythonds/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html

'''

class MarkovModel:
    def __init__(self, k, corpus):
        self.k = k
        self.corpus = corpus
        self.listCorpus = list(corpus)

    def __str__(self):
        textRet = ''
        if len(self.corpus) > 0:
            dicioFatias = {}
            k = self.k
    
            for i in range(2):
                indice = 0
                k += i
    
                while indice < len(self.corpus):
                    if indice + k > len(self.corpus):
                        fatia = self.corpus[indice:] + self.corpus[0:(indice + k) - len(self.corpus)]
                    else:
                        fatia = self.corpus[indice: indice + k]
    
                    if fatia not in dicioFatias:
                        dicioFatias[fatia] = 1
                    else:
                        dicioFatias[fatia] += 1
    
                    indice += 1
    
            textRet += "alfabeto tem " + str(len(self.alphabet())) + " símbolos\n"
    
            dicioOrdenado = {}
            listaKeys = list(dicioFatias.keys())
    
            for elem in listaKeys:
                if len(elem) != self.k:
                    indexKP = listaKeys.index(elem)
                    break
    
            listaK0 = sorted(listaKeys[:indexKP])
            listaK1 = sorted(listaKeys[indexKP:])
            listaKeys = listaK0 + listaK1
    
    
            for i in range(len(listaKeys)):
                dicioOrdenado[listaKeys[i]] = dicioFatias[listaKeys[i]]
    
            for chave, quant in dicioOrdenado.items():
                textRet += "'" + str(chave) + "'"+ "\t" + str(quant) + "\n"
    
            return textRet
        else:
            textRet += "alfabeto tem 0 símbolos\n"
            return textRet

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
        if len(self.corpus) > 0:
            if self.N(t) == None:
                nt = 0
            else:
                nt = self.N(t)
    
            if self.N(t[:-1]) == None:
                ntz = 0
            else:
                ntz = self.N(t[:-1])
    
            return (nt + 1)/(ntz + len(self.alphabet()))
        else:
            return 0