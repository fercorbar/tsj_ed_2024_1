
mi_arreglo_1d = ['A', 'B', 'C', 'D', 'E']

# Hacer un cliclo for para imprimir los elementos de mi_arreglo_1d
# for elemento in mi_arreglo_1d:
#     print(elemento)

print(mi_arreglo_1d[3])

exit(0)

mi_arreglo_2d = [
    ['A', 'B', 'C'], 
    ['D', 'E', 'F'], 
    ['G', 'H', 'I']
]

# Hacer un ciclo for para imprimir los elementos de mi_arreglo_2d

# for elemento in mi_arreglo_2d:
#     for sub_elemento in elemento:
#         print(sub_elemento)
    # print(elemento)


mi_arreglo_3d = [
    [
        ['A', 'B', 'C'], 
        ['D', 'E', 'F'], 
        ['G', 'H', 'I']
    ],
    [
        ['J', 'K', 'L'], 
        ['M', 'N', 'O'], 
        ['P', 'Q', 'R']
    ],
    [
        ['S', 'T', 'U'], 
        ['V', 'W', 'X'], 
        ['Y', 'Z', '0']
    ]
]

for elemento in mi_arreglo_3d:
    for sub_elemento in elemento:
        for sub_sub_elemento in sub_elemento:
            print(sub_sub_elemento)











lista = [32, 85, 18, 22, 2, 30, 4, 5]