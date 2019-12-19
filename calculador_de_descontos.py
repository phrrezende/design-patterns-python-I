from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_500_reais, Sem_desconto
class Calculador_de_descontos(object):

	def calcula(self, orcamento):
		desconto = Desconto_por_cinco_itens(
			Desconto_por_mais_de_500_reais(Sem_desconto())
			).calcula(orcamento)

		return desconto

if __name__ == '__main__':

	from orcamento import Orcamento,Item

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Item-1',100))
	orcamento.adiciona_item(Item('Item-1',50))
	orcamento.adiciona_item(Item('Item-1',400))
	

	calculador = Calculador_de_descontos()
	desconto = calculador.calcula(orcamento)

	print('Desconto calculado %s' % (desconto))