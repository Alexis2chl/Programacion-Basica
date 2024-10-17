def ordenar_diccionario(lista_diccionarios, clave):
    return sorted(lista_diccionarios, key=lambda x: x[clave])

personas = [
    {'nombre': 'Ana', 'edad': 30},
    {'nombre': 'Luis', 'edad': 25},
    {'nombre': 'Carlos', 'edad': 35}
]

clave='edad'
personas_ordenadas=ordenar_diccionario(personas, clave)
print("lista ordenada por edad:", personas_ordenadas)