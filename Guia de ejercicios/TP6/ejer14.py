from random import randint
from grafo import Graph

# Inicializamos el grafo no dirigido
grafo = Graph(dirigido=False)

# a. Agregamos los vértices que representan los ambientes de la casa
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    grafo.insert_vertice(ambiente)

# b. Agregar tres aristas a cada vértice, con dos vértices que tengan cinco aristas
#    con pesos aleatorios en metros
aristas = [
    ("cocina", "comedor"), ("cocina", "baño 1"), ("cocina", "terraza"),
    ("comedor", "sala de estar"), ("comedor", "quincho"), ("comedor", "baño 2"),
    ("sala de estar", "patio"), ("sala de estar", "terraza"), ("sala de estar", "habitación 1"),
    ("patio", "cochera"), ("patio", "terraza"), ("patio", "quincho"),
    ("terraza", "baño 1"), ("terraza", "baño 2"), ("terraza", "habitación 2"),
    ("habitación 1", "habitación 2"), ("habitación 1", "baño 1"), ("habitación 2", "quincho"),
    ("baño 1", "baño 2"), ("baño 1", "quincho"), ("cochera", "comedor"),
]

# Asignar distancias aleatorias para cada arista
for origen, destino in aristas:
    peso = randint(1, 15)  # Asignamos un peso entre 1 y 15 metros
    grafo.insert_arista(origen, destino, peso)

# c. Obtener el árbol de expansión mínima y la cantidad total de metros de cable
bosque_minimo = grafo.kruskal("cocina")
costo_total = 0

# Sumar los costos de cada arista en el árbol de expansión mínima
for arista in bosque_minimo:
    partes = arista.split(";")
    for parte in partes:
        _, _, peso = parte.split("-")
        costo_total += int(peso)

print("El árbol de expansión mínima conecta todos los ambientes y requiere un total de", costo_total, "metros de cable.")

# d. Determinar el camino más corto entre "habitación 1" y "sala de estar"
camino_corto = grafo.dijkstra("habitación 1")

# Calcular la distancia total desde "habitación 1" hasta "sala de estar"
distancia_total = 0
camino = []
while not camino_corto.is_empty():
    nodo = camino_corto.pop()
    if nodo[1][0] == "sala de estar":
        while nodo:
            camino.insert(0, nodo[1][0])
            nodo = nodo[1][2]
        distancia_total = nodo[0]
        break

print("El camino más corto desde 'habitación 1' hasta 'sala de estar' es:", " -> ".join(camino))
print("Se necesitan", distancia_total, "metros de cable de red para conectar el router con el Smart TV.")
