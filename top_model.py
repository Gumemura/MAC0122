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
    monitores e colegas). Com exceção de material de MAC0122, caso
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
# MarkovModel(), MarkovModel.laplace(), __str__()
from markov_model import MarkovModel

# math.log()
import math

class TopModel:
    def __init__(self, k, dict_corpora):
        self.k = k
        self.dict_corpora = dict_corpora

    def __str__(self):
        print_ret = ''
        for elem in self.dict_corpora:
            print_ret += str(MarkovModel(self.k, self.dict_corpora[elem])) + "\n"

        return print_ret

    def modelo(self, nome_modelo):
        if nome_modelo not in self.dict_corpora:
            print("modelo(): modelo '" + str(nome_modelo) +"' não foi definido")
            return
        else:
            return MarkovModel(self.k, self.dict_corpora[nome_modelo])

    def verossimilhanca_total(self, nome_modelo, citacao):
        if nome_modelo not in self.dict_corpora:
            print("verossimilhanca_total(): modelo '" + str(nome_modelo) +"' não foi definido")
            return
        else:
            markov = self.modelo(nome_modelo)
            k = self.k + 1
            cont = 0
            indice = 0
            text = ''

            while indice < len(citacao):
                if indice + k >= len(citacao):
                    text = citacao[indice:] + citacao[:(indice + k) - len(citacao)]
                else:
                    text = citacao[indice:indice + k]

                cont += math.log(markov.laplace(text))

                indice += 1

            return cont

    def media_verossimilhanca(self, nome_modelo, citacao):
        if nome_modelo not in self.dict_corpora:
            print("media_verossimilhanca(): modelo '" + str(nome_modelo) +"' não foi definido")
            return
        else:
            return (self.verossimilhanca_total(nome_modelo, citacao))/len(citacao)

    def top_model(self, citacao):
        dict_tm = (self.dict_corpora).copy()

        for elem in dict_tm:
            dict_tm[elem] = self.media_verossimilhanca(elem, citacao)

        return max(dict_tm, key = dict_tm.get), max(dict_tm.values())