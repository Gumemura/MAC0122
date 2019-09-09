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

        self.coefsOrdenados = []

        for i in range(len(coefs) - 1, -1, -1):
            self.coefsOrdenados.append(coefs[i])


    def __str__(self):
        polinomioReturn = ""
        redutor = 1
        sinal = ""

        for elem in(self.coefsOrdenados):
            if redutor > 1:
                if elem >= 0:
                    sinal = "+"

            if redutor < len(self.coefsOrdenados):
                polinomioReturn += (" " + sinal + "%sx^%s" %(elem, len(self.coefsOrdenados ) - redutor))
                redutor += 1
                sinal = ""

        if self.coefsOrdenados[-1] > 0:
            sinal = "+"

        polinomioReturn += " " + sinal + "%d" %self.coefsOrdenados[-1]

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


'''def main():
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

        
#----------------------------------------------------------
if __name__ == "__main__":
    main()'''
