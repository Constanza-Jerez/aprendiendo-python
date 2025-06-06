# -------------------------------------------
# 04 - Bucles en Python 🐍
# -------------------------------------------

# ¿Qué es un bucle?
# Un bucle es una estructura que permite repetir un bloque de código
# tantas veces como sea necesario, evitando duplicar líneas.
# Existen principalmente dos tipos en Python:
#   - for: recorre una secuencia (lista, rango, cadena, etc.).
#   - while: repite mientras se cumpla una condición.

# -------------------------------------------
# Ejemplo 1: Bucle for simple
for i in range(1, 6):
    print(f"Repetición número {i}")
    
# -------------------------------------------
# Ejemplo 2: Bucle for sobre lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la fruta: {fruta}")

# -------------------------------------------
# Ejemplo 3: Bucle while simple
contador = 1
while contador <= 5:
    print(f"Cuenta regresiva: {6 - contador}")
    contador += 1

# -------------------------------------------
# Ejemplo 4: Uso de break en while
numero = 0
while True:
    numero = int(input("Ingresa un número (negativo para salir): "))
    if numero < 0:
        print("Se detectó número negativo. Saliendo del bucle.")
        break
    print(f"El número ingresado es {numero}")

# -------------------------------------------
# Ejemplo 5: Uso de continue en for
for letra in "Python":
    if letra == "o":
        continue
    print(f"Letra actual: {letra}")

# -------------------------------------------
# Ejemplo 6: Bucle anidado
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"Fila {fila}, Columna {columna}")

# -------------------------------------------
# Ejemplo 7: Iterar con enumerate
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores, start=1):
    print(f"{indice}. {color}")

# -------------------------------------------
# Ejercicio propuesto
# Ejercicio propuesto
# Escribe un programa que imprima la tabla de multiplicar
# del 1 al 5 (cada una del 1 al 10).

for num in range(1, 6):
    print(f"\n--- Tabla de multiplicar del {num} ---")
    for mult in range(1, 11):
        print(f"{num} x {mult} = {num * mult}")
# -------------------------------------------
