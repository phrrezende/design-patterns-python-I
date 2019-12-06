class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento):
		imposto_calculado = orcamento.valor * 0.1
		print imposto_calculado

if __name__ == '__main__':
	from orcamento import Orcamento

	calculador = Calculador_de_impostos()
	orcamento = Orcamento(500)

	calculador.realiza_calculo(orcamento)