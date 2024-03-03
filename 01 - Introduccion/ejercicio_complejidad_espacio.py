import random

def desordenar(entrada):
    indices = []
    resultado = []
    indice = 0
    for elemento in entrada:
        indices.append(indice)
        indice += 1
        resultado.append(0)
    print(entrada)
    print(indices)
    print(resultado)

    for elemento in entrada:
        yyy = random.randint(0, len(indices)-1)
        indice_a_reemplazar = indices[yyy]
        resultado[indice_a_reemplazar] = elemento
        indices.pop(yyy)

    print('=========')
    print(entrada)
    print(indices)
    print(resultado)


lista_de_entrada = [11,22,33,44,55, 66, 77, 88, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
desordenar(lista_de_entrada)
