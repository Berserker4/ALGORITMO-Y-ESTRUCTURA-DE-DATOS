from package.ClassStack import Stack
import os

Episodio_V = Stack()
Episodio_VII = Stack()

for i in range(5):
    personajes_episodio5 = input("Ingresa personajes del Episodio V: ")
    Episodio_V.push(personajes_episodio5)
    # os.system("cls")

for i in range(5):
    personajes_episodio7 = input("Ingresa personajes del Episodio VII: ")
    Episodio_VII.push(personajes_episodio7)
    # os.system("cls")

def interseccion_pilas(pila1, pila2):
    pila1 = Stack()
    pila2 = Stack()
    aux = []
    encontrados = Stack()

    while not pila1.size() == 0:
        personaje = pila1.pop()
        encontrados.push(personaje)
        pila2_temp = pila2
        while not pila2_temp.size() == 0:
            if personaje == pila2_temp.pop():
                aux.append(personaje)
                break

    while not encontrados.size() == 0:
        pila1.push(encontrados.pop())
    
    return aux

interseccion_personajes = interseccion_pilas(Episodio_V, Episodio_VII)
print("Personajes que aparecen en ambos episodios:")
print(interseccion_personajes)
for personaje in interseccion_personajes:
    print(personaje)