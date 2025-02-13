import random
import time

class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.user_id = user_id
        self.nombre = nombre
        self.edad = edad


nombres = ["Ana", "Carlos", "Beatriz", "Daniel", "Elena", "Fernando", "Gabriela", "Hugo", "Isabel", "Javier"]
usuarios = []
for i in range(100000):
    nombre = random.choice(nombres)
    edad = random.randint(18, 80)
    usuarios.append(Usuario(i, nombre, edad))

def busqueda_lineal(usuarios, user_id):
    for usuario in usuarios:
        if usuario.user_id == user_id:
            return usuario
    return None

def busqueda_binaria(usuarios, user_id):
    izquierda = 0
    derecha = len(usuarios) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].user_id == user_id:
            return usuarios[medio]
        elif usuarios[medio].user_id < user_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

usuarios.sort(key=lambda x: x.user_id)

id_buscar = random.randint(0, 99999)
print(f"Buscando usuario con ID: {id_buscar}")

inicio = time.time()
resultado_lineal = busqueda_lineal(usuarios, id_buscar)
fin = time.time()
print(f"Tiempo de búsqueda lineal: {fin - inicio:.6f} segundos")
if resultado_lineal:
    print(f"Usuario encontrado (Lineal): {resultado_lineal.nombre}, {resultado_lineal.edad} años")

inicio = time.time()
resultado_binaria = busqueda_binaria(usuarios, id_buscar)
fin = time.time()
print(f"Tiempo de búsqueda binaria: {fin - inicio:.6f} segundos")
if resultado_binaria:
    print(f"Usuario encontrado (Binaria): {resultado_binaria.nombre}, {resultado_binaria.edad} años")
