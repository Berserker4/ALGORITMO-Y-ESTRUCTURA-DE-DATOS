
def by_name_jedis(lista, item):
    for jedi in lista:
        if jedi['name'] == item:
         return jedi

def by_name_especies(lista, item):
    jedi_especie = []
    for jedi in lista:
        if jedi['species'] == item:
            jedi_especie.append(jedi)
    return jedi_especie

def by_hegiht(item):
    return item['altura']

def search(list_values, criterio, value):
    for index, personaje in enumerate(list_values):
        if personaje[criterio] == value:
            return index
        
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

def show_list(name, jedis):
    for jedi in jedis:
        if jedi["name"] == name:
            print("Informacion de:", name)
            for key, value in jedi.items():
                print(f"{key}: {value}")
            break
    
    
    
class nodoLista():
    info, sig, sublista = None, None, None


