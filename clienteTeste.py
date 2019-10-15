#--------------------------------------------------------------------
#
# MAC0122 PrincÃ­pios de Desenvolvimento de Algoritmos
#
#--------------------------------------------------------------------

# classe Cliente
from cliente import Cliente

# random.shuffle() usado para testar a classe Cliente
import random  

#####################################################################
# CONSTANTES
# cada caractere representa o nome de um filme para testes
FILMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

#------------------------------------------------------------
def main(args=None):
    ''' (None) -> None

       Essa funÃ§Ã£o main estÃ¡ aqui para testar a classe Cliente.
       VocÃª pode alterÃ¡-la e incluir os seus prÃ³prios testes.
    '''
    # para podermos reproduzir os testes
    random.seed(0) # para outros testes, troco valor

    # lst de filmes
    lst_filmes = args
    if lst_filmes == None: lst_filmes = FILMES
    n_filmes     = len(lst_filmes)

    print("Cliente(): iniciando teste...")
    lst_clientes = []
    lst_clientes.append(Cliente("T'Challa"))
    lst_clientes.append(Cliente('Nakia'))
    lst_clientes.append(Cliente('Natasha Romanoff'))
    print("Cliente() nÃ£o explodiu... :-)")
    
    print("put_classificacao(): iniciando teste...")
    lst_clientes[0].put_classificacao(lst_filmes[:5]) 
    random.shuffle(lst_filmes)
    lst_clientes[1].put_classificacao(lst_filmes[:10])
    random.shuffle(lst_filmes) 
    lst_clientes[2].put_classificacao(lst_filmes[:7])
    print("put_classificao() nÃ£o explodiu... :-)")

    
    print("__str__(): iniciando teste:")
    for cliente in lst_clientes:
        print(cliente)
    print("__str__(): nÃ£o explodiu... :-)\n")
    
    print("get_nome() e get_classificacao(): iniciando teste")
    for cliente in lst_clientes:
        print("%s: %s"%(cliente.get_nome(), cliente.get_classificacao())) 
    print("get_nome() e get_classificacao() nÃ£o explodiu :-)\n")
        
    print("distancia(): iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("distancia(%s,%s)= %s"%(cliente0.get_nome(),
                                          cliente1.get_nome(),
                                          cliente0.distancia(cliente1)))
    print("distancia(): nÃ£o explodiu... :-)")

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()
