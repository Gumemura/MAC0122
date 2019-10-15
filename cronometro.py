# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#
# MAC0122 PrincÃ­pios de Desenvolvimento de Algoritmos
#
#--------------------------------------------------------------------

# importa a classe Cliente e as funÃ§Ãµes mergeX() e mergesortX()
from cliente import *

# para teste da classe Cliente
import random  

# math.log2
import math

# para cronometrar
import time

NMAX = 2**18

#------------------------------------------------------------
def main(args=None):
    ''' (None) -> None
    Essa funÃ§Ã£o main() compara os tempos de execuÃ§Ãµes dos 
    mÃ©todos Cliente.distancia() e Cliente.distanciaX().
    Cliente.distanciaX() Ã© baseado em uma adaptaÃ§Ã£o do 
    mergesort().

    VocÃª pode alterÃ¡-la e incluir os seus prÃ³prios testes.
    '''
    # para podermos reproduzir os testes
    random.seed(0)

    # lst de filmes
    n = 16
    print("     n   distancia  distanciaX  transposicÃµes     n(n-1)/2      n lg(n)")
    while n < NMAX:
        print("%6s"%n, end="")
        
        # crie listas representado as classificaÃ§Ãµes
        lst0 = [i for i in range(n)]
        lst1 = lst0[:]
        random.shuffle(lst0)
        lst2 = lst1[:] # clone
        
        # crie clientes 
        cliente0 = Cliente("cliente 0")
        cliente0.put_classificacao(lst0)
        
        cliente1 = Cliente("cliente 1")
        cliente1.put_classificacao(lst1)
        
        cliente2 = Cliente("cliente 2")
        cliente2.put_classificacao(lst2)

        # cronometre tempo de distancia()
        inicio = time.time()
        dist = cliente0.distancia(cliente1)
        fim = time.time()
        print("%10.3fs"%(fim-inicio), end="")
        
        # cronometre tempo de distancia()
        inicio = time.time()
        distX = cliente0.distancia(cliente1)
        fim = time.time()
        print(" %10.3fs"%(fim-inicio), end="")

        print("    %10d    %10d   %10d"%(dist,n*(n-1)/2, int(n*math.log2(n))))
        
        if dist != distX:
            print("SOCORRO! distancia() = %s != %s = distancia()"%(dist, distX))

        n *= 2

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()
