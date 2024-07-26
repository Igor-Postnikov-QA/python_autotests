import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f42687a42489d175585024d160f3a1a3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "xxxxxxxxxxx@yandex.ru",
    "password":"xxxxxxxx"
}
body_create = {
   "name": "generate",
    "photo_id": -1
}
body_new_name = {
    "pokemon_id": "45206",
    "name": "New Name",
    "photo_id": 166
}
body_add_pokeball = {
    "pokemon_id": "45206"
}
body_del_pokeboll = {
    "pokemon_id": "45206"
}

'''respons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(respons.text)'''

'''respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.text)'''

'''respons_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(respons_new_name.text)'''

'''respons_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(respons_add_pokeball.text)'''

respons_del_pokeboll = requests.put(url = f'{URL}/trainers/delete_pokeball', headers = HEADER, json = body_del_pokeboll)
print(respons_del_pokeboll.text)
