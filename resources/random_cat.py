import requests
import pathlib
import json
import os
import random
import sys
from PIL import Image, ImageFilter

myCatPicDir = pathlib.Path("D:\\Projects\\new\\discordBot\\resources\\myCatPics") 
# путь к папке с котами

def getCat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    jsonResponse = response.text
    py = json.loads(jsonResponse)
    pyDictionary = py[0]
    CatUrl = pyDictionary.get('url')
    return CatUrl

def myGetCat():
    global randomCatPic
    PicDict = os.listdir(myCatPicDir)
    randomCatPic = (random.choice(PicDict))
    return randomCatPic

def myGetlen():
    PicDict = os.listdir(myCatPicDir)
    return len(PicDict)
