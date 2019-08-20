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
	nao vim :( o mongol aqui esqueceu de ligar o despertador


