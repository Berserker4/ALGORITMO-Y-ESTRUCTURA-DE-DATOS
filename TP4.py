class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append(value)

    def hash_function(self, key):
        raise NotImplementedError("")

    def get_values(self, key):
        index = self.hash_function(key)
        return self.table[index]

class HashTableByType(HashTable):
    def hash_function(self, key):
        return hash(key) % self.size

class HashTableByLastDigit(HashTable):
    def hash_function(self, key):
        return int(str(key)[-1]) % self.size

class HashTableByLevel(HashTable):
    def hash_function(self, key):
        return key // 10 % self.size

class Pokedex:
    def __init__(self):
        self.table_by_type = HashTableByType(50)
        self.table_by_last_digit = HashTableByLastDigit(10)
        self.table_by_level = HashTableByLevel(10)
        self.all_pokemons = []

    def add_pokemon(self, number, name, types, level):
        pokemon = {
            'number': number,
            'name': name,
            'types': types,
            'level': level
        }
        self.all_pokemons.append(pokemon)
        for type_ in types:
            self.table_by_type.insert(type_, pokemon)
        self.table_by_last_digit.insert(number, pokemon)
        self.table_by_level.insert(level, pokemon)

    def show_pokemons_by_last_digit(self, digits):
        result = []
        for digit in digits:
            pokemons = self.table_by_last_digit.get_values(digit)
            result.extend(pokemons)
        return result

    def show_pokemons_by_level(self, levels):
        result = []
        for level in levels:
            pokemons = self.table_by_level.get_values(level)
            result.extend(pokemons)
        return result

    def show_pokemons_by_type(self, types):
        result = []
        for type_ in types:
            pokemons = self.table_by_type.get_values(type_)
            result.extend(pokemons)
        return result

# Ejemplo de uso:
pokedex = Pokedex()
pokedex.add_pokemon(1, 'Bulbasaur', ['Planta', 'Veneno'], 5)
pokedex.add_pokemon(25, 'Pikachu', ['Eléctrico'], 7)
pokedex.add_pokemon(4, 'Charmander', ['Fuego'], 10)
pokedex.add_pokemon(120, 'Staryu', ['Agua'], 15)
pokedex.add_pokemon(6, 'Charizard', ['Fuego', 'Volador'], 36)

# Mostrar Pokémons cuyos números terminan en 3, 7 y 9:
print("Pokémons cuyos números terminan en 3, 7 y 9:")
print(pokedex.show_pokemons_by_last_digit([3, 7, 9]))

# Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10:
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
print(pokedex.show_pokemons_by_level([2, 5, 10]))

# Mostrar Pokémons de tipo Acero, Fuego, Eléctrico, Hielo:
print("Pokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
print(pokedex.show_pokemons_by_type(['Acero', 'Fuego', 'Eléctrico', 'Hielo']))
