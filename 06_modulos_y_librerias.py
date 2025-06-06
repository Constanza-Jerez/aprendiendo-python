# -------------------------------------------
# 06 - Módulos y Librerías en Python 📦
# -------------------------------------------

# ¿Qué es un módulo?
# Un módulo es un archivo .py que contiene definiciones de funciones, clases o variables 
# que puedes reutilizar. Python incluye varios módulos estándar (stdlib) que facilitan tareas 
# comunes sin tener que escribir código desde cero. Además, existen librerías de terceros 
# (instalables vía pip) para funcionalidades más especializadas.

# -------------------------------------------
# Ejemplo 1: Módulo math
# Para operaciones matemáticas avanzadas (raíz cuadrada, trigonometría, etc.).
import math

print("Ejemplo - módulo math:")
# Pi y e
print("Pi:", math.pi)
print("Euler (e):", math.e)

# Raíz cuadrada
num = 25
print(f"Raíz cuadrada de {num}:", math.sqrt(num))

# Potencia
print("2⁸ =", math.pow(2, 8))

# Función trigonométrica
ángulo_grados = 30
ángulo_radianes = math.radians(ángulo_grados)
print(f"Coseno de {ángulo_grados}°:", math.cos(ángulo_radianes))

print("-" * 40)

# -------------------------------------------
# Ejemplo 2: Módulo random
# Para generar números aleatorios o elegir elementos al azar.
import random

print("Ejemplo - módulo random:")
# Entero aleatorio entre 1 y 10
aleatorio = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", aleatorio)

# Elegir un elemento al azar de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
print("Color aleatorio:", random.choice(colores))

# Barajar una lista
cartas = ["A", "2", "3", "4", "5", "J", "Q", "K"]
random.shuffle(cartas)
print("Cartas barajadas:", cartas)

# Generar una muestra sin reemplazo
muestra = random.sample(range(1, 50), 6)  # similar a sorteo de lotería
print("Números de muestra (lotto):", muestra)

print("-" * 40)

# -------------------------------------------
# Ejemplo 3: Módulo datetime
# Para manejar fechas y horas.
from datetime import datetime, timedelta

print("Ejemplo - módulo datetime:")
ahora = datetime.now()
print("Fecha y hora actuales:", ahora)

# Crear una fecha específica
fecha_evento = datetime(2025, 6, 15, 14, 30)  # 15 de junio de 2025 a las 14:30
print("Fecha de evento:", fecha_evento)

# Formatear fecha a cadena
print("Formato dd/mm/yyyy:", ahora.strftime("%d/%m/%Y"))
print("Formato dd-mm-yyyy HH:MM:", ahora.strftime("%d-%m-%Y %H:%M"))

# Operaciones con fechas (timedelta)
mañana = ahora + timedelta(days=1)
ayer = ahora - timedelta(days=1)
print("Mañana será:", mañana.strftime("%d/%m/%Y"))
print("Ayer fue:", ayer.strftime("%d/%m/%Y"))

print("-" * 40)

# -------------------------------------------
# Ejemplo 4: Módulo os
# Para interactuar con el sistema de archivos y entorno.
import os

print("Ejemplo - módulo os:")
# Obtener directorio actual
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)

# Listar archivos y carpetas en un directorio
contenido = os.listdir(directorio_actual)
print("Contenido de este directorio:")
for elemento in contenido:
    print("  -", elemento)

# Crear un directorio (si no existe)
nueva_carpeta = "carpeta_ejemplo"
if not os.path.exists(nueva_carpeta):
    os.mkdir(nueva_carpeta)
    print(f"Se creó la carpeta '{nueva_carpeta}'")
else:
    print(f"La carpeta '{nueva_carpeta}' ya existe")

# Eliminar la carpeta creada (comentar si deseas conservarla)
# os.rmdir(nueva_carpeta)
# print(f"Se eliminó la carpeta '{nueva_carpeta}'")

print("-" * 40)

# -------------------------------------------
# Ejemplo 5: Módulo sys
# Para acceder a parámetros de línea de comandos y entorno de ejecución.
import sys

print("Ejemplo - módulo sys:")
# Argumentos pasados al script (sys.argv[0] es el nombre del archivo .py)
print("Argumentos de la línea de comandos:", sys.argv)

# Versión de Python
print("Versión de Python:", sys.version)

# Ruta donde busca módulos instalados
print("Rutas de búsqueda de módulos:")
for ruta in sys.path:
    print("  -", ruta)

print("-" * 40)

# -------------------------------------------
# Ejemplo 6: Módulo json
# Para serializar y deserializar datos en formato JSON.
import json

print("Ejemplo - módulo json:")
# Diccionario de Python
data = {
    "nombre": "Cony",
    "edad": 35,
    "lenguajes": ["Python", "SQL", "Power BI"]
}

# Convertir dict a string JSON
json_str = json.dumps(data, indent=4, ensure_ascii=False)
print("JSON generado:")
print(json_str)

# Convertir string JSON a dict de Python
python_obj = json.loads(json_str)
print("Python objeto desde JSON:", python_obj)
print("Accediendo a 'nombre':", python_obj["nombre"])

print("-" * 40)

# -------------------------------------------
# Ejemplo 7: Librería de terceros requests (HTTP)
# Para hacer peticiones HTTP (GET, POST, etc.).
# Nota: debes instalar requests antes: pip install requests
try:
    import requests
    print("Ejemplo - librería requests:")
    respuesta = requests.get("https://api.github.com")
    print("Código de estado:", respuesta.status_code)
    # Mostrar las primeras 200 caracteres de la respuesta JSON
    print("Contenido (JSON):", respuesta.text[:200], "...")
except ImportError:
    print("La librería 'requests' no está instalada. Instálala con: pip install requests")

print("-" * 40)
