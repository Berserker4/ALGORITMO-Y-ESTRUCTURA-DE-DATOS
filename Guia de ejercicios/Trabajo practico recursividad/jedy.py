def usar_la_fuerza(mochila, pasos=0):
    if not mochila:
        return False, pasos
    
    objeto = mochila.pop(0)
    pasos += 1
    
    if objeto == "Sable de luz":
        return True, pasos
    
    if not mochila:
        return False, pasos
    
    return usar_la_fuerza(mochila, pasos)

mochila_jedi = ["Madera", "Ojo humano", "sable defectuoso", "Sable de luz", "Motor XVVU", "Sable oscuro"]
sable_encontrado, pasos_necesarios = usar_la_fuerza(mochila_jedi.copy())
if sable_encontrado:
    print("La mochila contiene un sable de luz", "Fueron necesario sacar", pasos_necesarios-1)
else:
    print("No se encontro un sable de luz en la mochila")
