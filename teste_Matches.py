#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   Cliente para a classe Matches.
'''

# importa a classe Matches para ser cronometrada
from matches import Matches

# para o cronÃ´metro
import time

# para o gerador de numeros aleatÃ³rios
import random

# expressÃµes regulares
# veja https://docs.python.org/3/library/re.html
# veja https://www.regular-expressions.info/
import re

#------------------------------------------------------
# CONSTANTES

# semente default para o gerador de ná¸¿eros aleatÃ³rios
SEMENTE = 1234567

# usamos os primeiros 10 milhÃµes de dÃ­gitos de pi para testes
ARQUIVO = "pi-10million.txt"

MIN = 2500

#------------------------------------------------------
def main():
    # para o gerador de numeros aleatorios 
    semente = SEMENTE   

    # inicialize a semente do gerador de nÃºmeros aleatorios 
    random.seed(semente)

    # leia a string com os 10 milhÃµes de dÃ­gitos de pi
    print("main(): lendo a string s")
    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        pi = arq.read()
    len_pi = len(pi)    
    print("main(): string de comprimento %s lida"%len_pi)
    
    # imprima cabeÃ§alho
    print("                   Consumo de tempo")
    print("                   ----------------")
    print("         n     Matches()   matches()  re.finditer()")

    # faÃ§a testes para cada fatia pi[0:n]
    n = MIN
    while n < 2*len_pi:
        # pedaÃ§o da string que serÃ¡ considerado
        if n > len_pi:
            fatia_pi = pi
            n = len_pi
        else: fatia_pi = pi[0:n]
        
        # cronometre a criaÃ§Ã£o de um objeto da classe `Matches`
        inicio = time.time()
        matches = Matches(fatia_pi)
        fim = time.time()
        t_criacao = fim-inicio

        # cronometre os tempo de __n consultas__
        t_consulta = 0 # para Matches.matches()
        t_re = 0       # para re.finditer()
        for i in range(n):
            # crie uma string com 10 dÃ­gitos
            s = string_rand(10)
            
            # procure a string
            inicio = time.time()
            lst = matches.matches(s)
            fim = time.time()
            t_consulta += fim-inicio

            if n <= 40000: 
                # procure usando a biblioteca re
                # ver https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
                inicio = time.time()
                lst_re = [k.start() for k in re.finditer('(?=%s)'%s, fatia_pi)]
                fim = time.time()
                t_re += fim - inicio

                if lst != lst_re:
                    print("Vixe!\nDeu ruim!\nSocorro!")
                    print("n =", n, "s =", s)
                    return
            
        # mostre resultado
        print("%10d %10.2fs %10.2fs %10.2fs" %(n, t_criacao, t_consulta, t_re))
        
        # proximo valor de n
        n *= 2

#------------------------------------------------------------
#  F U N C Ãƒ O   A U X I L I A R 
#------------------------------------------------------------
def string_rand(n):
    '''(int) -> str

    Recebe um inteiro nÃ£o negativo n e cria uma string aleatÃ³ria
    com n digitos.
    '''
    digito = "0123456789"
    s = ""
    for i in range(n):
        s += digito[random.randrange(10)]
    return s

#-----------------------------------------------------------    
if __name__ == "__main__":
    main()
