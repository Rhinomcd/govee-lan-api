# Govee LAN API Client 

[![PyPI version](https://badge.fury.io/py/govee-lan-api.svg)](https://badge.fury.io/py/govee-lan-api) 
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Rhinomcd_govee-lan-client&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Rhinomcd_govee-lan-client)

A simple API client for [Govee's LAN UDP API](https://app-h5.govee.com/user-manual/wlan-guide)

This was done in a weekend to help support a home assistant plugin for
controlling govee devices over their new(ish) LAN API


Here's some sample code that I'm using to test this -- formal API docs and tests coming soon. 

```py
from govee-lan-api.client import GoveeClient
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
    await client.turn_on(LIVING_ROOM_LIGHT)
    await client.set_brightness(LIVING_ROOM_LIGHT, 100)
    await client.set_color_by_rgb(LIVING_ROOM_LIGHT, GREEN)

    await client.set_brightness(LIVING_ROOM_LIGHT, 50)
    await client.set_brightness(LIVING_ROOM_LIGHT, 1)
    await client.set_brightness(LIVING_ROOM_LIGHT, 100)

    await client.turn_on(LIVING_ROOM_LIGHT)
    await client.set_color_by_rgb(LIVING_ROOM_LIGHT, RED)
    await client.set_color_by_rgb(LIVING_ROOM_LIGHT, GREEN)
    await client.set_color_by_rgb(LIVING_ROOM_LIGHT, BLUE)
    await client.set_color_by_rgb(LIVING_ROOM_LIGHT, PURPLE)


if __name__ == "__main__":
    asyncio.run(main())
```