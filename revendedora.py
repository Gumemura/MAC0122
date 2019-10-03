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

        copEn = (encomenda).copy()
        copSE = (self.estoque).copy()

        def verifica_atende(estoque, pedido):
            if len(pedido) > 0:
                for i in range(len(estoque)):
                    if pedido[0] <= estoque[i]:
                        estoque[i] -= pedido[0]
                        pedido.pop(0)
                        verifica_atende(estoque, pedido)
                        break
                    elif i == (len(estoque) - 1):
                        return 0
                        break
            if len(pedido) == 0:
                return 1

        if verifica_atende(copSE, copEn) == 1:
            tamanhoEnco = len(encomenda)
            for l in range(tamanhoEnco):
                for i in range(self.len):
                    if encomenda[0] <= self.estoque[i]:
                        self.estoque[i] -= encomenda[0]
                        listRet.append(i)
                        encomenda.pop(0)
                        tamanhoEnco = len(encomenda)
                        break

            return listRet