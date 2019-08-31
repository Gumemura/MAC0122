class Fracao:
    #------------------------------------
    def __init__(self, num = 0, den = 1):
        """ (Fracao, int, int) -> Fracao

        Construtor: cria um objeto Fracao.
        """
        self.num = num
        self.den = den
        self.simplifique()

    #------------------------------------
    def __str__(self):
        """ (Fracao) -> str

        Retorna o string que print() usa para imprimir um
        Fracao.
        """
        if self.den == 1:
            texto = "%d" %self.num
        else:
            texto = "%d/%d" %(self.num,self.den)
        return texto

    #-------------------------------------
    def simplifique(self):
        """ (Fracao) -> None

        Recebe uma fracao e altera a sua representacao
        para a forma irredutivel.
        """
        comum = mdc(self.num,self.den)
        self.num //= comum
        self.den //= comum
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

    #-------------------------------------
    def get(self):
        """ (Fracao) -> int, int

        Recebe uma fracao e retorna o seu numerador e o
        seu denominador.
        """
        return self.num, self.den

    #--------------------------------------
    def put(self, novo_num, novo_den):
        """ (Fracao) -> None

        Recebe uma fracao e dois inteiros novo_num e
        novo_den e modifica a fracao para representar
        novo_num/novo_den.
        """
        self.num = novo_num
        self.den = novo_den
        self.simplifique()

    #------------------------------------
    def __add__(self,other):
        """ (Fracao,Fracao) -> Fracao

        Retorna a soma dos racionais `self` e `other`.
        Usado pelo Python quando escrevemos Fracao + Fracao
        """
        novo_num = self.num*other.den + self.den*other.num
        novo_den = self.den*other.den
        f = Fracao(novo_num,novo_den)
        return f

    #------------------------------------
    def __sub__(self, other):
        """ (Fraco,Fracao) -> Fracao

        Retorna a diferenca das fracoes `self` e `other`.
        Usado pelo Python quando escrevemos Fracao - Fracao
        """
        novo_num = self.num*other.den - self.den*other.num
        novo_den = self.den*other.den
        f = Fracao(novo_num,novo_den)
        return f

    #------------------------------------
    def __mul__(self, other):
        """ (Fracao,Fracao) -> Fracao

        Retorna o produto dos racionais `self` e `other`.
        Usado pelo Python quando escrevemos Fracao * Fracao
        """
        novo_num = self.num * other.num
        novo_den = self.den * other.den
        f = Fracao(novo_num, novo_den)
        return f

    #-------------------------------------
    def __truediv__(self, other):
        novo_num = self.num * other.den
        novo_den = self.den * other.num
        f = Fracao(novo_num, novo_den)
        return f

    #-------------------------------------
    def __eq__(self, other):
        prim_num = self.num  * other.den
        seg_num  = other.num * self.den
        return prim_num == seg_num

#-----------------------------------------
def mdc(m, n):
    """ (int, int) -> int
    Recebe dois inteiros m e n e retorna o
    mdc de m e n.

    Retorna 0 indicando que n e m são 0.
    """
    if n < 0: n = -n
    if m < 0: m = -m
    if n == 0: return m
    r = m%n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n