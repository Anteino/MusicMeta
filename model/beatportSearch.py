import requests
import json

from utils.constants import *

def beatportSearch(query):
    formattedQuery = query.replace(" ", "+")
    response = requests.get(BEATPORT_API_URL + formattedQuery)

    # print(response.text)
    
    resp = json.loads(response.text)

    for track in resp["tracks"]:
        trackName = track["name"] + " " + track["mix_name"] + " - "

        addComma = 0
        for artist in track["artists"]:
            trackName += ("" if addComma == 0 else ", ") + artist["name"]
            addComma = 1
        
        print(trackName)
        