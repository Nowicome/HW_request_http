import requests
import json


def get_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes = requests.get(url)
    return heroes.json()


def most_intelligence(heroes):
    base = get_heroes()
    super_name, super_int = "", 0
    for i in base:
        if i["name"] not in heroes:
            continue
        if i["powerstats"]["intelligence"] > super_int:
            super_name = i["name"]
            super_int = i["powerstats"]["intelligence"]
    hero = f"Самый умный супер герой {super_name}, его интелект = {super_int}"
    return hero
