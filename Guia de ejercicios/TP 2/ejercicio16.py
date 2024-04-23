from package.ClassStack import Stack
import os

Episodio_V = Stack()
Episodio_VII = Stack()
for i in range(5):
    Personajes_Episodio5 = input(print("Ingresa personajes",i+1,"del Episodio V: "))
    Episodio_V.push(Personajes_Episodio5)
    os.system("cls") #Lo uso para una mayor comodidad visual
for i in range(5):
    Personajes_Episodio7 = input(print("Ingresa personajes",i+1,"del Episodio VII: " ))
    Episodio_VII.push(Personajes_Episodio7)
    os.system("cls") 

def interseccion_pilas(pila1, pila2):
    elementos_comunes = []
    temp_stack = Stack()

    # Vaciar pila1 en temp_stack y comparar cada elemento con pila2
    while not pila1.is_empty():
        personaje = pila1.pop()
        temp_stack.push(personaje)
        if personaje in pila2:
            elementos_comunes.append(personaje)

    # Restaurar pila1 desde temp_stack
    while not temp_stack.is_empty():
        pila1.push(temp_stack.pop())

    return elementos_comunes

interseccion_personajes = interseccion_pilas(Episodio_V, Episodio_VII)
print("Personajes que aparecen en ambos episodios:")
for personaje in interseccion_personajes:
    print(personaje)