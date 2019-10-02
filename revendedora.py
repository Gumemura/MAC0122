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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''

#------------------------------------------------------------
class Revendedora:
    ''' Recebe uma lista estoque com os comprimentos de rolos 
        disponíveis e atende pedidos fazendo controle desse 
        estoque.
    '''

    def __init__(self, estoque):
        self.estoque = estoque
        self.len = len(self.estoque)

    def __str__(self):
        relatorio = "Estoque possui %d rolo(s):\n" %len(self.estoque)
        for i in range(len(self.estoque)):
            relatorio += "\tRolo %d: %d m\n" %(i, self.estoque[i])

        return relatorio

    def atenda_encomenda(self, encomenda):
        listRet = []
        ie = 0
        ise = 0

        while ie < (len(encomenda)):
            if encomenda[ie] <= self.estoque[ise]:
                listRet.append(ise)
                self.estoque[ise] -= encomenda[ie]
                ise = 0
                ie += 1

            elif ise == (self.len - 1):
                ie += 1

            ise += 1

        if len(listRet) == len(encomenda):
            return listRet


























