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

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
class Polinomio:
    def __init__(self, coefs):
        self.coefs = coefs

    def __str__(self):
        coefsOrdenados = list()
        for i in range(len(self.coefs) - 1, -1, -1):
            coefsOrdenados.append(self.coefs[i])

        polinomioReturn = str()
        redutor = 1
        sinal = ""

        if sum(coefsOrdenados) == 0:
            polinomioReturn = "  0"
        else:
            for elem in(coefsOrdenados):
                if elem != 0:
                    if elem >= 0:
                        if redutor > 1:
                            sinal = "+"
                    else:
                        sinal = "-"
        
                    if elem < 0:
                        elem *= -1
        
                    if redutor < len(coefsOrdenados):
                        polinomioReturn += (" " + sinal + " %sx^%s" %(elem, len(coefsOrdenados ) - redutor))
    
                redutor += 1
    
            if coefsOrdenados[-1] != 0:
                if coefsOrdenados[-1] > 0:
                    sinal = "+"
                elif coefsOrdenados[-1] < 0:
                    sinal = "-"
                    coefsOrdenados[-1] *= -1
                polinomioReturn += " " + sinal + " %s" %coefsOrdenados[-1]

        return polinomioReturn

    def grau(self):
        return len(self.coefs) - 1

    def coeficientes(self):
        return self.coefs

    def derive(self):
        derivada = self.coefs[1:len(self.coefs)]

        for i in range(1, len(derivada)):
            derivada[i] *= i + 1

        return Polinomio(derivada)

    def __call__(self, alpha):
        valor = 0
        exp = 0
        for coeficiente in self.coefs:
            valor += coeficiente * (alpha)**exp
            exp += 1

        return valor

    def __add__(self, poli):
        if type(poli) == int or type(poli) == float:
            poliSoma = (self.coefs).copy()
            poliSoma[0] += poli
        else:
            selfCoefCopia = self.coefs.copy()
            poliCoefCopia = poli.coefs.copy()
            poliSoma = list()

            if len(selfCoefCopia) > len(poliCoefCopia):
                for i in range(len(selfCoefCopia) - len(poliCoefCopia)):
                    poliCoefCopia.append(0)
            else:
                for i in range(len(poliCoefCopia) - len(selfCoefCopia)):
                    selfCoefCopia.append(0)
    
            for i in range(len(selfCoefCopia)):
                poliSoma.append(selfCoefCopia[i] + poliCoefCopia[i])
    
        return Polinomio(poliSoma)

    def __radd__(self, num):
        if type(num) == int or type(num) == float:
            numRadd = (self.coefs).copy()
            numRadd[0] += num
        return Polinomio(numRadd)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            otherSubtrai = (self.coefs).copy()
            otherSubtrai[0] -= other
        else:
            selfCoefCopia = self.coefs.copy()
            otherCoefCopia = other.coefs.copy()
            otherSubtrai = list()

            if len(selfCoefCopia) > len(otherCoefCopia):
                for i in range(len(selfCoefCopia) - len(otherCoefCopia)):
                    otherCoefCopia.append(0)
            elif(len(selfCoefCopia) < len(otherCoefCopia)):
                for i in range(len(otherCoefCopia) - len(selfCoefCopia)):
                    selfCoefCopia.append(0)
            elif(selfCoefCopia == otherCoefCopia):
                otherSubtrai.append(0)

            for i in range(len(selfCoefCopia)):
                otherSubtrai.append(selfCoefCopia[i] - otherCoefCopia[i])

        return Polinomio(otherSubtrai)

    def __rsub__(self, num):
        if type(num) == int or type(num) == float:
            numRsub = (self.coefs).copy()
            numRsub[0] -= num
        return Polinomio(numRsub)

    def __mul__(self, otherMul):
        if type(otherMul) == int or type(otherMul) == float:
            listProduto = (self.coefs).copy()
            for i in range(len(listProduto)):
                listProduto[i] *= otherMul

        else:
            selfCoefCopia = self.coefs.copy()
            otherMulCoefCopia = otherMul.coefs.copy()
    
            if len(selfCoefCopia) > len(otherMulCoefCopia):
                for i in range(len(selfCoefCopia) - len(otherMulCoefCopia)):
                    otherMulCoefCopia.append(0)
            elif len(selfCoefCopia) < len(otherMulCoefCopia):
                for i in range(len(otherMulCoefCopia) - len(selfCoefCopia)):
                    selfCoefCopia.append(0)
    
            tabelaResults = list()
            for i in range((len(selfCoefCopia) + len(otherMulCoefCopia)) - 1):
                linha = [0] * (len(selfCoefCopia) * len(otherMulCoefCopia))
                tabelaResults.append(linha)
    
            colunaTR = 0
            for i in range(len(selfCoefCopia)):
                for t in range(len(otherMulCoefCopia)):
                    tabelaResults[i + t][colunaTR] = selfCoefCopia[i] * otherMulCoefCopia[t]
                    colunaTR += 1
    
            coeficienteMul = 0
            listProduto = []
            for a in range(len(tabelaResults)):
                for b in range(len(tabelaResults[0])):
                    coeficienteMul += tabelaResults[a][b]
                listProduto.append(coeficienteMul)
                coeficienteMul = 0

            for i in range(1, len(listProduto)):
                if listProduto[-1] == 0:
                    listProduto.pop(-1)
                else:
                    break

        return Polinomio(listProduto)

    def __rmul__(self, otherRMul):
        listRProduto = (self.coefs).copy()
        for i in range(len(listRProduto)):
            listRProduto[i] *= otherRMul

        return Polinomio(listRProduto)

def main():
    # crie lista de coeficientes
    coefs = [5, 1, -2, 0, -3]
    # crie um objeto da classe polinomio
    print("1. criaÃ§Ã£o de polinÃ´mios")
    p = Polinomio(coefs) # __init__()
    coefs = [-1, -1, -1]
    print("polinomio p: %s"%p)     # __str__()
    print("grau de p %s"%p.grau()) # grau()
    print("coeficientes e p: %s\n"%p.coeficientes()) # coeficientes()

    
    #crie um polinomio que represente a derivada de p
    print("2. derivada de polinÃ´mios")
    dp = p.derive()  # __ derive__()
    print("derivada de p (=dp): %s"%dp) # __str__() 
   
    # crie um polinomio que represente a derivada de p
    ddp = dp.derive() # __derive__()
    print("derivada de dp (=ddp): %s"%ddp) # __str__()

    # coeficiente de p, dp e ddp 
    print("coeficientes de   p: %s"%p.coeficientes())
    print("coeficientes de  dp: %s"%dp.coeficientes())
    print("coeficientes de ddp: %s\n"%ddp.coeficientes())

    # calcule o valor dos polinÃ´mio
    print("3. valor de polinÃ´mios")
    valores = [0, 1, 0.5, 3] # depois tente com complex(1,1)
    for x in valores:
        print("p(%s) = %s," %(x, p(x)), end=" ")    # __call__() 
        print("dp(%s) = %s," %(x, dp(x)), end=" ")  # __call__() 
        print("ddp(%s) = %s" %(x, ddp(x)))          # __call__() 

    # calcule o valor dos polinÃ´mio
    print("\n4. adiÃ§Ã£o de polinÃ´mios")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print("p1     : %s"%p1)
    print("p2     : %s"%p2)
    p3 = p1 + p2  # __add__()
    print("p1 + p2: %s"%p3)
    p4 = p1 - p1  # __sub__()
    print("p1 - p1: %s"%p4)
    p5 = p1 + 1   # __add__()
    print("p1 + 1 : %s"%p5)
    p6 = 2 + p1   # __radd__()
    print(" 2 + p1: %s"%p6)

    '''4. adição de polinômios
    p1     : 3*x^4 - 2*x^2 + 1*x^1 + 5
    p2     : 1*x^2 + 5*x^1 - 2
    p1 + p2: 3*x^4 - 1*x^2 + 6*x^1 + 3
    p1 - p1: 0
    p1 + 1 : 3*x^4 - 2*x^2 + 1*x^1 + 6
     2 + p1: 3*x^4 - 2*x^2 + 1*x^1 + 7'''

    # calcule o produto de polinÃ´nios
    print("\n5. multiplicaÃ§Ã£o de polinÃ´mios")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print("p1     : %s"%p1)
    print("p2     : %s"%p2)
    p3 = p1 * p2   # __mul__()
    print("p1 * p2: %s"%p3)
    p4 = p1 * p1   # __mul__()
    print("p1 * p1: %s"%p4)
    p5 = p1 * -2   # __mul__()
    print("p1 * -2: %s"%p5)
    p6 = 3 * p1    # __rmul__()
    print(" 3 * p1: %s"%p6)
    
    '''5. multiplicação de polinômios
    p1     : 3*x^4 - 2*x^2 + 1*x^1 + 5
    p2     : 1*x^2 + 5*x^1 - 2
    p1 * p2: 3*x^6 + 15*x^5 - 8*x^4 - 9*x^3 + 14*x^2 + 23*x^1 - 10
    p1 * p1: 9*x^8 - 12*x^6 + 6*x^5 + 34*x^4 - 4*x^3 - 19*x^2 + 10*x^1 + 25
    p1 * -2:  - 6*x^4 + 4*x^2 - 2*x^1 - 10
     3 * p1: 9*x^4 - 6*x^2 + 3*x^1 + 15'''

        
#----------------------------------------------------------
if __name__ == "__main__":
    main()
