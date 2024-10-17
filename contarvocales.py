frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in frase:
    if letra in vocales:
        contador_vocales += 1
print(f"La frase contiene {contador_vocales} vocales.")
