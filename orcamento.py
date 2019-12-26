
from abc import ABCMeta, abstractmethod
class Estado_de_um_orcamento(object, metaclass=ABCMeta):

	def __init__(self):
		self.desconto_ja_aplicado = False

	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass

	@abstractmethod
	def aprova(self, orcamento):
		pass

	@abstractmethod
	def reprova(self, orcamento):
		pass

	@abstractmethod
	def finaliza(self, orcamento):
		pass


class Em_aprovacao(Estado_de_um_orcamento):

	def aplica_desconto_extra(self, orcamento):
		if self.desconto_ja_aplicado is False:
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
			self.desconto_ja_aplicado = True
		else:
			raise Exception("Desconto extra já aplicado para orçamento com situação Em Aprovação.")

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		raise Exception("Orçamento em aprovação não pode ser finalizado.")

class Aprovado(Estado_de_um_orcamento):

	def aplica_desconto_extra(self, orcamento):
		if self.desconto_ja_aplicado is False:
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.05) 
			self.desconto_ja_aplicado = True
		else:
			raise Exception("Desconto extra já aplicado para orçamento com situação Aprovado.")

	def aprova(self, orcamento):
		raise Exception("Orçamento já está com estado aprovado.")

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):

	def aplica_desconto_extra(self, orcamento):
		raise Exception("Orçamentos reprovados não receberão desconto extra.")

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		raise Exception("Orçamento já está com estado reprovado.")

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()

class Finalizado(Estado_de_um_orcamento):

	def aplica_desconto_extra(self, orcamento):
		raise Exception("Orçamentos finalizados não receberão desconto extra.")

	def aprova(self, orcamento):
		raise Exception("Orçamentos finalizados não podem ser aprovados.")

	def reprova(self, orcamento):
		raise Exception("Orçamentos finalizados não podem ser reprovados.")

	def finaliza(self, orcamento):
		raise Exception("O estado atual do orçamento já é finalizado.")

class Orcamento(object):

	def __init__(self):

		self.__itens = []
		self.estado_atual = Em_aprovacao()
		self.__desconto_extra = 0

	@property
	def desconto_extra(self):
		return self.__desconto_extra
	

	def aprova(self):
		self.estado_atual.aprova(orcamento)

	def reprova(self):
		self.estado_atual.reprova(orcamento)

	def finaliza(self):
		self.estado_atual.finaliza(orcamento)

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)	
	
	def adiciona_desconto_extra(self, desconto):
		self.__desconto_extra += desconto

	@property 
	def valor(self):
		total = 0.0
		for item in self.__itens:
			total += item.valor
		return total - self.__desconto_extra

	def obter_itens(self):
		return tuple(self.__itens)

	@property
	def total_itens(self):
		return len(self.__itens)

	def adiciona_item(self, item):
		self.__itens.append(item)



class Item(object):

	def __init__(self, nome, valor):

		self.__nome = nome
		self.__valor = valor
	
	@property
	def valor(self):
		return self.__valor

	@property
	def nome(self):
		return self.__nome

if __name__ == "__main__":

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Item-1',100))
	orcamento.adiciona_item(Item('Item-1',50))
	orcamento.adiciona_item(Item('Item-1',400))

	print(orcamento.valor)
	orcamento.aplica_desconto_extra()
	print(orcamento.valor)
	orcamento.estado_atual = Aprovado()
	orcamento.aplica_desconto_extra()
	print(orcamento.valor)
	orcamento.aplica_desconto_extra()
	
	
	
