from arbol_avl import BinaryTree
from cola import Queue
arbol = BinaryTree()
arbol.insert_node("Iron Man", {"is_hero": True})
arbol.insert_node("Thanos", {"is_hero": False})
arbol.insert_node("Captain America", {"is_hero": True})
arbol.insert_node("Loki", {"is_hero": False})
arbol.insert_node("Doctor Str", {"is_hero": True})
arbol.insert_node("Red Skull", {"is_hero": False})

print("Villanos ordenados alfabéticamente:")
arbol.inorden_villanos()

print("\nSuperhéroes que comienzan con 'C':")
arbol.inorden_superheros_start_with("C")

total_superheroes = arbol.contar_super_heroes()
print(f"\nTotal de superhéroes en el árbol: {total_superheroes}")

nodo = arbol.search("Doctor Str") 
if nodo is not None:
    nodo.value = "Doctor Strange"
print("\nNombre corregido de Doctor Strange")

def inorden_superheroes_descendente(root):
    if root is not None:
        inorden_superheroes_descendente(root.right)
        if root.other_value.get('is_hero') is True:
            print(root.value)
        inorden_superheroes_descendente(root.left)

print("\nSuperhéroes en orden descendente:")
inorden_superheroes_descendente(arbol.root)

heroes_tree = BinaryTree()
villains_tree = BinaryTree()

def split_heroes_villains(root):
    if root is not None:
        if root.other_value.get('is_hero') is True:
            heroes_tree.insert_node(root.value, root.other_value)
        else:
            villains_tree.insert_node(root.value, root.other_value)
        split_heroes_villains