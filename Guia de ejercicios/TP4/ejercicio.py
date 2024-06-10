from random import randint, choice
class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def insert(self, key, value):
        index = hash(key) % len(self.table)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % len(self.table)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo, numero):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
        self.numero = numero

def hash_tipo(valor):
    # Simplemente devolvemos el valor, ya que usaremos el tipo como clave
    return valor

def hash_digito(numero):
    return numero[-1:]

def hash_nivel(nivel):
    return nivel // 10

table_tipo = {}
table_numerica = {}
table_nivel = {pos: [] for pos in range(10)}

pokemons = [
    {'name': 'Minior', 'nivel': 22, 'tipo': 'roca', 'subtipo': 'volador', "numero": 345},
    {'name': 'Tyrantrum', 'nivel': 12, 'tipo': 'roca', 'subtipo': 'dragon', "numero": 532},
    {'name': 'Mimikyu', 'nivel': 47, 'tipo': 'fantasma', 'subtipo': 'hada', "numero": 789},
    {'name': 'Onix', 'nivel': 27, 'tipo': 'tierra', 'subtipo': 'roca', "numero": 123},
    {'name': 'Wingull', 'nivel': 7, 'tipo': 'agua', 'subtipo': 'volador', "numero": 342},
    {'name': 'Electrode', 'nivel': 90, 'tipo': 'electrico', 'subtipo': None, "numero": 998},
    {'name': 'Metagross', 'nivel': 72, 'tipo': 'acero', 'subtipo': 'psiquico', "numero": 877},
    {'name': 'Eevee', 'nivel': 1, 'tipo': 'normal', 'subtipo': None, "numero": 236}
]

for pokemon_data in pokemons:
    pokemon = Pokemon(pokemon_data['name'], pokemon_data['nivel'], pokemon_data['tipo'], pokemon_data['subtipo'], pokemon_data["numero"])
    tipo = pokemon.tipo
    if tipo not in table_tipo:
        table_tipo[tipo] = []
        table_tipo[tipo].append((pokemon.nombre, pokemon.subtipo))


print("Tabla de hash del tipo de Pokémon:")
for tipo, index in table_tipo.items():
    print(f'Tipo: {tipo}, Pokemones: {index}')

for pokemon_data in pokemons:
    pokemon = Pokemon(pokemon_data['name'], pokemon_data['nivel'], pokemon_data['tipo'], pokemon_data['subtipo'], pokemon_data["numero"])
    clave = hash_digito(str(pokemon.numero))
    if clave not in table_numerica:
        table_numerica[clave] = []
    table_numerica[clave].append((pokemon.nombre))             
             
#print(table_numerica)

for pokemon_data in pokemons:
    pokemon = Pokemon(pokemon_data['name'], pokemon_data['nivel'], pokemon_data['tipo'], pokemon_data['subtipo'], pokemon_data["numero"])
    posicion = hash_nivel(pokemon.nivel)
    table_nivel[posicion].append((pokemon.nombre, pokemon.nivel, pokemon.subtipo))

print("Tabla de hash del nivel de Pokémon:")
for posicion, pokemones in table_nivel.items():
    print(f'Posición: {posicion}, Pokemones: {pokemones}')

#for pokemon_data in pokemons:
#    pokemon = Pokemon(pokemon_data['numero'])
#    table_digito[pokemon.nombre] = []
#    if pokemon.tipo not in table_tipo:
#        table_tipo[pokemon.tipo] = []

#for i in range(0, 8):
#    pokemon = choice(pokemons)
#    digito = f"{pokemon['name']}-{randint(1, 100)}"
#    clave = hash_digito(str(pokemon['nivel']))
#    if clave not in table_digito:
#        table_digito[clave] = []
#    
#    table_tipo[pokemon['tipo']].append(digito) 
#    table_digito[clave].append(digito)
#    
#print(table_tipo)