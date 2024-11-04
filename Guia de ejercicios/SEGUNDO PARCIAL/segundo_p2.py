from package.ClassQueue import Queue
from package.heap import HeapMin
from package.ClassStack import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print("Nodos:")
        for nodo in self.elements:
            print(f"Personaje: {nodo['value']}")
            print("    Aristas:")
            for arista in nodo['aristas']:
                print(f"    - {arista['value']} (Episodios: {arista['peso']})")
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index
        return None

    def insert_vertice(self, value):
        nodo = {
            'value': value,  # Nombre del personaje
            'aristas': [],   # Aristas que contienen las relaciones
            'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {
                'value': destino,  # Nombre del personaje destino
                'peso': peso       # Cantidad de episodios
            }
            self.elements[pos_origen]['aristas'].append(arista)
            # Añadir arista en el sentido inverso si el grafo no es dirigido
            if not self.dirigido:
                arista_inversa = {
                    'value': origen,  # Nombre del personaje origen
                    'peso': peso      # Cantidad de episodios
                }
                self.elements[pos_destino]['aristas'].append(arista_inversa)

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = []
        aristas = HeapMin()
        for nodo in self.elements:
            bosque.append(nodo['value'])
            for adyacente in nodo['aristas']:
                # Se usa la arista como un conjunto (personaje1, personaje2, peso)
                aristas.arrive([nodo['value'], adyacente['value']], adyacente['peso'])

        resultado = []
        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            if origen is not None and destino is not None and origen != destino:
                if origen > destino:
                    vertice_ori = bosque.pop(origen)
                    vertice_des = bosque.pop(destino)
                else:
                    vertice_des = bosque.pop(destino)
                    vertice_ori = bosque.pop(origen)

                resultado.append((vertice_ori, vertice_des, arista[2]))  # Guardar como (origen, destino, peso)
                bosque.append(f'{vertice_ori}-{vertice_des}-{arista[2]}')  # Guardar en el bosque
        return resultado

    def max_episodes_shared(self):
        max_episodes = 0
        characters = (None, None)
        for nodo in self.elements:
            for arista in nodo['aristas']:
                if arista['peso'] > max_episodes:
                    max_episodes = arista['peso']
                    characters = (nodo['value'], arista['value'])
        return characters, max_episodes

    def has_character(self, character_name):
        for nodo in self.elements:
            if nodo['value'] == character_name:
                return True
        return False

def cargar_personajes():
    graph = Graph(dirigido=False)

    personajes = [
        "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
        "C-3PO", "Leia", "Rey", "Kylo Ren", 
        "Chewbacca", "Han Solo", "R2-D2", "BB-8"
    ]

    for personaje in personajes:
        graph.insert_vertice(personaje)

    relaciones = [
        ("Luke Skywalker", "Darth Vader", 5),
        ("Yoda", "Darth Vader", 3),
        ("Yoda", "Luke Skywalker", 4),
        ("Leia", "Luke Skywalker", 4),
        ("Leia", "Darth Vader", 2),
        ("Rey", "Kylo Ren", 3),
        ("Chewbacca", "Han Solo", 6),
        ("R2-D2", "C-3PO", 5),
        ("BB-8", "Rey", 2),
        ("Boba Fett", "Darth Vader", 3)
    ]

    for origen, destino, peso in relaciones:
        graph.insert_arista(origen, destino, peso)

    return graph

# Cargar personajes y mostrar el grafo
graph = cargar_personajes()
graph.show_graph()

# Hallar el árbol de expansión mínimo y verificar si contiene a Yoda
arbol_minimo = graph.kruskal()
print("Árbol de Expansión Mínimo:")
for origen, destino, peso in arbol_minimo:
    print(f"{origen} - {destino} (Episodios: {peso})")
print("Contiene a Yoda:", graph.has_character("Yoda"))

# Determinar el número máximo de episodios compartidos
characters, max_episodes = graph.max_episodes_shared()
print(f"Los personajes que comparten el máximo de episodios son {characters[0]} y {characters[1]} con {max_episodes} episodios.")
