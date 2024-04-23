from pila import Stack
from random import randint
pila = Stack()
pila_aux = Stack()

for i in range(5):
    num =randint(1,99)
    print(num)
    pila.push(num)
buscar = int(input("ingrese el numero que desea buscar su repetido: "))
acc= 0
while pila.size() > 0:
    data = pila.pop()
    if data == buscar :
        acc+= 1
print("el numero", buscar ,"se repitio", acc ,"veces")