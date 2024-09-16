from ClassQueue import Queue
class Character:
    def __init__(self, character_name, superhero_name, gender):
        self.character_name = character_name
        self.superhero_name = superhero_name
        self.gender = gender

    def __str__(self):
        return f"{self.character_name}, {self.superhero_name}, {self.gender}"


queue = Queue()
queue.arrive(Character("Tony Stark", "Iron Man", "M"))
queue.arrive(Character("Steve Rogers", "Captain America", "M"))
queue.arrive(Character("Natasha Romanoff", "Black Widow", "F"))
queue.arrive(Character("Carol Danvers", "Captain Marvel", "F"))
queue.arrive(Character("Scott Lang", "Ant-Man", "M"))
queue.arrive(Character("Wanda Maximoff", "Scarlet Witch", "F"))
queue.arrive(Character("Stephen Strange", "Doctor Strange", "M"))

def find_character_by_superhero(queue, superhero_name):
    for i in range(queue.size()):
        character = queue.attention()
        if character.superhero_name == superhero_name:
            print(f"El personaje de {superhero_name} es {character.character_name}")
        queue.arrive(character)

def show_female_superheroes(queue):
    print("Superhéroes femeninos:")
    for i in range(queue.size()):
        character = queue.attention()
        if character.gender == "F":
            print(character.superhero_name)
        queue.arrive(character)

def show_male_characters(queue):
    print("Personajes masculinos:")
    for i in range(queue.size()):
        character = queue.attention()
        if character.gender == "M":
            print(character.character_name)
        queue.arrive(character)

def find_superhero_by_character(queue, character_name):
    for i in range(queue.size()):
        character = queue.attention()
        if character.character_name == character_name:
            print(f"El superhéroe de {character_name} es {character.superhero_name}")
        queue.arrive(character)

def show_characters_starting_with_s(queue):
    print("Personajes y superhéroes cuyos nombres empiezan con 'S':")
    for i in range(queue.size()):
        character = queue.attention()
        if character.character_name.startswith("S") or character.superhero_name.startswith("S"):
            print(character)
        queue.arrive(character)

def check_for_carol_danvers(queue):
    found = False
    for i in range(queue.size()):
        character = queue.attention()
        if character.character_name == "Carol Danvers":
            print(f"Carol Danvers es {character.superhero_name}")
            found = True
        queue.arrive(character)
    
    if not found:
        print("Carol Danvers no está en la cola.")


find_character_by_superhero(queue, "Captain Marvel")

print()

show_female_superheroes(queue)

print()

show_male_characters(queue)

print()

find_superhero_by_character(queue, "Scott Lang")

print()

show_characters_starting_with_s(queue)

print() 

check_for_carol_danvers(queue)
