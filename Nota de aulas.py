MAC 0122

Monitorias: 4ª, 5ª, e 6ª, 12:00 as 13:00, na sala 2 do CEC


>>>>>>> Aula 2 - 06/08/2019

aula passada: cálculo de numero harmonico 

def -> cria função

class -> cria classe

def __init__(self) -> sempre que a função estiver entre 4 underlines (orelhas), é pq ele é da biblioteca do python

class Frac:

	def __init__(self, num, den):
		''' Inicializa os atributos da função'''
		self.num = num
		self.den = den

	def __str__(self):
		s = '%d/%d' %(self.num, self.den)
		return s

tipos de erro em programação: 
	sintaticos: erro de ditacao, falha na grafia do texto de linguagem formal. Exemplo: print("fdfd)
	Runtime Errors: erros evidenciados na exeucao do programa. Geralmente sao erros de logica. Exemplo: usar um variavel cuja existencia esta protegida por if, sem replicar essa condicao em seu uso 
	Semantico: Erros que nao sao destacados pelo compilador mas percebidos pelo ususario/programador. Exemplo: usar uma variavel quando na verdade se desejava outra


>>>>>>> Aula 3 - 08/08/2019
	n teve nada de muito relevante que devesse ser anotado

>>>>>>> Aula 4 - 13/08/2019
	n fui :(

>>>>>>> Aula 5 - 15/08/2019
	Condutor da aula = Exercicio: verificar se uma string esta bem feita ou nao. Ou seja, se cada parenteses, colchetes e chaves sao fechadas na ordem inversam em foram abertas
	Ex.: bem formada: "([], {[]})"
		 mau formada: "()["

	- Pilhas, ou Stack em ingles

		#dicionario: estudar. Parece uma vetor de duas colunas, uma lista de pares
		A solucao para o problema é algo assim:

		s = input("digite o texto a ser analisado").stip() --> o stip limpa os espaços em branco

		abres = '([{'
		fechas = ')]}'

		pilha = stack()   --> no stakc temos dois metodos principais: push("para adc elemento"); pop("que remove"); peer("espia o topo da pilha"); is_empty() "ve se esta vazia"
							  Na verdade, a Stack() nao é uma classe natural de python. temos q implementa-la
		
		dicio = {']':'[', ')':'(', '}':'{'}		--> o tipo Dicionario tmbm n existe, vamos implementa-la

		for i in range(len(s)):
			if s[i] in abres:
				pilha.push(s[i])

>>>>>>> Aula 6 - 20/08/2019
	nao fui :( o mongol aqui esqueceu de ligar o despertador


>>>>>>> Aula 7 - 22/08/2019
	Aula de hj - array

	desenvolvimento da classe Arry2D = dois parametros: tuble, com as dimencoes da matrix e um int (ou float) com os valores das celular
	
	para fazer a classe Array, nao precisa fazer uma matriz, mas um lista. na hora de dar o print, percorremos todos os itens da lista de metemos um /n pra cada linha 

	=
>>>>>>> Aula 8 - 27/08/2019
	continuacao de array.
	array é basicamente uma representacao de matrizes, uma lista bidimensional
	vista = exibicao dos valores da array mas de forma diferente

>>>>>>> Aula 9 - 29/08/2019
	exemplo: como determinar o caminha mais curto entre duas cidade

	Fazer uma rede: uma matrix cujos indices sao as cidades. se a celular for 1, as cidade indicadas no indice sao vizinhas

	Fila: uma pilha ao contrario

>>>>>>> Aula 10 - 10/09/2019
	Revendo aula passada: fazendo um mini google maps
	Array, onde cada linha X coluna é uma cidade. Caso haja caminho entre ambos, valor 1. Caso contrario, valor 0
	Dica para criar matrizes:
		for i in range(n):
			matriz.append([0] * n)


>>>>>>> ESTUDAR PRA PROVA
	Numeros posfixo
	Fila
	Pilhas

	Formas de criar uma array

	import numpy as np
		a = np.array('lista', 'tipo primitivo dos objetos')  --> exemplo: a = np.array([[0,1,2],[3,4,5]], int)
		a = np.array(range('valor a maximo da array'))
		a = np.full(('tuple com as dimensoes da array'), 'valor')

	Principais funções com array
		nomeDaArray.reshape(3,4) -> altera as dimensoes da array

	Propriedades da arra
		nomeDaArray.shape() -> tuple, dimensoes da array 
		nomeDaArray.size() -> int, quantidade de elementos contidos na array (multiplicacao dos termos da tuple retornada por shape)
		
>>>>>>> Aula 11 - 17/09/2019
	joguinho das argolinhas nas bases
	recusao, funcao sendo chamda dentro da propria funcao

>>>>>>> Aula 12 - 19/09/2019
	3 regras da recursao
		- RESOLVER: Se vc sabe resolver sem recursao, entao resolva assim
		- REDUZIR: use a funcao p se aproximar de um caso base
		- RECORRER:	resolva o problema usando a resposta do problema menor





