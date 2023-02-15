import sys
import aiohttp
import urllib.parse

sys.path.append('../MusicMeta')
from utils.constants import *

async def beatportSearch(query, index, setBeatportData):
    finalQuery = query
    finalQuery = finalQuery.replace("(", " ")
    finalQuery = finalQuery.replace(")", " ")
    finalQuery = urllib.parse.quote(finalQuery)

    async with aiohttp.ClientSession() as session:
        requestUrl = BEATPORT_API_URL + finalQuery
        async with session.get(requestUrl) as response:
            resp = await response.json()
            setBeatportData(index, resp)