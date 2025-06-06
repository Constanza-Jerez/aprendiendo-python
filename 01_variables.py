# -------------------------------------------
# 01 - Variables en Python 🐍
# -------------------------------------------

# Una variable es un espacio en memoria donde almacenamos un valor.
# En Python no necesitas declarar el tipo de variable explícitamente.

# Ejemplo 1: Variables de diferentes tipos
nombre = "Cony"           # string
edad = 30                 # int
altura = 1.68             # float
es_estudiante = True      # bool

# Imprimir variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)

# Ejemplo 2: Concatenación
mensaje = "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print(mensaje)

# Ejemplo 3: F-strings (recomendado)
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura}m.")

# Ejemplo 4: Reasignación de variables
edad = edad + 1
print(f"En un año tendré {edad} años.")

# Ejemplo 5: Tipado dinámico
variable = 10        # int
print(variable)
variable = "texto"   # ahora es string
print(variable)

# Ejemplo 6: Múltiples asignaciones
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

# Ejemplo 7: Constantes (por convención)
PI = 3.1416  # Las constantes se escriben en mayúsculas, aunque no son realmente constantes
print("Valor de PI:", PI)

# -------------------------------------------

