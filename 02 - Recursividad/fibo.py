
def fibonacci(n):
    if n <= 1:
        valor = n
        print(f"calculando el fibonacci de {n} el valor es {valor}")
        return valor
    else:
        valor = fibonacci(n-1) + fibonacci(n-2)
        print(f"calculando el fibonacci de {n} el valor es {valor}")
        return valor

print(fibonacci(10))


