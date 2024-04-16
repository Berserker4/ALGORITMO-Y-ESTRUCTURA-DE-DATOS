import random
from Pila import Stack

palos_cartas = ["Oros", "Copas", "Espadas" , "Bastos"]
valores_cartas = ["1","2","3","4","5","6","7","10","11","12"]

pila = Stack()
pila_oros = Stack()
pila_copas = Stack()
pila_espadas= Stack()
pila_bastos = Stack()


def mazo_aleatoreo():
    mazo = [(valor, palos) for valor in valores_cartas for palos in palos_cartas]
    random.shuffle(mazo)
    for carta in mazo:
        pila.append(carta)
        return pila


pila_cartas = mazo_aleatoreo()

print("Cartas alatoreas:")
while pila_cartas:
    carta = pila_cartas.pop()
    print(carta[0], "de", carta[1])
    
while pila_cartas.size() > 1:
    data = pila_cartas.pop()
    if data == "Oros": 
        data.push(pila_oros)
    elif data == "Copas":
        data.push(pila_copas)
    elif data == "Espadas":
        data.push(pila_espadas)
    elif data == "Bastos":
        data.push(pila_bastos)
    
    
    
    


