# -------------------------------------------
# 03 - Condicionales 🐍
# -------------------------------------------

# ¿Qué es una condicional?
# Es una estructura que permite ejecutar cierto código solo si se cumple una condición.

# Sintaxis:
# if condición:
#     hacer algo
# elif otra_condición:
#     hacer otra cosa
# else:
#     hacer algo por defecto

# -------------------------------------------
# Ejemplo 1: Condicional simple
edad = 18

if edad >= 18:
    print("Eres mayor de edad")

# -------------------------------------------
# Ejemplo 2: Condicional con else
temperatura = 10

if temperatura > 20:
    print("Hace calor")
else:
    print("Hace frío")

# -------------------------------------------
# Ejemplo 3: if...elif...else
nota = 6.5

if nota >= 6.0:
    print("¡Aprobaste!")
elif nota >= 4.0:
    print("Tienes que recuperar")
else:
    print("Reprobaste")

# -------------------------------------------
# Ejemplo 4: Comparación de valores
a = 10
b = 20

if a == b:
    print("a y b son iguales")
else:
    print("a y b son diferentes")

# -------------------------------------------
# Ejemplo 5: Validación de número par/impar
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")

# -------------------------------------------
# Ejemplo 6: Combinación de condiciones con operadores lógicos
usuario = "admin"
clave = "1234"

if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
else:
    print("Usuario o clave incorrectos")

# -------------------------------------------
# Ejemplo 7: Verificar si una variable existe o está vacía
nombre = ""

if nombre:
    print(f"Hola, {nombre}")
else:
    print("No ingresaste tu nombre")

# -------------------------------------------
# 1 Ejercicio propuesto
# Escribe un programa que reciba un número y diga si es positivo, negativo o cero.

numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# -------------------------------------------

# 2 Ejercicio propuesto
#Ejercicio: Clasificación de edades

# Crea un programa que pida la edad de una persona y diga en qué etapa de la vida está:

#     Menor de 0: ❌ Edad no válida

#     De 0 a 12 años: 👶 Infancia

#     De 13 a 17 años: 🧒 Adolescencia

#     De 18 a 59 años: 🧑 Adultez

#     60 o más: 👵 Vejez

Edad = float(input("ingrese su edad: "))    

if edad < 0:
    print("Edad no válida")
elif edad <=12:
    print("Estas en la Infancia")
elif edad <=17:
    print("Estas en la adolescencia")
elif edad <=59:
    print("Ya eres un adulto")
else:
    print("Estas en la vejez")