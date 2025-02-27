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
def crie_imagem(nlin, ncol, valor):
    lista = list()

    ''' (int, int, obj) -> list

    Recebe dois inteiros nlin e ncol e um valor. 
    Cria e retorna uma imagem de dimensão nlin x ncol com valor em cada 
    posição.

    Exemplos:
    >>> t = crie_imagem(3,4,-1)
    >>> t
    [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
    >>> tt = crie_imagem(3,3,0)
    >>> tt
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> 
    '''
    #print("crie_imagem(): Vixe! Essa função ainda não foi feita.")

    for c in range(ncol):
        lista.append(valor)

    lista = [lista] * nlin

    return(lista)

#--------------------------------------------------------------------------
def copie_imagem(dest, orig):
    ''' (list, list) -> None

    Recebe duas imagens de mesma dimensão e copia o conteúdo de orig para dest.

    Exemplo:

    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = [[11, 22, 33],[44, 55, 66]]
    >>> copie_imagem(tt, t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 777
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[777, -122, 3], [1, 2, 3]]
    '''
    #print("copie_imagem(): Vixe! Essa função ainda não foi feita.")

    if len(dest) > len(orig):
        del dest[-(len(dest) - len(orig)):]
    elif len(dest) < len(orig):
        for a in range(len(orig) - len(dest)):
            dest.append(orig[-a])

    for i in range(0, len(dest)):
        dest[i] = orig[i]



#--------------------------------------------------------------------------
def clone_imagem(imagem):
    lista_Clone = list()
    ''' (list) -> list

    Recebe uma imagem e retorna uma cópia/clone da imagem

    Exemplo:
    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = clone_imagem(t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 111111
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[111111, -122, 3], [1, 2, 3]]
    >>> 
    '''
    #print("clone_imagem(): Vixe! Essa função ainda não foi feita.")

    lista_Clone = imagem[:]
    return lista_Clone

#--------------------------------------------------------------------------
def recorte_imagem(imagem, tlx, tly, brx, bry):
    #PENDENTE
    mini_list = list()
    transferidor = list()
    ''' (list, int, int, int, int) -> list

    Recebe uma imagem e as coordenadas (tlx, tly) do ponto TL (Top-Left) 
    e (brx, bry) do ponto BR (Bottom-Right), representando um retângulo 
    de cantos TL e BR. A função cria e retorna uma imagem de dimensão
    (brx-tlx) x (bry-tly), com conteúdo igual ao do retângulo TLxBR. 
    Observe que os pontos na linha brx e coluna bry não fazem parte do retângulo.

    Exemplo:
    >>> recorte_imagem([[1, 99, 3, 4, 5], 
                    [1, 88, 3, 4, 5], 
                    [1, 77, 3, 4, 5],    
                    [1, 66, 3, 4, 5] ], 0, 1, 3, 4)

                                    tlx tly brx bry
                                     0   1   3   4

    [[2,3,4], [2,3,4], [2,3,4]]
    >>> recorte_imagem([[1, 2, 3, 4, 5], 
                    [6, 7, 8, 9, 0], 
                    [0, 9, 8, 7, 6], 
                    [1, 2, 3, 4, 5] ], 1, 1, 3, 3)
    [[7,8], [9,8]]
    '''
    #print("recorte_imagem(): Vixe! Essa função ainda não foi feita.")

    for l in range(tlx, brx):
        print("a")
        for c in range(tly, bry):
            transferidor.append(imagem[l][c])

        mini_list.append(transferidor.copy())
        del transferidor[:]

    return mini_list

#--------------------------------------------------------------------------
