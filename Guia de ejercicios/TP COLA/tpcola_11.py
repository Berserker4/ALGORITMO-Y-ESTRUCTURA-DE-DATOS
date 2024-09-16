from ClassQueue import Queue

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f"{self.nombre} ({self.planeta})"


def mostrar_personajes_de_planetas(cola, planetas):
    print(f"Personajes de los planetas {planetas}:")
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje.planeta in planetas:
            print(personaje)
        cola.arrive(personaje)

def mostrar_planeta_natal(cola, nombres):
    for i in range(cola.size()):
        personaje = cola.attention()
        if personaje.nombre in nombres:
            print(f"{personaje.nombre} es de {personaje.planeta}")
        cola.arrive(personaje)

def insertar_antes_de(cola, nuevo_personaje, nombre_objetivo):
    cola_temporal = Queue()
    insertado = False

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.nombre == nombre_objetivo and not insertado:
            cola_temporal.arrive(nuevo_personaje)
            insertado = True
        cola_temporal.arrive(personaje)

    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.attention())

def eliminar_despues_de(cola, nombre_objetivo):
    cola_temporal = Queue()
    saltar_siguiente = False

    while cola.size() > 0:
        personaje = cola.attention()
        if saltar_siguiente:
            saltar_siguiente = False
            continue
        cola_temporal.arrive(personaje)
        if personaje.nombre == nombre_objetivo:
            saltar_siguiente = True

    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.attention())


cola = Queue()
cola.arrive(Personaje("Luke Skywalker", "Tatooine"))
cola.arrive(Personaje("Han Solo", "Corellia"))
cola.arrive(Personaje("Leia Organa", "Alderaan"))
cola.arrive(Personaje("Yoda", "Dagobah"))
cola.arrive(Personaje("Chewbacca", "Kashyyyk"))
cola.arrive(Personaje("Darth Vader", "Tatooine"))
cola.arrive(Personaje("Jar Jar Binks", "Naboo"))

input("Precione para continuar")
planetas = ["Alderaan", "Endor", "Tatooine"]
mostrar_personajes_de_planetas(cola, planetas)


input("Precione para continuar")
nombres = ["Luke Skywalker", "Han Solo"]
mostrar_planeta_natal(cola, nombres)

input("Precione para continuar")
nuevo_personaje = Personaje("Obi-Wan Kenobi", "Stewjon")
insertar_antes_de(cola, nuevo_personaje, "Yoda")

input("Precione para continuar")
for i in range(cola.size()):
    personaje = cola.attention()
    print(personaje)
    cola.arrive(personaje)

input("Precione para continuar")
eliminar_despues_de(cola, "Jar Jar Binks")

input("Precione para continuar")
for i in range(cola.size()):
    personaje = cola.attention()
    print(personaje)
    cola.arrive(personaje)
