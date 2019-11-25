import requests
import json
import random
from random import randint
from imgurpython import ImgurClient


with open("resources/IMGURTOKEN.txt", "r") as token: #imgur токен
    readtoken = token.readlines()
    client_id = readtoken[0] # почему-то выдает "тут токен"\n
    client_id = client_id.replace('\n', '') # без этой комманды ничего не работает
    client_secret = readtoken[2]

imgur = ImgurClient(client_id, client_secret)


def getCat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    jsonResponse = response.text
    py = json.loads(jsonResponse)
    pyDictionary = py[0]
    CatUrl = pyDictionary.get('url')
    return CatUrl

def init_myCatImages():
    global readline
    with open('resources/links.txt', "r") as link:
        readline = link.readlines()
        album = imgur.get_album_images("0m0etMm")
        with open('resources/links.txt', "w") as link:
        #пришлось открывать файл снова, потому что иначе работает как говно!
            for images in album:
                link.write(images.link + '\n')
    return '{} - number of cats!'.format(len(readline))

def lenMyCatImages():
    return '{} - котов в альбоме'.format(len(readline))

def getMyCatImages():
    randomNumber = randint(0, len(readline))
    return readline[randomNumber]
