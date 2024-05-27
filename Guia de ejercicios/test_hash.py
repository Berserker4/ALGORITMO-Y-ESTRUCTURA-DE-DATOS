from random import randint, choice
legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]

tabla_legiones = {}
for legion in legiones:
    tabla_legiones[legion] = []


for i in range(0, 10):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    legion = trooper[:2]
    tabla_legiones[legion].append(trooper)
    

print(tabla_legiones)
