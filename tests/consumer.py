from client import GoveeClient
import asyncio
import logging

LIVING_ROOM_LIGHT = '18:66:C4:32:38:30:1E:32'

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (248, 207, 255)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    client = GoveeClient()
    await client.set_brightness(LIVING_ROOM_LIGHT, 100)
    await client.set_brightness(LIVING_ROOM_LIGHT, 50)
    await client.set_brightness(LIVING_ROOM_LIGHT, 1)
    await client.set_brightness(LIVING_ROOM_LIGHT, 100)

    # await client.turn_on(LIVING_ROOM_LIGHT)
    # await client.set_color_by_rgb(LIVING_ROOM_LIGHT, RED)
    # await client.set_color_by_rgb(LIVING_ROOM_LIGHT, GREEN)
    # await client.set_color_by_rgb(LIVING_ROOM_LIGHT, BLUE)
    # await client.set_color_by_rgb(LIVING_ROOM_LIGHT, PURPLE)


if __name__ == "__main__":
    asyncio.run(main())