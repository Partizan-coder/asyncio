import aiohttp
import asyncio
import asyncpg
import more_itertools


sw_url = 'https://swapi.dev/api'


async def get_hero(hero_id: int) -> dict:
    session = aiohttp.ClientSession()
    response = await session.get(f'{sw_url}/people/{hero_id}')
    response_json = await response.json()
    print(response_json)
    await session.close()

    id = hero_id
    films = ', '.join(response_json.get('films'))
    gender = response_json.get('gender')
    hair_color = response_json.get('hair_color')
    height = int(response_json.get('height'))
    homeworld = response_json.get('homeworld')
    mass = int(response_json.get('mass'))
    name = response_json.get('name')
    skin_color = response_json.get('skin_color')
    species = ', '.join(response_json.get('species'))
    starships = ', '.join(response_json.get('starships'))
    vehicles = ', '.join(response_json.get('vehicles'))
    conn = await asyncpg.connect('postgresql://asyncio:12345@127.0.0.1:5432/asyncio')

    await conn.execute('''
            INSERT INTO hero_model(id, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles) 
            VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
        ''', id, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles)
    await conn.close()
    return response_json


async def get_heroes(heroes_ids):
    tasks = [asyncio.create_task(get_hero(hero_id)) for hero_id in heroes_ids]
    for task in tasks:
        task_res = await task
        yield task_res


async def main():
    for hero_ids_chunk in more_itertools.chunked(range(1, 10), 10):
        async for hero in get_heroes (hero_ids_chunk):
            print('')


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(main())
