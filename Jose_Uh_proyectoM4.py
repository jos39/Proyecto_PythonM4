# Importar las bibliotecas necesarias
import requests                     # Libreria para realizar solicitudes http
import matplotlib.pyplot as plt     # Libreria para visualización de imágenes
import json                         # Libreria para trabajar con datos JSON
from PIL import Image               # Libreria para manipulación de imágenes
from urllib.request import urlopen  # abrir URL
import os                           # Sirve para manejar archivos

# Pide al usuario que introduzca el nombre de un Pokemon
pokemon = input('Introduce el nombre de un pokemon: ')

# URL de la API del pokemon
url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

try:
# Obtener respuesta del servidor 
    respuesta = requests.get(url, timeout=10)
except requests.Timeout:
    print('El tiempo de espera ha expirado')

# Verifica si se obtuvo una respuesta exitosa
if respuesta.status_code != 200:
    print('El pokemon no fue encontrado')
    exit()

# Guarda los datos del servidor en un json
datos = respuesta.json()

try:
# Obtiene la imagen del servidor y abri la imagen
    url_imagen = datos['sprites']['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print('El pokemon no tiene imagen')
    exit()

# Busca el nombre del pokemon
nombre = datos['species']['name']
print('Nombre del pokemon: ' + str(nombre))

# Busca el peso del pokemon
peso = datos['weight']
print('Peso: ' + str(peso))

# Busca el tamaño del pokemon
tamaño = datos['height']
print('Tamaño: ' + str(tamaño))

# Busca los moviementos del pokemon
movimientos = datos['moves']
lista_movimientos = [movimiento['move']['name'] for movimiento in movimientos] # Crea una lista con los movimientos
print('Los movimientos: ' + ', '.join(lista_movimientos))

# Busca las habilidades del pokemon
habilidades = datos['abilities']
lista_habilidades = [habilidad['ability']['name'] for habilidad in habilidades] # Crea una lista con los hablidades
print('Sus habilidades son: ' + ', '.join(lista_habilidades))

# Busca el tipo de pokemon
tipos = datos['types']
lista_tipos = [tipo['type']['name'] for tipo in tipos]  #                       # Crea una lista con los tipos
print('Tipo: ' + ', '.join(lista_tipos))

# Se crea un diccionario con los datos del pokemon
pokemon_data = {
    "nombre": nombre,
    "peso": peso,
    "tamaño": tamaño,
    "movimientos": lista_movimientos,
    "habilidades": lista_habilidades,
    "tipos": lista_tipos,
    "url_imagen": url_imagen
}

# Guarda el archivo en json
carpeta = "pokedex"                     # Nombre de la carpta donde se guardara
if not os.path.exists(carpeta):         # verifica si existe la carpeta
    os.makedirs(carpeta)                # Crea una carpta si no existe

with open(os.path.join(carpeta, f"{nombre}.json"), "w") as f: # Guarda los datos en el json
    json.dump(pokemon_data, f, indent=4)

# Muestra imagen del pokemon
plt.title(nombre)
imgplot = plt.imshow(imagen)
plt.show()