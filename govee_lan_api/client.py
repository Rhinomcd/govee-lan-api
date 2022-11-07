from .listener import start_listener, MULTICAST_GROUP_ADDRESS
from . import api_requests


class GoveeClient:
    devices = {}

    async def turn_on(self, device_id):
        if device_id not in self.devices:
            await self.scan_devices()
        message = api_requests.turn_on()
        command = {
            "message": message,
            "ip": self.devices[device_id]["ip"],
            "device": device_id,
        }
        await start_listener(command)

    async def turn_off(self, device_id):
        if device_id not in self.devices:
            await self.scan_devices()
        message = api_requests.turn_off()
        command = {
            "message": message,
            "ip": self.devices[device_id]["ip"],
            "device": device_id,
        }
        await start_listener(command)

    async def set_color_by_rgb(self, device_id, rgb):
        if device_id not in self.devices:
            await self.scan_devices()
        message = api_requests.color_by_rgb(rgb)
        command = {
            "message": message,
            "ip": self.devices[device_id]["ip"],
            "device": device_id,
        }
        await self.scan_devices()
        await start_listener(command)

    async def set_color_by_kelvin(self, device_id, kelvin):
        if device_id not in self.devices:
            await self.scan_devices()
        message = api_requests.color_by_kelvin(kelvin)
        command = {
            "message": message,
            "ip": self.devices[device_id]["ip"],
            "device": device_id,
        }
        await self.scan_devices()
        await start_listener(command)

    async def set_brightness(self, device_id, percent):
        if device_id not in self.devices:
            await self.scan_devices()
        message = api_requests.brightness(percent)
        command = {
            "message": message,
            "ip": self.devices[device_id]["ip"],
            "device": device_id,
        }
        await self.scan_devices()
        await start_listener(command)

    async def scan_devices(self):
        message = api_requests.scan_devices()
        command = {"message": message, "ip": MULTICAST_GROUP_ADDRESS}
        self.devices = await start_listener(command)
