class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __repr__(self):
        return f"{self.nombre} (#{self.numero}, tipos: {', '.join(self.tipos)})"


class BinaryTree:
    class __Node:
        def __init__(self, pokemon, left=None, right=None):
            self.pokemon = pokemon
            self.left = left
            self.right = right

    def __init__(self, key_function):
        self.root = None
        self.key_function = key_function

    def insert(self, pokemon):
        def __insert(node, pokemon):
            if node is None:
                return self.__Node(pokemon)
            elif self.key_function(pokemon) < self.key_function(node.pokemon):
                node.left = __insert(node.left, pokemon)
            else:
                node.right = __insert(node.right, pokemon)
            return node

        self.root = __insert(self.root, pokemon)

    def search(self, key):
        def __search(node, key):
            if node is None:
                return None
            if self.key_function(node.pokemon) == key:
                return node.pokemon
            elif key < self.key_function(node.pokemon):
                return __search(node.left, key)
            else:
                return __search(node.right, key)

        return __search(self.root, key)

    def proximity_search(self, prefix):
        results = []

        def __proximity_search(node, prefix):
            if node is not None:
                if node.pokemon.nombre.startswith(prefix):
                    results.append(node.pokemon)
                __proximity_search(node.left, prefix)
                __proximity_search(node.right, prefix)

        __proximity_search(self.root, prefix)
        return results

    def in_order(self):
        results = []

        def __in_order(node):
            if node is not None:
                __in_order(node.left)
                results.append(node.pokemon)
                __in_order(node.right)

        __in_order(self.root)
        return results

    def by_level(self):
        if self.root is None:
            return []
        level_list = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            level_list.append(current.pokemon)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return level_list


class Pokedex:
    def __init__(self):
        self.trees = {
            'nombre': BinaryTree(lambda p: p.nombre),
            'numero': BinaryTree(lambda p: p.numero),
            'tipo': BinaryTree(lambda p: p.tipos[0])
        }

    def insert_pokemon(self, pokemon):
        self.trees['nombre'].insert(pokemon)
        self.trees['numero'].insert(pokemon)
        for tipo in pokemon.tipos:
            self.trees['tipo'].insert(pokemon)

    def search_pokemon_by_number(self, numero):
        return self.trees['numero'].search(numero)

    def search_pokemon_by_name(self, name):
        return self.trees['nombre'].proximity_search(name)

    def list_pokemons_by_type(self, tipo):
        results = []

        def collect_by_type(node):
            if node is not None:
                if tipo in node.pokemon.tipos:
                    results.append(node.pokemon)
                collect_by_type(node.left)
                collect_by_type(node.right)

        collect_by_type(self.trees['tipo'].root)
        return results

    def list_all(self):
        return self.trees['numero'].in_order()

    def count_by_type(self, tipo):
        count = 0
        def count_types(node):
            nonlocal count
            if node is not None:
                if tipo in node.pokemon.tipos:
                    count += 1
                count_types(node.left)
                count_types(node.right)

        count_types(self.trees['tipo'].root)
        return count


pokedex = Pokedex()

pokedex.insert_pokemon(Pokemon("Bulbasaur", 1, ["Planta", "Veneno"]))
pokedex.insert_pokemon(Pokemon("Charmander", 4, ["Fuego"]))
pokedex.insert_pokemon(Pokemon("Squirtle", 7, ["Agua"]))
pokedex.insert_pokemon(Pokemon("Pikachu", 25, ["Eléctrico"]))
pokedex.insert_pokemon(Pokemon("Jolteon", 135, ["Eléctrico"]))
pokedex.insert_pokemon(Pokemon("Tyrantrum", 696, ["Roca", "Dragón"]))
pokedex.insert_pokemon(Pokemon("Lycanroc", 744, ["Roca"]))

print("Búsqueda por número (1):", pokedex.search_pokemon_by_number(1))

# b)
numero_a_buscar = 1
pokemon_encontrado = pokedex.search_pokemon_by_number(numero_a_buscar)
if pokemon_encontrado:
    print(f"Datos del Pokémon con número {numero_a_buscar}: {pokemon_encontrado}")
else:
    print(f"No se encontró Pokémon con número {numero_a_buscar}")
# b)
nombre_a_buscar = "Squi"
pokemons_encontrados = pokedex.search_pokemon_by_name(nombre_a_buscar)
print(f"Pokémons que contienen '{nombre_a_buscar}': {pokemons_encontrados}")

# c) 
print("Pokémons de tipo 'Agua':", pokedex.list_pokemons_by_type("Agua"))

print("Pokémons de tipo 'Fuego':", pokedex.list_pokemons_by_type("Fuego"))

print("Pokémons de tipo 'Planta':", pokedex.list_pokemons_by_type("Planta"))

print("Pokémons de tipo 'Eléctrico':", pokedex.list_pokemons_by_type("Eléctrico"))


# d) 
print("Listado de Pokémon por número:", pokedex.list_all())

# e)
print("Datos de Jolteon:", pokedex.search_pokemon_by_number(135))
print("Datos de Lycanroc:", pokedex.search_pokemon_by_number(744))
print("Datos de Tyrantrum:", pokedex.search_pokemon_by_number(696))

# f)
count_eléctrico = pokedex.count_by_type("Eléctrico")
count_acero = pokedex.count_by_type("Acero")
print(f"Número de Pokémon de tipo Eléctrico: {count_eléctrico}")
print(f"Número de Pokémon de tipo Acero: {count_acero}")