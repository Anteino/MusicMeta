# import asyncio

# from presentation.mainviewcontroller import MainViewController

# mainViewController = MainViewController()
# mainViewController.show()

import asyncio
import aiohttp
import time
import requests

musicData = ["believe - cher", "dreadlock holiday - 10cc", "Better off alone - DJ Alice", "freestyler - bomfunk mcs", "fireball - pitbull", "spacer - sheila", "new shoes - paolo nutini", "one - metallica", "tribute - tenacious d", "galvanize - chemical brothers"]

# async def collectBeatportDataAsync():
#     async with aiohttp.ClientSession() as session:
#         for item in musicData:
#             print(item + ": start")
#             request_url = f'https://www.beatport.com/api/v4/catalog/search?q=' + item.replace(' ', '+')
#             async with session.get(request_url) as response:
#                 resp = await response.json()
#                 print(item + ": finish, result: " + resp["tracks"][0]["name"])

# def collectBeatportDataSync():
#     for item in musicData:
#         print(item + ": start")
#         request_url = f'https://www.beatport.com/api/v4/catalog/search?q=' + item.replace(' ', '+')
#         response = requests.get(request_url)
#         resp = response.json()
#         print(item + ": finish, result: " + resp["tracks"][0]["name"])

# start_time = time.time()
# asyncio.run(collectBeatportDataAsync())
# print(time.time() - start_time)

# start_time = time.time()
# collectBeatportDataSync()
# print(time.time() - start_time)



# async def collectPokemonDataAsync():
#     async with aiohttp.ClientSession() as session:
#         for i in range(1, 10):
#             print(str(i) + ": start")
#             pokemon_url = f'https://pokeapi.co/api/v2/pokemon/' + str(i)
#             async with session.get(pokemon_url) as response:
#                 resp = await response.json()
#                 print(str(i) + ": finish, result: " + resp["name"])

# def collectPokemonDataSync():
#     for i in range(1, 10):
#         print(str(i) + ": start")
#         pokemon_url = f'https://pokeapi.co/api/v2/pokemon/' + str(i)
#         response = requests.get(pokemon_url)
#         resp = response.json()
#         print(str(i) + ": finish, result: " + resp["name"])

# start_time = time.time()
# asyncio.run(collectPokemonDataAsync())
# print(time.time() - start_time)

# start_time = time.time()
# collectPokemonDataSync()
# print(time.time() - start_time)


async def async_func(item):
    async with aiohttp.ClientSession() as session:
        print(item + ": start")
        request_url = f'https://www.beatport.com/api/v4/catalog/search?q=' + item.replace(' ', '+')
        async with session.get(request_url) as response:
            resp = await response.json()
            print(item + ": finish, result: " + resp["tracks"][0]["name"])

async def main():
    tasks = []
    for item in musicData:
        tasks.append(loop.create_task (async_func(item)))

    await asyncio.wait(tasks)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except :
        pass