from aiohttp import ClientSession
from urllib.parse import quote
from sys import path

path.append('../MusicMeta')
from utils.constants import *

async def beatportSearch(query, index, setBeatportData):
    finalQuery = query
    finalQuery = finalQuery.replace("(", " ")
    finalQuery = finalQuery.replace(")", " ")
    finalQuery = quote(finalQuery)

    async with ClientSession() as session:
        requestUrl = BEATPORT_API_URL + finalQuery
        async with session.get(requestUrl) as response:
            resp = await response.json()
            setBeatportData(index, resp)