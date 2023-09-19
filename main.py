from FormataMoeda.utilidades import moeda
from FormataMoeda.utilidades import dado

#main
p = dado.lerDinheiro('Digite o preço: R$')
moeda.resumo(p, 10, 13)

