from random import randint, choice
def lista_inverso(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + lista_inverso(lista[:-1])
    
lista = [1,2,3,4,5,6,7,8,9,10]

print("Lista:", lista)
print("Lista inversa:", lista_inverso(lista))
    