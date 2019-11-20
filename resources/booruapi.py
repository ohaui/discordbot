from __future__ import unicode_literals
from pybooru import Danbooru
import discord

#TODO разобраться почему запрос score:1000 занимает так много времени
rd = open("resources/DANBOORUTOKEN.txt", "r") #никнейм и токен на данбоору
tokens = rd.readlines()
booru = client = Danbooru('danbooru', username=tokens[0], api_key=tokens[2])
def getLinkBoorus(tags):
        getpicture = booru.post_list(tags=tags, random=True, limit = 1)
        #tags - тэги для поиска, random = рандомная ли картинка, limit - лимит постов
        to_return = getpicture[0].get('file_url'), getpicture[0].get('score'),\
                  getpicture[0].get('tag_string_artist')
        print(to_return) # отображает ссылку, рейтинг и художника рандомного поста
        return to_return
