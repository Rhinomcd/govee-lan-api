import json


def turn_on():
    message = {"msg": {"cmd": "turn", "data": {"value": 1}}}
    return json.dumps(message)


def turn_off():
    message = {"msg": {"cmd": "turn", "data": {"value": 0}}}
    return json.dumps(message)


def color_by_rgb(rgb):
    message = {
        "msg": {
            "cmd": "colorwc",
            "data": {
                "color": {"r": rgb[0], "g": rgb[1], "b": rgb[2]},
                "colorTemInKelvin": 0,
            },
        }
    }
    return json.dumps(message)


def color_by_kelvin(kelvin):
    message = {
        "msg": {
            "cmd": "colorwc",
            "data": {"color": {"r": 0, "g": 0, "b": 0}, "colorTemInKelvin": kelvin},
        }
    }
    return json.dumps(message)


def brightness(percent):
    message = {"msg": {"cmd": "brightness", "data": {"value": percent}}}
    return json.dumps(message)


def scan_devices():
    message = {"msg": {"cmd": "scan", "data": {"account_topic": "reserve"}}}
    return json.dumps(message)
