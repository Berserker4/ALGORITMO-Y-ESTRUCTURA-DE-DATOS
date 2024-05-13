class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_peliculas}"

personajes = [
    {'nombre': 'Rocket Raccoon', 'pelis': 4},
    {'nombre': 'Iron Man', 'pelis': 6},
    {'nombre': 'Capitan America', 'pelis': 5},
    {'nombre': 'Groot', 'pelis': 4},
    {'nombre': 'Black Widow', 'pelis': 7},
    {'nombre': 'Loki', 'pelis': 4},
]
from package.ClassStack import Stack
pila = Stack()
for pers in personajes:
    pila.push(Personaje(pers['nombre'],pers['pelis']))

iniciales = ['C','D','G']
pos = pila.size()+1
while(not pila.is_empty()):
    pos -= 1
    dato = pila.pop()
    if(dato.nombre == "Rocket Raccoon" or dato.nombre == "Groot"):
        print(dato.nombre,"se encuentra en la posicion",pos)
    elif(dato.nombre == "Black Widow"):
        print("Black Widow participo en",dato.cantidad_peliculas,"peliculas")
    if(dato.cantidad_peliculas > 5):
        print(dato.nombre,"participo en",dato.cantidad_peliculas,"peliculas")
    if(dato.nombre[0] in iniciales):
        print(dato)
        