def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print()
    
def search(lst, key, value):
    for index, item in enumerate(lst):
        if item[key] == value:
            return index
    return None
        
def by_name(item):
    return item['nombre']


entrenadores = [
    {'nombre': 'Juan', 'Cantidad de torneos': 20, 'Batallas perdidas': 115, 'Batalals ganadas': 120, 'ID': 1},
    {'nombre': 'Pédro', 'Cantidad de torneos': 10, 'Batallas perdidas': 120, 'Batalals ganadas': 125,'ID': 2},
    {'nombre': 'Ariel', 'Cantidad de torneos': 0, 'Batallas perdidas': 150, 'Batalals ganadas': 100, 'ID': 3},
    {'nombre': 'Yesi', 'Cantidad de torneos': 3, 'Batallas perdidas': 170, 'Batalals ganadas': 150, 'ID': 4},
    {'nombre': 'Analia', 'Cantidad de torneos': 2, 'Batallas perdidas': 155, 'Batalals ganadas': 100, 'ID': 5},


]

lista_pokemones = []

pokemones = [
    {'Nombre': "A", 'Nivel': 12, 'Tipo': 'Agua', 'Sub-Tipo': "Tierra", 'IDS': 1},
    {'Nombre': "B", 'Nivel': 30, 'Tipo': 'Fuego', 'Sub-Tipo': "Volador", 'IDS': 1},
    {'Nombre': "C", 'Nivel': 23, 'Tipo': 'Tierra', 'Sub-Tipo': "Fuego", 'IDS': 2},
    {'Nombre': "D", 'Nivel': 45, 'Tipo': 'Volador', 'Sub-Tipo': "Fantasmal", 'IDS': 2},
    {'Nombre': "E", 'Nivel': 60, 'Tipo': 'Fuego', 'Sub-Tipo': "Electrico", 'IDS': 3},
    {'Nombre': "F", 'Nivel': 80, 'Tipo': 'Electrico', 'Sub-Tipo': "Agua", 'IDS': 4},
    {'Nombre': "G", 'Nivel': 100, 'Tipo': 'Fantasmal', 'Sub-Tipo': "", 'IDS': 5},
    {'Nombre': "H", 'Nivel': 120, 'Tipo': 'Agua', 'Sub-Tipo': "Fuego", 'IDS': 5},
]

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_pokemones.append(entrenador)
    
for pokemone in pokemones:
    pos = search(entrenadores, 'ID' , pokemones['IDS'])
    if pos is not None:
        lista_pokemones[pos]['sublist'].append(pokemone)
    else:
        print('No tiene entrenador')
        
lista_pokemones.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemones', lista_pokemones)
