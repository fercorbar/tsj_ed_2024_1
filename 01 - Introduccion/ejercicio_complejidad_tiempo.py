


def sumarx(entrada, incremento):
    resultado = []
    for elemento in entrada:
        nuevo_valor = elemento + incremento
        resultado.append(nuevo_valor)
    print(entrada)
    print(resultado)

lista_entrada = [10,11,12,13,14,15]
sumarx(lista_entrada, 10)
