from heap import HeapMin
from ClassStack import Stack

class Graph:
    def __init__(self):
        self.elements = []

    def insert_vertice(self, nombre, pais, tipo):
        nodo = {
            'nombre': nombre,
            'pais': pais,
            'tipo': tipo,
            'aristas': [],
            'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, distancia):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {'valor': destino, 'peso': distancia}
            self.elements[pos_origen]['aristas'].append(arista)
            arista_inversa = {'valor': origen, 'peso': distancia}
            self.elements[pos_destino]['aristas'].append(arista_inversa)

    def search(self, nombre):
        for index, element in enumerate(self.elements):
            if element['nombre'] == nombre:
                return index
        return None

    def get_marvels_by_type(self, tipo):
        return [nodo['nombre'] for nodo in self.elements if nodo['tipo'] == tipo]

    def kruskal(self):
        pass

    def countries_with_architectural_and_natural(self):
        tipos = {}
        for nodo in self.elements:
            if nodo['pais'] not in tipos:
                tipos[nodo['pais']] = set()
            tipos[nodo['pais']].add(nodo['tipo'])
        
        return any(len(tipos[pais]) > 1 for pais in tipos)

    def countries_with_multiple_marvels(self):
        tipos = {}
        for nodo in self.elements:
            if nodo['pais'] not in tipos:
                tipos[nodo['pais']] = {}
            if nodo['tipo'] not in tipos[nodo['pais']]:
                tipos[nodo['pais']][nodo['tipo']] = 0
            tipos[nodo['pais']][nodo['tipo']] += 1
        
        return any(count > 1 for pais in tipos for count in tipos[pais].values())

grafo = Graph()
grafo.insert_vertice("Chichén Itzá", "México", "arquitectónica")
grafo.insert_vertice("Machu Picchu", "Perú", "arquitectónica")
grafo.insert_vertice("Cristo Redentor", "Brasil", "arquitectónica")
grafo.insert_vertice("Gran Muralla China", "China", "arquitectónica")
grafo.insert_vertice("Coloso de Rhode", "Grecia", "arquitectónica")
grafo.insert_vertice("Taj Mahal", "India", "arquitectónica")
grafo.insert_vertice("Petra", "Jordania", "arquitectónica")

grafo.insert_arista("Chichén Itzá", "Machu Picchu", 2500)
grafo.insert_arista("Chichén Itzá", "Cristo Redentor", 5000)
grafo.insert_arista("Machu Picchu", "Gran Muralla China", 3000)
grafo.insert_arista("Cristo Redentor", "Coloso de Rhode", 4000)
grafo.insert_arista("Taj Mahal", "Petra", 6000)

print("Maravillas arquitectónicas:", grafo.get_marvels_by_type("arquitectónica"))
print("¿Existen países con maravillas arquitectónicas y naturales?", grafo.countries_with_architectural_and_natural())
print("¿Algún país tiene más de una maravilla del mismo tipo?", grafo.countries_with_multiple_marvels())
