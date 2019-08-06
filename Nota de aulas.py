MAC 0122

Monitorias: 4ª, 5ª, e 6ª, 12:00 as 13:00, na sala 2 do CEC


	Aula 2 - 06/08/2019

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
