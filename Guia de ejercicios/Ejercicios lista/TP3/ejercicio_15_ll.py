from lista import Lista
from random import randint
from random import choice

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return self.nombre
    
class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - {self.nivel}'

lista_entrenadores = Lista()

entrenadores = [
    {'name': 'Brock','tg':5,'bg':27,'bp':12},
    {'name': 'Misty','tg':6,'bg':32,'bp':13},
    {'name': 'Ash','tg':0,'bg':50,'bp':58},
    {'name': 'Juan L','tg': 0,'bg':5,'bp':141},
    {'name': 'Serena','tg':3 ,'bg':28 ,'bp':8}
]

pokemons = [
    {'name':'Minior','nivel':22,'tipo':'roca','subtipo':'volador'},
    {'name':'Tyrantrum','nivel':12,'tipo':'roca','subtipo':'dragon'},
    {'name':'Mimikyu','nivel': 47,'tipo':'fantasma','subtipo':'hada'},
    {'name':'Onix','nivel':27,'tipo':'tierra','subtipo':'roca'},
    {'name':'Wingull','nivel':7,'tipo':'agua','subtipo':'volador'},
    {'name':'Electrode','nivel': 100,'tipo':'electrico','subtipo': None},
    {'name': 'Metagross', 'nivel':72, 'tipo':'acero', 'subtipo':'psiquico'},
    {'name': 'Eevee', 'nivel':1, 'tipo':'normal', 'subtipo':None}
]

for entrenador in entrenadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],entrenador['tg'],entrenador['bp'],entrenador['bg']),'nombre')

for entrenador in entrenadores:
    for i in range(randint(1,5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'],'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],pokemon['nivel'],pokemon['tipo'],pokemon['subtipo']),'nombre')        

lista_entrenadores.barrido_lista_lista()
print()


entrenador = input('Ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    print('El entrenador tiene:',pos.sublista.tamanio(),'pokemons')


print()
print('Entrenadores que hayan ganado más de tres torneos: ')
lista_entrenadores.barrido_entrenador_mas_tres()


print()
print('Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados: ')
mayor = lista_entrenadores.mayor('torneos_ganados')
print(mayor.info, mayor.sublista.mayor('nivel').info)


print()
entrenador = input('Ingrese nombre del entrenador que desea saber datos y sus Pokémons: ')
pos = lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    print(f'el entrenador tiene {pos.info}')
    print('sus pokemons:')
    pos.sublista.barrido()


print()
print("Entrenadores con mas del 79% de batallas ganadas:")
lista_entrenadores.barrido_porc_victorias()


print()
print("Entrenadores con Pokemones de tipo fuego y planta o agua/volador:")
lista_entrenadores.barrido_tipo_subtipo()


print()
entrenador = input('Ingrese nombre del entrenador que desea saber promedio de nivel de los Pokémons ')
pos = lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    print("El promedio de nivel de los Pokémons del entrenador",pos.info.nombre,"es",pos.sublista.barrido_promedio())


print()
pokemon = input('Ingrese pokemon: ')
print(lista_entrenadores.barrido_cuantos_tienen_pokemon(pokemon), 'entrenadores tienen el pokemon', pokemon)


print()
print('Entrenadores con pokemons repetidos:',lista_entrenadores.barrido_repetidos())


print()
print("Entrenadores que tienen uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull:")
lista_entrenadores.barrido_tiene_pokemon(['Tyrantrum', 'Terrakion', 'Wingull'])


print()
entrenador = input('Ingrese nombre del entrenador X: ')
pos = lista_entrenadores.busqueda(entrenador,'nombre')
if(pos):
    pokemon = input('Ingrese nombre del pokemon Y: ')
    pos1 = pos.sublista.busqueda(pokemon,'nombre')
    if(pos1):
        print('El entrenador', pos.info.nombre, 'tiene al pokemon',pos1.info.nombre)
        print(pos.info)
        print(pos1.info)
    else:
        print('El entrenador ',pos.info.nombre, 'no tiene al pokemon ingresado')
else:
    print('El entrenador no existe')