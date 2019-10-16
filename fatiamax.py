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
    monitores e colegas). Com exceção de material de MAC0122, 
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

#--------------------------------------------------------
def fatia_max(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

    soma_max == sum(v[e,d]) é a maior soma de uma fatia 
    v[i:j] com p <= i <= j <= r.
    '''
    soma_temp = 0
    soma_max = 0
    incremento = 0
    i = p
    j = r

    while p < r:
        for n in range(p, r):
            soma_temp += v[n]
            if soma_temp > soma_max:
                soma_max = soma_temp
                i = p
                j = n + 1
        incremento += 1
        soma_temp = 0
        p += 1

    return soma_max, i, j

#--------------------------------------------------------
def fatia_max_meio(p, q, r, v):
    '''(int, int, int, list) -> int, int, int

    RECEBE números inteiros p < q < r e uma lista v[p:r] de 
    números inteiros e RETORNA valores inteiros 
    soma_max, e, d tais que 

        soma_max==sum(v[e:d]) é a maior soma de uma fatia 
        v[i:j] com p <= i < q < j <= r.
    '''




    return -1, -1, -1

#--------------------------------------------------------
def fatia_max_div_conq(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    '''
    print("Vixe! Ainda não fiz a função fatia_max_div_conq()...")
    return -1, -1, -1



def main():

    v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    #v = [0,0,0,0,0,0,0,0,0,0]
    print(v, "\n")
    print("Fatia: [0:10]\nEsperado: (187, 2, 7)\nResultado: ",fatia_max(0,10,v), "\n")

    print("Fatia: [2:9]\nEsperado: (187, 2, 7)\nResultado: ",fatia_max(2,9,v), "\n")

    print("Fatia: [3:9]\nEsperado: (155, 5, 7)\nResultado: ",fatia_max(3,9,v), "\n")

    print("Fatia: [7:10]\nEsperado: (84, 9, 10)\nResultado: ",fatia_max(7,10,v), "\n")

main()
