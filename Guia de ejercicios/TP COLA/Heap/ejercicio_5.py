from ClassHeap import HeapMax
from ClassQueue import Queue

class Request:
    def __init__(self, general_name, planet, description):
        self.general_name = general_name
        self.planet = planet
        self.description = description

    def __str__(self):
        
        return f"General: {self.general_name}, Planet: {self.planet}, Description: {self.description}"


class PriorityQueue(HeapMax):
    def __init__(self):
        super().__init__()

    def add_request(self, request, priority):
        self.arrive(request, priority)

    def process_requests(self):
        log = []
        while self.size() > 0:
            request = self.atention()
            print("Procesando pedido:", request)
            log.append(request)
            input("Presiona para continuar") 
        return log


queue = PriorityQueue()
log = []

def get_priority(request):
    if (request.general_name == "Gran Inquisidor" or
        request.planet == "Lothal" or
        "Hera Syndulla" in request.description):
        return 3
    elif (request.general_name == "Agente Kallus" or
          "Destructor Estelar" in request.description or
          "AT-AT" in request.description):
        return 2
    else:
        return 1

requests = [
    Request("Gran Inquisidor", "Lothal", "Revisar las ultimas tácticas de Hera Syndulla"),
    Request("Agente Kallus", "Garel", "Actualizar sobre operaciones del Destructor Estelar"),
    Request("General Hux", "Coruscant", "Preparar planes de defensa para el próximo ataque"),
    Request("General Veers", "Hoth", "Inspeccionar la estrategia de despliegue de AT-AT"),
    Request("General Thrawn", "Naboo", "Evaluar el movimiento rebelde"),
    Request("General Tarkin", "Eriadu", "Planificar ataque a la fortaleza rebelde"),
    Request("General Armitage Hux", "Kashyyyk", "Coordinar con la flota Imperial"),
    Request("Gran Moff Tarkin", "Dagobah", "Prepararse para una posible evacuacion")
]

for request in requests:
    priority = get_priority(request)
    queue.add_request(request, priority)

log = queue.process_requests()

print("\nBitácora de pedidos de alta prioridad:")
for entry in log:
    print(entry)
