def calcular_desconto(valor, percentual):
    if percentual > 50:
        percentual = 50

    return valor - (valor * percentual / 100)
