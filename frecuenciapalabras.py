from collections import Counter
import re

def contar_palabras(texto):
    palabras = re.findall(r'\b\w+\b',texto.lower())
    frecuencia = Counter(palabras)
    return frecuencia

texto = input("ingrese un texto:")
resultado = contar_palabras(texto)
print("Frecuencia de palabras:",resultado)