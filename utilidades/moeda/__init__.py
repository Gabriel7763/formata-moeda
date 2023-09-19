def aumentar(preco=0, taxa=0, formata=False):
    '''
    Função para aumentar x porcento
    :param preco: Valor que foi passado
    :param taxa: A porcentagem
    :param formata: Opção para formatar o valor. False para não, True para sim
    :return: Retorna o valor normal ou formatado de acordo com o parametro 'formata'
    '''
    res = preco + (preco * taxa/100)
    return res if formata is False else moeda(res)


def reduzir(preco=0, taxa=0, formata=False):
    '''
    Função para diminuir x porcento
    :param preco: Valor que foi passado
    :param taxa: A porcentagem
    :param formata: Opção para formatar o valor. False para não, True para sim
    :return: Retorna o valor normal ou formatado de acordo com o parametro 'formata'
    '''
    res = preco - (preco * taxa/100)
    return res if formata is False else moeda(res)


def dobrar(preco=0, formata=False):
    """
    Função para dobrar um valor
    :param preco: Valor que foi passado
    :param formata: Opção para formatar o valor. False para não, True para sim
    :return: Retorna o valor normal ou formatado de acordo com o parametro 'formata'
    """
    res = preco*2
    return res if formata is False else moeda(res)


def metade(preco=0, formata=False):
    """
    Função para dividir um valor pela metade
    :param preco: Valor que foi passado
    :param formata: Opção para formatar o valor. False para não, True para sim
    :return: Retorna o valor normal ou formatado de acordo com o parametro 'formata'
    """
    res = preco/2
    return res if formata is False else moeda(res)


def moeda(preco=0,moeda="R$"):
    '''
    Função para formatar o valor
    :param preco: Valor que foi passado
    :param moeda: Tipo de moeda que será formatada
    :return: Retorna a formatação da moeda com duas casas decimais, substituindo . por ,
    '''
    return f'{moeda}{preco:.2f}'.replace('.',',').strip()


def resumo(preco=0,taxaau=0,taxaredu=0):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: {moeda(preco)}')
    print('-' * 40)
    print(f'Metade: \t\t\t\t\t{metade(preco, True)}')
    print(f'Dobro: \t\t\t\t\t\t{dobrar(preco, True)}')
    print(f'{taxaau}% de aumento: \t\t\t{aumentar(preco, 10, True)}')
    print(f'{taxaredu}% de redução: \t\t\t{reduzir(preco, 13, True)}')