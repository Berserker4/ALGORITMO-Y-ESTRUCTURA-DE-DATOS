#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:


#determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from package.ClassStack import Stack
from package.ClassQueue import Queue

Datos = Stack()

Datos.push("Iron Man")
Datos.push("Captain America")
Datos.push("Rocket Raccoon")
Datos.push("Groot")
Datos.push("Thor")
Datos.push("Hulk")
Datos.push("Black Widow")
Datos.push("Doctor Strange")

def positions_rocket_y_groot(Datos):
    positions = []
    position = Datos.size()  
    while not Datos.is_empty():
        personaje = Datos.pop()
        if personaje == "Rocket Raccoon" or personaje == "Groot":
            positions.append(position)
        position -= 1
        
    return positions   

print("Posición de Rocket Raccoon y Groot:", positions_rocket_y_groot(Datos))

Letras = ["C", "D", "G"]
aux = Stack()
while not Datos.is_empty():
    elemento = Datos.pop()
    if elemento[0][0] in Letras:
        aux.push(elemento)  
    Datos.push(elemento)  

print("Personajes que empiezan con C, D y G:")
while not aux.is_empty():
    print(aux.pop())