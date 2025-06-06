# -------------------------------------------
# 02 - Funciones en Python 🐍
# -------------------------------------------

# ¿Qué es una función?
# Una función es un bloque de código que realiza una tarea específica.
# Puedes "llamarla" cuantas veces quieras, evitando repetir código.
#ejecucion
#nombre_funcion()
#nombre_funcion(parametros)

# -------------------------------------------
# Ejemplo 1: Función con input
def saludar():

    nombre = input("Cual es tu nombre?")
    print(f"¡Hola, {nombre}!")

saludar()

# -------------------------------------------
# Ejemplo 2: Función simple sin parámetros
def saludar():
    print("¡Hola, bienvenida Cony!")

saludar()

# -------------------------------------------
# Ejemplo 3: Función con un parámetro
def saludar_nombre(nombre):
    print(f"Hola, {nombre}! ¿Cómo estás hoy?")

saludar_nombre("Cony")
saludar_nombre("Sofía")

# -------------------------------------------
# Ejemplo 4: Función con múltiples parámetros
def sumar(a, b):
    resultado = a + b
    return resultado

print("Suma:", sumar(4, 6))
print("Suma:", sumar(-3, 10))

# -------------------------------------------
# Ejemplo 5: Función con valor por defecto
def saludar_con_emoji(nombre="amiga", emoji="😊"):
    print(f"Hola, {nombre} {emoji}")

saludar_con_emoji()
saludar_con_emoji("Cony", "🐍")

# -------------------------------------------
# Ejemplo 6: Documentación de funciones (docstrings)
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: π * r²
    """
    pi = 3.1416
    return pi * radio ** 2

print("Área:", area_circulo(5))

# -------------------------------------------
# Ejemplo 7: Función con condicional
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print("¿Es par?", es_par(4))  # True
print("¿Es par?", es_par(7))  # False

# -------------------------------------------
# Ejercicio propuesto
# Crea una función que calcule el IMC (Índice de Masa Corporal)
# fórmula: imc = peso / altura**2

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

print("IMC:", calcular_imc(65, 1.68))

# -------------------------------------------



