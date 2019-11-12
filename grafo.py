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

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#-----------------------------------------------------------------
class Grafo:
    '''
        Siga as especificações do enunciado para construir a classe Grafo.

        Coloque o seu código a seguir.
    '''
    def __init__(self, doc = "", separador = " "):
        self.doc = doc
        self.grafo = []
        self.vert = []
        self.separador = separador

        if self.doc != '':
            for line in open(self.doc, 'r', encoding = "utf8"):
                list_temp = []
                param_inic = 0
    
                for i in range(len(line)):
                    if line[i] == self.separador:
                        list_temp.append(line[param_inic:i])
                        param_inic = i + 1
                    elif i == len(line) - 1:
                        if line[i] == '\n':
                            list_temp.append(line[param_inic:len(line) - 1])
                        else:
                            list_temp.append(line[param_inic:])
    
                self.grafo.append(list_temp)
    
        for i in range(len(self.grafo)):
            self.vert.append(self.grafo[i][0])

        temp_graf = []
        for i in range(len(self.grafo)):
            for l in range(1, len(self.grafo[i])):
                if self.grafo[i][l] not in self.vert:
                    self.vert.append(self.grafo[i][l])
                    temp_graf.append(self.grafo[i][l])
                    temp_graf.append(self.grafo[i][0])
                    self.grafo.append((temp_graf).copy())
                    temp_graf.clear()



    def __str__(self):
        textRet = ''

        for elem in self.grafo:
            for i in range(len(elem)):
                textRet += elem[i]
                if i == 0:
                    textRet += " \t| "
                elif i != len(elem) - 1:
                    textRet += ", "
            textRet += '\n'
        return textRet

    def insira_aresta(self, v, w):
        if (type(v) != str or type(w) != str) or (v == '' or w == ''):
            print('Caracteres inválidos. Insira apenas strings não vazias')
        else:
            def insere_aresta_sub(v, w):
                if v not in self.vert:
                    self.vert.append(v)
                    self.grafo.append([v, w])
                else:
                    for i in range(len(self.grafo)):
                        if self.grafo[i][0] == v:
                            self.grafo[i].append(w)
                            break
            insere_aresta_sub(v, w)
            insere_aresta_sub(w, v)

    def tem_vertice(self, v):
        if v in self.vert:
            return True
        else:
            return False

    def V(self):
        return len(self.vert)

    def A(self):
        #REVER!!
        quant = 0
        for elem in self.grafo:
            quant += len(elem) - 1

        return quant//2


    def vertices(self):
        return self.vert

    def adjacentes(self, v):
        for i in range(len(self.grafo)):
            if self.grafo[i][0] == v:
                return self.grafo[i][1:]

    def grau(self, v):
        return len(self.adjacentes(v))

    def tem_aresta(self, v, w):
        for i in range(len(self.grafo)):
            if self.grafo[i][0] == v:
                if w in self.grafo[i]:
                    return True
                else:
                    return False





