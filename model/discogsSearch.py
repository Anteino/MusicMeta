from urllib.parse import quote
from requests import get
from decouple import Config, RepositoryEnv

from sys import path
path.append("../../MusicMeta")
from utils.resourcepath import resourcePath
from utils.constants import *

env=Config(RepositoryEnv(resourcePath(".env")))
key = env.get("DISCOGS_KEY")
secret = env.get("DISCOGS_SECRET")

def discogsSearch(data):
    try:
        requestUrl = "https://api.discogs.com/database/search?q={}&key={}&secret={}".format(quote(data), key, secret)
        resp = get(requestUrl).json()
        return constructDiscogsPage(resp)
    except Exception as e:
        return "An exception occuring during handling of discogs request: " + str(e)

def constructDiscogsPage(data):
    if("results" not in data):
        return NOT_FOUND_PAGE
    if (len(data["results"]) == 0):
        return NOT_FOUND_PAGE

    html = "<html><head><title>Page not found</title></head><body>"
    for result in data["results"]:
        html += '<a href="' + DISCOGS_BASE_URL + result["uri"] + '">' + result["title"]
        if("year" in result):
            html +=  ' (' + result["year"] + ')'
        html += '</a><br />'
    html += "</body></html>"

    return html