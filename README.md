# yandex-lamp.py
Python fastapi app for control Smart Lamp from yandex IOT api

Clone this repository
```
git clone https://github.com/dimosikrus/yandex-lamp.py.git
cd yandex-lamp.git
```

Install requirements.
```
python3 -m pip install fastapi requests
```

Copy Config and edit.
```
cp config.sample.py config.py
nano config.py

DOMAIN - YOUR_CUSTOM_DOMAIN example-> led.example.com
TOKEN - Get this from https://oauth.yandex.ru/authorize?response_type=token&client_id=YOUR_YANDEX_CLIENT_ID
DEVICE_ID - Get this from api device info https://api.iot.yandex.net/v1.0/user/info [GET]

#help page yandex smart home:
  https://yandex.ru/dev/dialogs/smart-home/doc/concepts/platform-quickstart.html

# headers for requests
headers = {"Authorization": f"Bearer TOKEN",'Content-Type': 'application/json'}
```

Run Your app
```
uvicorn main:app --reload
# or with custom port
uvicorn main:app --reload --port 2566
```

# Using Nginx
using example config
```
ln -r -s nginx.conf /etc/nginx/sites-enabled/yandexlamp.conf
sudo nginx -s reload
```
