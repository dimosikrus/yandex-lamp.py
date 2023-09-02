# main.py

from fastapi import FastAPI
import requests as req
from config import *

app = FastAPI()

url = "https://api.iot.yandex.net/v1.0/devices/actions"
headers = {"Authorization": f"Bearer {TOKEN}",'Content-Type': 'application/json'}

@app.get("/")
async def root():
    js = {"color": f"https://{DOMAIN}/color/999","temperature": f"https://{DOMAIN}/temp/999","brightness": f"https://{DOMAIN}/light/999", "state": f"https://{DOMAIN}/state/999"}
    return js

@app.get("/color/{color:int}")
async def lamp_state(color):
    if color >= 0 and color <= 360:
        color_packet = {
            "devices": [{
                "id": DEVICE_ID,
                "actions": [{
                    "type": "devices.capabilities.color_setting",
                    "state": {
                        "instance": "hsv",
                        "value": {
                        "h": color,
                        "s": 100,
                        "v": 100
                        }
                    }
                }]
            }]
            }
        print(req.post(url=url, headers=headers, json=color_packet).content.decode())
        return {"color": color}
    else:
        return {"color": "input 0 - 360"}

@app.get("/temp/{temp:int}")
async def lamp_state(temp):
    if temp > 0 and temp <=100:
        temp2 = 2662 + (temp * 38)
        color_packet = {
            "devices": [{
                "id": DEVICE_ID,
                "actions": [{
                    "type": "devices.capabilities.color_setting",
                    "state": {
                        "instance": "temperature_k",
                        "value": temp2
                    }
                }]
            }]
            }
        print(req.post(url=url, headers=headers, json=color_packet).content.decode())
        return {"temperature": temp, "temperature_legacy": temp2}
    else:
        return {"temperature": "input 1 - 100"}

@app.get("/light/{brightness:int}")
async def lamp_state(brightness):
    if brightness > 1 and brightness <= 100:
        color_packet = {
            "devices": [{
                "id": DEVICE_ID,
                "actions": [{
                    "type": "devices.capabilities.range",
                    "state": {
                        "instance": "brightness",
                        "value": brightness
                    }
                }]
            }]
            }
        print(req.post(url=url, headers=headers, json=color_packet).content.decode())
        return {"brightness": brightness}
    else:
        return {"brightness": "input 1 - 100"}

@app.get("/state/{state:int}")
async def lamp_state(state):
    if state in (0, 1):
        if state == 0:
            state2 = False
        if state == 1:
            state2 = True
        color_packet = {
            "devices": [{
                "id": DEVICE_ID,
                "actions": [{
                    "type": "devices.capabilities.on_off",
                    "state": {
                        "instance": "on",
                        "value": state2
                    }
                }]
            }]
            }
        print(req.post(url=url, headers=headers, json=color_packet).content.decode())
        return {"state": state, "state_legacy": state2}
    else:
        return {"state": "input 0 - 1"}