import requests
import json
import sys

sys.path.append('../MusicMeta')

from utils.constants import *

async def beatportSearch(query):
    print("Searching")
    formattedQuery = query.replace(" ", "+")
    response = await requests.get(BEATPORT_API_URL + formattedQuery)
    
    # resp = json.loads(response.text)

    # print(resp["tracks"][0]["name"])

    # for track in resp["tracks"]:
    #     trackName = track["name"] + " " + track["mix_name"] + " - "

    #     addComma = 0
    #     for artist in track["artists"]:
    #         trackName += ("" if addComma == 0 else ", ") + artist["name"]
    #         addComma = 1
        