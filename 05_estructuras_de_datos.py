# -------------------------------------------
# 05 - Estructuras de Datos en Python 🗂️
# -------------------------------------------

# ¿Qué es una estructura de datos?
# Una estructura de datos es una forma de organizar y almacenar colecciones de datos
# para poder accederlos y manipularlos de manera eficiente. En Python, las más comunes son:
#   - Listas
#   - Tuplas
#   - Diccionarios

# -------------------------------------------
# Ejemplo 1: Listas
# Una lista es una secuencia ordenada y modificable de elementos.
# Se escribe usando corchetes [ ] y los elementos se separan por comas.

# Crear una lista de números
numeros = [10, 20, 30, 40, 50]
print("Lista inicial:", numeros)

# Acceder por índice (empezando en 0)
print("Primer elemento:", numeros[0])    # 10
print("Tercer elemento:", numeros[2])    # 30

# Modificar un elemento
numeros[1] = 25
print("Después de modificar índice 1:", numeros)

# Agregar elementos al final
numeros.append(60)
print("Después de append(60):", numeros)

# Insertar en una posición específica
numeros.insert(2, 27)   # inserta 27 en el índice 2, moviendo el resto a la derecha
print("Después de insert(2, 27):", numeros)

# Eliminar elementos
elemento = numeros.pop(3)  # elimina el elemento en índice 3 y lo retorna
print("Elemento eliminado (pop índice 3):", elemento)
print("Lista tras pop:", numeros)

# Recorrer con un bucle for
print("\nRecorriendo la lista con for:")
for num in numeros:
    print(num)

# Métodos útiles: sort(), reverse(), count(), len()
numeros.sort()    # ordena de menor a mayor
print("\nLista ordenada:", numeros)

numeros.reverse() # invierte el orden
print("Lista invertida:", numeros)

print("Cantidad de veces que aparece 25:", numeros.count(25))
print("Longitud de la lista:", len(numeros))

# -------------------------------------------
# Ejemplo 2: Tuplas
# Una tupla es similar a una lista, pero es inmutable (no se puede cambiar, agregar ni eliminar elementos).
# Se escribe usando paréntesis ( ) o sin paréntesis, separando por comas.

# Crear tuplas
mi_tupla = (1, 2, 3, 4, 5)
otra_tupla = "a", "b", "c"   # también válido

print("\nTupla:", mi_tupla)
print("Otras tupla:", otra_tupla)

# Acceder por índice
print("Elemento índice 2 de mi_tupla:", mi_tupla[2])  # 3

# Intentar modificar produce un error (descomenta para probar)
# mi_tupla[1] = 10   # TypeError: 'tuple' object does not support item assignment

# Desempaquetado de tupla (unpacking)
a, b, c, d, e = mi_tupla
print("Desempaquetado:", a, b, c, d, e)

# Métodos: count(), index()
print("¿Cuántas veces aparece el 3?", mi_tupla.count(3))
print("Índice del elemento 4:", mi_tupla.index(4))

# -------------------------------------------
# Ejemplo 3: Diccionarios
# Un diccionario es una colección de pares clave-valor. Es desordenado (hasta Python 3.6),
# modificable y permite buscar valores por su clave. Se escribe con llaves { }.

# Crear un diccionario de ejemplo: país -> capital
capitales = {
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "Argentina": "Buenos Aires"
}
print("\nDiccionario inicial:", capitales)

# Acceder a un valor usando su clave
print("Capital de Perú:", capitales["Perú"])

# Agregar un nuevo par clave-valor
capitales["México"] = "Ciudad de México"
print("Después de agregar México:", capitales)

# Modificar el valor de una clave existente
capitales["Chile"] = "Valparaíso"  # reassign valor de "Chile"
print("Después de modificar Chile:", capitales)

# Eliminar un par clave-valor
valor_eliminado = capitales.pop("Colombia")  # retorna el valor eliminado
print("Valor eliminado (Colombia):", valor_eliminado)
print("Diccionario tras pop:", capitales)

# Recorrer un diccionario:
# 1) Sólo claves
print("\nClaves en el diccionario:")
for pais in capitales:
    print(pais)

# 2) Clave y valor con items()
print("\nPares clave-valor:")
for pais, capital in capitales.items():
    print(f"{pais} ➔ {capital}")

# 3) Sólo valores
print("\nValores en el diccionario:")
for capital in capitales.values():
    print(capital)

# Métodos útiles: keys(), values(), items(), get(), clear()
print("\nLista de claves:", list(capitales.keys()))
print("Lista de valores:", list(capitales.values()))

print("get('Chile'):", capitales.get("Chile"))
print("get('Brasil', 'No encontrado'):", capitales.get("Brasil", "No encontrado"))

# -------------------------------------------
# Ejemplo 4: Listas de tuplas y diccionarios anidados
# Se pueden combinar estructuras para mayor complejidad.

# Lista de tuplas (cada tupla representa un par (nombre, edad))
personas = [("Ana", 28), ("Carlos", 35), ("María", 22)]
print("\nLista de tuplas de personas:", personas)

# Recorrerla imprimiendo datos
for nombre, edad in personas:
    print(f"{nombre} tiene {edad} años")

# Lista de diccionarios (cada dict representa un registro de persona)
registros = [
    {"nombre": "Diego", "edad": 30, "ciudad": "Santiago"},
    {"nombre": "Lucía", "edad": 27, "ciudad": "Lima"},
    {"nombre": "Pedro", "edad": 33, "ciudad": "Buenos Aires"}
]
print("\nLista de diccionarios de registros:")
for persona in registros:
    print(persona)

# Acceder a un campo específico de cada dict
print("\nNombres extraídos de registros:")
for persona in registros:
    print(persona["nombre"])

# Diccionario con listas como valores
grupos = {
    "EquipoA": ["Alice", "Bob", "Carlos"],
    "EquipoB": ["Daniela", "Esteban"]
}
print("\nDiccionario con listas como valores:", grupos)

# Recorrer el diccionario y las listas internas
for equipo, miembros in grupos.items():
    print(f"\n{equipo} tiene {len(miembros)} miembros:")
    for miembro in miembros:
        print("-", miembro)

# -------------------------------------------
# Ejercicio propuesto
# - Crea una lista de diversas frutas (mismo nombre repetido algunas veces).
# - Utiliza un diccionario para contar cuántas veces aparece cada fruta.
# - Finalmente, imprime cada fruta con su respectivo conteo.

# Sugerencia de solución:
# frutas_lista = ["manzana", "banana", "pera", "manzana", "kiwi", "banana", "pera", "manzana"]

# conteo = {}
# for fruta in frutas_lista:
#     if fruta in conteo:
#         conteo[fruta] += 1
#     else:
#         conteo[fruta] = 1

# print("\nConteo de frutas:")
# for fruta, cantidad in conteo.items():
#     print(f"{fruta}: {cantidad}")

