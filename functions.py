import os

import time
import random
import requests

from settings import settings

def log(log):
     with open("log.txt", "a", encoding="UTF-8") as file:
          ap = f"|{time.strftime('%d/%m')}{str(log)}"
          file.write(ap)

def senha(pass_length):
    elements = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?~"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def tempo():
    return time.strftime("%H:%M:%S", time.localtime())

def mens(texto):
    return f"{settings['pre']}{str(texto)}"

def moeda():
        return random.choice(["Cara", "Coroa"])

def poke(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"#Olha que daora(pokemon = número ou nome do pokemon)
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        dados = resposta.json() #Converte a resposta em formato JSON para um mega dicionário com chaves e valores
        final = {
            "name": dados["name"],
            "id": dados["id"],
            "imagem": dados["sprites"]["front_default"],
            "height": dados["height"] * 10,
            "weight": dados["weight"] / 10,
            "type": dados["types"][0]["type"]["name"],
            "ability": dados["abilities"][0]["ability"]["name"]
        }
        return final
    
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")