# IMPORTACION DEL MÓDULO ARITMETICA
from package import aritmetica

# IMPORTACION DEL MÓDULO PROMEDIO
from package import promedio

# IMPORTACION DEL MÓDULO RAIZ CUADRADA
from package import raiz

# IMPORTACION DEL MÓDULO FIBONACCI
from package import fibonacci

# IMPORTACION DEL MÓDULO AREAS
from package import areas


def pedir_cantidad():
    cantidad = int(input("¿Cuantos números deseas operar?: "))
    return cantidad
    
active_module = 0
while active_module <= 0 or active_module > 5:
    print("""
Bienvenido al menú, elija el modulo que quiere consultar:
    1. Operaciones aritmeticas
    2. Calcular promedio
    3. Calcular la raiz cuadrada de un número
    4. Serie Fibonacci
    5. Hallar el área de una figura geometrica
    """)
    active_module = int(input("Ingresa una opción: "))
    while (active_module < 1 or active_module > 5):
        active_module = int(input("Opción invalida, vuelve a intentarlo: "))


# Implementación módulo aritmetica
if(active_module == 1):
    # Pedir datos
    print("""
----------- BIENVENIDO AL MODULO DE OPERACIONES ARITMETICAS -----------

¿Que operación deseas realizar?
1. Suma
2. Resta
3. Multiplicación
4. División
    """)
    op = int(input("Ingresa una opción: "))
    while (op < 1 or op > 4):
        op = int(input("Opción invalida, vuelve a intentarlo: "))
    
    cantidad = pedir_cantidad()
    lst = []
    for i in range(cantidad):
        lst.append(int(input("Ingresa el número " + str(i + 1) + ": ")))
    
    # Operar datos
    if(op == 1):
        print("Resultado de la suma: ", aritmetica.suma(lst))

    if(op == 2):
        print("Resultado de la resta: ", aritmetica.resta(lst))

    if(op == 3):
        print("Resultado de la multiplicación: ", aritmetica.multiplicacion(lst))

    if(op == 4):
        print("Resultado de la división: ", aritmetica.division(lst)) 

# Implementación módulo promedio
if(active_module == 2):
    print("----------- BIENVENIDO AL MODULO DE CALCULAR PROMEDIO -----------")
    print("Calcula facilmente el promedio de tu materia y te diremos si vas aprobando o reprobando.\n\n")
    cantidad = pedir_cantidad()
    notas = []
    for i in range(cantidad):
        nota = float(input("Ingresa la nota " + str(i + 1) + ": "))

        while nota > 5 or nota < 0:
            print("Error, la nota debe estar en un rango de 0 a 5")
            print("Ingrese la nota", i+1, end="")
            nota = float(input(": "))

        notas.append(nota) 
    prom = promedio.calcular(notas)
    if prom > 3.5:
        print("\nAPROBADO CON:", round(prom, 1))
    else:
        print("\nREPROBADO CON:", round(prom, 1))

# Implementación módulo raiz cuadrada
if(active_module == 3):
    print("----------- BIENVENIDO AL MODULO DE RAIZ CUADRADA -----------\n\n")
    num = float(input("Ingrese el número al que desea calcularle la raíz cuadrada: "))
    print("La raíz cuadrada de", num, "es", raiz.calcular(num))

# Implementación módulo raiz cuadrada
if(active_module == 4):
    print("----------- BIENVENIDO AL MODULO DE SERIE FIBONACCI -----------\n\n")
    cantidad = int(input("Ingrese la longitud de la secuencia que desea ver: "))
    fibonacci.secuencia(cantidad)

# Implementación módulo áreas
if(active_module == 5):
    # Pedir datos
    print("""
----------- BIENVENIDO AL MODULO DE ÁREAS GEOMÉTRICAS -----------

¿Que figura geometrica quieres hallarle su área?
1. Cuadrado
2. Rectángulo
3. Triángulo
4. Circulo
    """)
    op = int(input("Ingresa una opción: "))
    while (op < 1 or op > 4):
        op = int(input("Opción invalida, vuelve a intentarlo: "))
        
    if(op == 1):
        area_cuadrado = areas.cuadrado(float(input("Ingresa la longitud del lado del cuadrado: ")))
        print("El área del cuadrado es de:", area_cuadrado)

    if(op == 2):
        b = float(input("Ingresa la base del rectángulo: "))
        h = float(input("Ingresa la altura del rectángulo: "))
        area_rectangulo = areas.rectangulo(b, h)
        print("El área del rectángulo es de:", area_rectangulo)

    if(op == 3):
        b = float(input("Ingresa la base del triángulo: "))
        h = float(input("Ingresa la altura del triángulo: "))
        area_triangulo = areas.triangulo(b, h)
        print("El área del triángulo es de:", area_triangulo)

    if(op == 4):
        area_circulo = areas.circulo(float(input("Ingresa el radio del círculo: ")))
        print("El área del círculo es de:", area_circulo)