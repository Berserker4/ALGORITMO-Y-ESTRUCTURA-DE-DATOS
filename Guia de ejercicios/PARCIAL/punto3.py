#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
#necesarias para resolver las actividades enumeradas a continuación:
#a) listado ordenado por nombre y por especie;
#b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
#c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#d) mostrar los Jedi de especie humana y twi'lek;
#e) listar todos los Jedi que comienzan con A;
#f) mostrar los Jedi que usaron sable de luz de más de un color;
#g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
#i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
from ClassQueue import Queue
from ClassStack import Stack
from lista import by_name_jedis, by_name_especies, search
jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Anakin Skywalker/Darth Vader",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi",
        "lightsaber_color": "Blue",
        "homeworld": "Tatooine",
        "birth_year": "41ABY",
        "height": 1.88,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Quinlan Vos",
        "rank": "Jedi Master",
        "species": "Human/Kiffar",
        "master": "Tholme",
        "lightsaber_color": "Green",
        "homeworld": "Kiffu",
        "birth_year": "59ABY",
        "height": 1.91,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Yoda",
        "rank": "Grand Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "896ABY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Mace Windu",
        "rank": "Jedi Master/Master of the Order",
        "species": "Human",
        "master": "Cyslin Myr",
        "lightsaber_color": "Purple",
        "homeworld": "Haruun Kal",
        "birth_year": "72ABY",
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ki-Adi-Mundi",
        "rank": "Jedi Master",
        "species": "Cerean",
        "master": None,
        "lightsaber_color": "Purple/Blue",
        "homeworld": "Cerea",
        "birth_year": "92ABY",
        "height": 1.98,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Plo Koon",
        "rank": "Jedi Master",
        "species": "Kel Dor",
        "master": None,
        "lightsaber_color": "Yellow/Blue/Orange",
        "homeworld": "Dorin",
        "birth_year": "71ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Saesee Tiin",
        "rank": "Jedi Master",
        "species": "Iktotchi",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Iktotch",
        "birth_year": None,
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yaddle",
        "rank": "Jedi Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "509AYB",
        "height": 0.61,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Even Piell",
        "rank": "Jedi Master",
        "species": "Lannik",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Lannik",
        "birth_year": None,
        "height": 1.22,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Oppo Rancisis",
        "rank": "Jedi Master",
        "species": "Thisspiasian",
        "master": "Yaddle",
        "lightsaber_color": "Green",
        "homeworld": "Thisspias",
        "birth_year": "206ABY",
        "height": 1.38,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Adi Gallia",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.84,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yarael Poof",
        "rank": "Jedi Master",
        "species": "Quermian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Quermia",
        "birth_year": None,
        "height": 2.64,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Eeth Koth",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Iridonia",
        "birth_year": None,
        "height": 1.71,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Depa Billaba",
        "rank": "Jedi Master",
        "species": "Chalactan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Chalacta",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kit Fisto",
        "rank": "Jedi Master",
        "species": "Nautolan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Glee Anselm",
        "birth_year": None,
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luminara Unduli",
        "rank": "Jedi Master",
        "species": "Mirialan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mirial",
        "birth_year": "58ABY",
        "height": 1.76,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Barriss Offee",
        "rank": "Padawan",
        "species": "Mirialan",
        "master": "Luminara Unduli",
        "lightsaber_color": "Blue",
        "homeworld": "Mirial",
        "birth_year": "40ABY",
        "height": 1.66,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Shaak Ti",
        "rank": "Jedi Master",
        "species": "Togruta",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Shili",
        "birth_year": None,
        "height": 1.87,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Coleman Trebor",
        "rank": "Jedi Master",
        "species": "Vurk",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Sembla",
        "birth_year": None,
        "height": 2.13,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jocasta Nu",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.69,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Aayla Secura",
        "rank": "Jedi Knight",
        "species": "Twi'lek",
        "master": "Quinlan Vos",
        "lightsaber_color": "Blue",
        "homeworld": "Ryloth",
        "birth_year": "47ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Sifo-Dyas",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mundos Cassandranos",
        "birth_year": "75ABY",
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Count Dooku",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Yoda",
        "lightsaber_color": "Blue/Red",
        "homeworld": "Serenno",
        "birth_year": "102ABY",
        "height": 1.93,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Pablo-Jill",
        "rank": "Jedi Knight",
        "species": None,
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cúmulo Estelar Skustell",
        "birth_year": None,
        "height": 1.60,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bultar Swan",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Plo Koon",
        "lightsaber_color": "Green",
        "homeworld": "Kuat",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Agen Kolar",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Stass Allie",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Tholoth",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ahsoka Tano",
        "rank": "Padawan",
        "species": "Togruta",
        "master": "Anakin Skywalker",
        "lightsaber_color": "Green/Yellow/Blue/White",
        "homeworld": "Shili",
        "birth_year": "36ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Asajj Ventress",
        "rank": "Padawan",
        "species": "Dathomirian",
        "master": "Ky Narec",
        "lightsaber_color": "Yellow/Red",
        "homeworld": "Dathomir",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Ima-Gun Di",
        "rank": "Jedi Master",
        "species": "Nikto",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Nahdar Vebb",
        "rank": "Jedi Knight",
        "species": "Mon Calamari",
        "master": "Kit Fisto",
        "lightsaber_color": "Blue",
        "homeworld": "Dac",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bolla Ropal",
        "rank": "Jedi Master",
        "species": "Rodian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Rodia",
        "birth_year": None,
        "height": 1.75,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ord Enisence",
        "rank": "Jedi Master",
        "species": "Skrilling",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Agrimundo-2079",
        "birth_year": None,
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tera Sinube",
        "rank": "Jedi Master",
        "species": "Cosian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cosia",
        "birth_year": "102ABY",
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ky Narec",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Pong Krell",
        "rank": "Jedi Master",
        "species": "Besalisk",
        "master": None,
        "lightsaber_color": "Blue/Green",
        "homeworld": "Ojom",
        "birth_year": None,
        "height": 2.36,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Coleman Kcaj",
        "rank": "Jedi Master",
        "species": "Ongree",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Skustell",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplar",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplee",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tu-Anh",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kanan Jarrus",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Depa Billaba",
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": "33ABY",
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ezra Bridger",
        "rank": "Padawan",
        "species": "Human",
        "master": "Kanan Jarrus",
        "lightsaber_color": "Blue",
        "homeworld": "Lothal",
        "birth_year": "19ABY",
        "height": 1.65,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Tatooine",
        "birth_year": "19ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Leia Organa",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Blue",
        "homeworld": "Alderaan",
        "birth_year": "19ABY",
        "height": 1.50,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ben Solo/Kylo Ren",
        "rank": "Padawan",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Chandrila",
        "birth_year": "5DBY",
        "height": 1.89,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Rey Skywalker",
        "rank": "Jedi Sentinel",
        "species": "Human",
        "master": "Luke Skywalker/Leia Organa",
        "lightsaber_color": "Blue/Green/Yellow",
        "homeworld": "Jakku",
        "birth_year": "15DYB",
        "height": 1.70,
        "to_darkside": None,
        "come_lightside": None
    }
 ]

#a)

Lista_ordenada = sorted(jedis, key=lambda jedi: (jedi["name"],))


def by_name(item):
    return (item["name"], item["species"])

ordenados= sorted(jedis, key=by_name)
jedis_cola= Queue()

for jedi in ordenados:
    jedis_cola.arrive(jedi)
    
print("Listado ordenado:")
while jedis_cola.size() > 0:
    jedi = jedis_cola.attention()
    print(f"nombre: {jedi["name"]}, especie: {jedi["species"]}")

#b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
Ahsoka = by_name_jedis(jedis, "Ahsoka Tano")
if Ahsoka:
    print("Informacion de Ahsoka Tano:")
    for key, value in Ahsoka.items():
        print(f"{key}: {value}")

print()
print()

kit = by_name_jedis(jedis, "Kit Fisto")
if kit:
    print("Informacion de Kit Fisto:")
    for key, value in kit.items():
        print(f"{key}: {value}")
        
        
#c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print()
for i in range (len(jedis)):
    if jedis[i]["master"] is not None:
        if "Luke Skywalker" in jedis[i]["master"] or "Yoda" in jedis[i]["master"]:
            print(f'Nombre: {jedis[i]["name"]}, Maestro: {jedis[i]["master"]}')
#d) mostrar los Jedi de especie humana y twi'lek;
print()
print()
tipo_human = by_name_especies(jedis, "Human")
tipo_twilek = by_name_especies(jedis, "Twi'lek")
print("Los Humanos Son:")
for jedi in tipo_human:
    print(f'Nombre: {jedi["name"]}, Especie: {jedi["species"]}')
print("Los TWILEK Son:")
for jedi in tipo_twilek:
    print(f'Nombre: {jedi["name"]}, Especie: {jedi["species"]}')
    
#e) listar todos los Jedi que comienzan con A;
print()
print()
print()

print("Jedi con la Letra A:")
for jedi in jedis:
    if jedi["name"].startswith("A"):
        print(f'Nombre: {jedi["name"]}')

#f) mostrar los Jedi que usaron sable de luz de más de un color;
print()
print()

sable_luz = []
for jedi in jedis:
    if jedi['lightsaber_color'] and '/' in jedi["lightsaber_color"]:
        sable_luz.append(jedi["name"])

print("Jedis que usaron el un sable con mas de un color:")
for nombre in sable_luz:
    print(f'Nombre: {nombre}')

#g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
sable_luz_color = []
for jedi in jedis:
    if jedi["lightsaber_color"] and "Yellow" in jedi["lightsaber_color"]:
        sable_luz_color.append(jedi["name"])
    if jedi["lightsaber_color"] and "Purple" in jedi["lightsaber_color"]:
        sable_luz_color.append(jedi["name"])
print("Jedis que utilizador sable de luz amarillo o violeta:")
for nombre in sable_luz_color:
    print(f'Nombre:{nombre}')
#h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
#i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
print("Jedi con el rango Grand Master:")
index = search(jedis, "rank", "Grand Master")
if index is not None:
    print(jedis[index]["name"])