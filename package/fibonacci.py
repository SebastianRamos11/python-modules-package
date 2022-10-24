def secuencia(cantidad):
    n1, n2 = 0, 1
    count = 0

    if cantidad <= 0:
       print("Porfavor ingresa un número entero")

    elif cantidad == 1:
       print("Secuencia Fibonacci hasta:",cantidad,":")
       print(n1)

    # Generar secuencia
    else:
       print("Secuencia Fibonacci:")
       while count < cantidad:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
