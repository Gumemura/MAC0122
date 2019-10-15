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
        Copie a sua classe Cliente do EP10 para aqui.

        Estenda essa classe adicionando os métodos:
           em_comum() e distanciaX()
        como especifado no enunciado.
 
        Coloque o seu código a seguir.
    '''

def main():
    print("mergeX(), EP11: iniciando teste...")
    A = [3,  7, 10, 14, 18]
    B = [2, 11, 16, 20, 23]
    C = A + B
    print("    A: ", A)
    print("    B: ", B)
    print("    C  antes: ", C)
    print("    mergeX('A+B'): retornou ", mergeX(C, 3,6,7))
    print("    C depois: ", C)

    print("mergesortX(), EP11: iniciando teste...")
    V = [10, 14, 18, 7, 3, 20, 23, 11, 2, 16]
    print("V  antes: ", V)
    print("mergesortX(V): ", mergesortX(V,0,10))
    print("V depois: ", V)
    print("mergesortX(): não explodiu sorriso\n")

main()



