from arbol_avl import BinaryTree
from cola import Queue
    
def inorden_with_defeated_by(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                defeated_by = root.other_value.get('defeated_by', 'Nadie')
                print(f"Criatura: {root.value}, Derrotado por: {defeated_by}")
                __inorden(root.right)

        __inorden(self.root)

def add_description(self, creature_name, description):
        node = self.search(creature_name)
        if node:
            node.other_value["description"] = description

def show_talos_info(self):
        talos_node = self.search("Talos")
        if talos_node:
            print(f"Criatura: {talos_node.value}, Derrotado por: {talos_node.other_value.get('defeated_by')}, "
                  f"Descripción: {talos_node.other_value.get('description', 'No disponible')}")

def top_heroes(self):
        def __collect_heroes(root, counter):
            if root is not None:
                defeated_by = root.other_value.get('defeated_by')
                if defeated_by:
                    counter[defeated_by] += 1
                __collect_heroes(root.left, counter)
                __collect_heroes(root.right, counter)

        hero_counter = Counter()
        __collect_heroes(self.root, hero_counter)
        return hero_counter.most_common(3)

def creatures_defeated_by(self, hero):
        def __inorden_defeated_by(root):
            if root is not None:
                __inorden_defeated_by(root.left)
                if root.other_value.get('defeated_by') == hero:
                    print(root.value)
                __inorden_defeated_by(root.right)

        __inorden_defeated_by(self.root)

def undefeated_creatures(self):
        def __inorden_undefeated(root):
            if root is not None:
                __inorden_undefeated(root.left)
                if root.other_value.get('defeated_by') is None:
                    print(root.value)
                __inorden_undefeated(root.right)

        __inorden_undefeated(self.root)

def add_capture(self, creature_name, capturer):
        node = self.search(creature_name)
        if node:
            node.other_value["captured_by"] = capturer

def mark_heracles_captures(self):
        captures = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
        for creature in captures:
            self.add_capture(creature, "Heracles")

def proximity_search(self, search_value):
        def __proximity_search(root, search_value):
            if root is not None:
                __proximity_search(root.left, search_value)
                if root.value.startswith(search_value):
                    print(root.value)
                __proximity_search(root.right, search_value)

        __proximity_search(self.root, search_value)

def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    root.right, value_delete = __delete(root.right, value)
                else:
                    value_delete = root.value
                    if root.left is None:
                        return root.right, value_delete
                    elif root.right is None:
                        return root.left, value_delete
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
            return root, value_delete

        if self.root is not None:
            self.root, _ = __delete(self.root, value)

def modify_stymphalian_birds(self):
        node = self.search("Aves del Estínfalo")
        if node:
            node.other_value["defeated_by"] = "Heracles"

def rename_ladon(self):
        node = self.search("Ladón")
        if node:
            node.value = "Dragón Ladón"

def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

def heracles_captures(self):
        def __inorden_captures(root):
            if root is not None:
                __inorden_captures(root.left)
                if root.other_value.get('captured_by') == "Heracles":
                    print(root.value)
                __inorden_captures(root.right)

        __inorden_captures(self.root)


creatures_data = [
    {"name": "Ceto", "defeated_by": None, "description": "Antigua deidad marina"},
    {"name": "Tifón", "defeated_by": "Zeus", "description": "Gigante monstruoso con múltiples cabezas"},
    {"name": "Equidna", "defeated_by": "Argos Panoptes", "description": "Monstruo mitad mujer, mitad serpiente"},
    {"name": "Dino", "defeated_by": None, "description": "Una de las Greyas"},
    {"name": "Pefredo", "defeated_by": None, "description": "Otra de las Greyas"},
    {"name": "Enio", "defeated_by": None, "description": "La tercera de las Greyas"},
    {"name": "Escila", "defeated_by": None, "description": "Monstruo marino de múltiples cabezas"},
    {"name": "Caribdis", "defeated_by": None, "description": "Monstruo marino que causaba remolinos"},
    {"name": "Medusa", "defeated_by": "Perseo", "description": "Gorgona con serpientes en lugar de cabello"},
    {"name": "Ladón", "defeated_by": "Heracles", "description": "Dragón guardián del jardín de las Hespérides"},
    {"name": "León de Nemea", "defeated_by": "Heracles", "description": "León con piel impenetrable"},
    {"name": "Hidra de Lerna", "defeated_by": "Heracles", "description": "Monstruo con muchas cabezas regenerativas"},
    {"name": "Talos", "defeated_by": "Medea", "description": "Gigante de bronce que protegía Creta"},
    {"name": "Cerbero", "defeated_by": None, "description": "Perro guardián del Hades"},
    {"name": "Toro de Creta", "defeated_by": "Teseo", "description": "Monstruo capturado en Creta"},
    {"name": "Cierva Cerinea", "defeated_by": None, "description": "Cierva divina capturada"},
    {"name": "Jabalí de Erimanto", "defeated_by": None, "description": "Jabalí capturado por Heracles"}
]

tree = BinaryTree()

for creature in creatures_data:
    tree.insert_node(creature["name"], {"defeated_by": creature["defeated_by"], "description": creature["description"]})

tree.inorden_with_defeated_by()

tree.add_description("Cerbero", "Perro guardián de tres cabezas del Hades")

tree.show_talos_info()

print(tree.top_heroes())

tree.creatures_defeated_by("Heracles")

tree.undefeated_creatures()

tree.add_capture("Cerbero", "Heracles")

tree.mark_heracles_captures()

tree.proximity_search("C")

tree.delete_node("Basilisco")
tree.delete_node("Sirenas")

tree.modify_stymphalian_birds()
tree.rename_ladon()
tree.by_level()
tree.heracles_captures()