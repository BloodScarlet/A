import aiohttp
import json

data = json.load(open("config.json"))["boobbot"]
auth = {"key": data["key"]}

async def neko():
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://nekos.life/api/v2/img/neko") as r:
            res = await r.json()
    return res["url"]

async def boobbot(name:str):
    async with aiohttp.ClientSession(headers=auth) as cs:
        async with cs.get(data["base"] + name) as r:
            res = await r.json()
    return res["url"]