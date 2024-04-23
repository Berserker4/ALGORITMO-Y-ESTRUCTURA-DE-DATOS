from package.ClassStack import Stack
import os


def interseccion_pilas(pila1, pila2):
    interseccion = Stack()

    aux = set()
    while not pila1.size() == 0:
        aux.add(pila1.pop())

    while not pila2.size() == 0:
        personaje = pila2.pop()
        if personaje in aux:
            interseccion.push(personaje)

    return interseccion

episodio_V = Stack()
for i in range(5):
    Personajes_Episodio5 = input(print("Ingresa personajes",i+1,"del Episodio V: "))
    episodio_V.push(Personajes_Episodio5)
    os.system("cls") #Lo uso para una mayor comodidad visual

episodio_VII = Stack()
for i in range(5):
    Personajes_Episodio7 = input(print("Ingresa personajes",i+1,"del Episodio VII: " ))
    episodio_VII.push(Personajes_Episodio7)
    os.system("cls") 

interseccion = interseccion_pilas(episodio_V, episodio_VII)

print("Personajes que aparecen en ambos episodios:")
while not interseccion.size() == 0:
    print(interseccion.pop())

