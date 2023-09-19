def lerDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: {entrada} não é um valor válido!!')
        else:
            valido = True
            return float(entrada)