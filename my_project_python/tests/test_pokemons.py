import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f42687a42489d175585024d160f3a1a3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4304'

def test_status_code():
    respons = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert respons.status_code == 200

def test_part_of_response():
    respons_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert respons_get.json()['data'][0]['trainer_name'] == 'LORD'
    