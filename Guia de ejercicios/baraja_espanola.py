from pila import Stack
import random

palos_cartas = ["Oro", "Copa", "Espada" , "Basto"]
valores_cartas = ["1","2","3","4","5","6","7","10","11","12"]

pila = Stack()
pila_oros = Stack()
pila_copas = Stack()
pila_espadas= Stack()
pila_bastos = Stack()


mazo = [(valor, palos) for valor in valores_cartas for palos in palos_cartas]
random.shuffle(mazo)
for carta in mazo:
    pila.push(carta)


print("Cartas aleatoreas:")
print(pila.on_top())
    
while pila.size() > 1:
    data = pila.pop()
    if data[1] == "Oro": 
        pila_oros.push(data)
    elif data[1] == "Copa":
        pila_copas.push(data)
    elif data[1] == "Espada":
        pila_espadas.push(data)
    elif data[1] == "Basto":
        pila_bastos.push(data)
        

print(pila_bastos.size())
print(pila_copas.size())
print(pila_oros.size())
print(pila_espadas.size())


    
    
    
    


