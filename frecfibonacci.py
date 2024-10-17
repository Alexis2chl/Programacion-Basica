def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia)< n:
        secuencia.append(secuencia[-1] + secuencia [-2])
    return secuencia
numero =int(input("Ingreso la cantidad en termino de Fibonacci:"))
resultado = fibonacci(numero)
print("secuencia de fibonacci:", resultado)
   