from __future__ import unicode_literals
from pybooru import Danbooru
from pybooru.exceptions import PybooruHTTPError
import discord

#TODO разобраться почему запрос score:1000 занимает так много времени

booru = client = Danbooru('danbooru', username='your_nickname', api_key='your_api')
def getLinkBoorus(tags):
        getpicture = booru.post_list(tags=tags, random=True, limit = 1)
        #tags - тэги для поиска, random = рандомная ли картинка, limit - лимит постов
        returns = getpicture[0].get('file_url'), getpicture[0].get('score'),\
                  getpicture[0].get('tag_string_artist')
        print(returns)
        return returns
