from random import randint, choice
legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]

def hash_legiones(value):
    return legion[-2:]
    
def hash_numerica(value):
    return trooper[-3:]

tabla_legiones = {}
tabla_numerica = {}

for legion in legiones:
    tabla_legiones[legion] = []

for i in range(0, 100):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    clave = hash_numerica(trooper)
    if clave not in tabla_numerica:
        tabla_numerica[clave] = []
        
    tabla_legiones[hash_legiones(trooper)].append(trooper) 
    tabla_numerica[clave].append(trooper)


    #print(trooper, hash_numerica(trooper))



mission_assault = tabla_numerica.get('2342', [])
print("Stromtroppers para mision de asalto")
for index, trooper in enumerate(mission_assault):
    print(f'{index} - {trooper}')
print()

mision_exploracion = tabla_numerica.get('3245', [])
print("Stromtroppers para mision de exploracion")
for index, trooper in enumerate(mision_exploracion):
    print(f'{index} - {trooper}')
print()
    
mision_koth = tabla_legiones.get('CT', [])
print("Stromtroppers para mision a hoth")
for index, trooper in enumerate(mision_koth):
    print(f'{index} - {trooper}')
print()

mision_endor = tabla_legiones.get('TF', [])
print("Stromtroppers para mision a endor")
for index, trooper in enumerate(mision_endor):
    print(f'{index} - {trooper}')
print()



print(tabla_legiones)
print("Tabla Numerica:", tabla_numerica)
