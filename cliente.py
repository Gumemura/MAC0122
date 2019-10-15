# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
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

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

#-------------------------------------------------------------------
#
# Funções administrativas mergeX() e mergesortX()
#
#-------------------------------------------------------------------
def mergeX(v, e = 0, m = None, d = None):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''

    contBreak = 0
    cont = 0
    indice = e

    if d == None:
        d = len(v) - 1

    if len(v) > 1 or d - e > 1:
        while contBreak < d - e:
            if indice < d - 1:
                if v[indice] > v[indice + 1]:
                    storage = v[indice]
                    v[indice] = v[indice + 1]
                    v[indice + 1] = storage
                    cont += 1
                else:
                    contBreak += 1

                indice += 1

                if contBreak == len(v) - 1:
                    break
            else:
                indice = 0
                contBreak = 0

    
    return cont


def mergesortX(v, e=None, d=None):
    ''' (list, int, int) -> int

    Recebe uma lista v e dois inteiros que definem 
    um segmento de v que deve ser ordenado. 

    Quando e e d são None, a lista inteira deve ser ordenada.

    A função retorna o número de transposições resultantes da ordenação 
    de v[e:d].
    '''
    return mergeX(v, e, 0, d)


#-----------------------------------------------------------


class Cliente:
    '''
        Siga as especificações do enunciado para 
        construir a classe Cliente.

        Coloque o seu código a seguir.
    '''

    def __init__(self, nome):
        self.nome = nome
        self.filmes = []

    def put_classificacao(self, filmes):
        self.filmes = filmes

    def __str__(self):
        report = self.nome + "\n"

        if len(self.filmes) >= 0:
            for i in range(len(self.filmes)):
                report += "%d: %s \n" %(i, str(self.filmes[i]))

        return report

    def get_nome(self):
        return self.nome

    def get_classificacao(self):
        if len(self.filmes) > 0:
            list_clone = (self.filmes).copy()
            return list_clone

    def distanciaX(self, clienteOther):
        lista_propria = self.get_classificacao()
        lista_other = clienteOther.get_classificacao()

        i_da_LP = i_da_LO = 0

        while i_da_LP < len(lista_propria):
            if lista_propria[i_da_LP] not in lista_other:
                lista_propria.pop(i_da_LP)
            else:
                i_da_LP += 1

        while i_da_LO < len(lista_other):
            if lista_other[i_da_LO] not in lista_propria:
                lista_other.pop(i_da_LO)
            else:
                i_da_LO += 1


        i_da_LP = cont = 0
        while lista_propria != lista_other:
            indexLO = lista_other.index(lista_propria[i_da_LP])

            if i_da_LP < indexLO:
                transp = -1
            else:
                transp = 1

            while lista_propria[i_da_LP] != lista_other[i_da_LP]:
                reserva = lista_other[indexLO]
                lista_other[indexLO] = lista_other[indexLO + transp]
                lista_other[indexLO + transp] = reserva
                indexLO += transp
                cont += 1

            i_da_LP += 1

        return cont

    def em_comum(self, other):
        filmes_em_comum = []

        for elem in other.filmes:
            if elem in self.filmes:
                filmes_em_comum.append(self.filmes.index(elem))

        return filmes_em_comum



