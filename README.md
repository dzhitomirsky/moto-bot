# onliner-moto-bot

## Purpose
Yes I do riding a motorcycle, do not tell me I'm crazy! When the time has come to change an iron horse,
I'm a little bit sick of monitoring vehicle-trading web-sites from my mobile.
So, I've implemented a bot using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) that aggregates motocycles of charecteristics that I'm interested in from [onliner.by](https://mb.onliner.by/)


## How to lounch?
* Go to (telegram bot father contact)[https://telegram.me/BotFather] and register a new bot - you will be given private token. Do not show your token to anyone!
* Ruild a docker image:
```bash
cd telegram-moto-bot
docker build -t my-moto-bot .
```
* Run it
```bash
docker run -e TELEGRAM_TOKEN=<your priovate token> my-moto-bot
```
* Thats all - add your bot with @<bot_name> to your contact list - and start picking new bikes!

## Contributing & lounching in dev mode
To develop a bot I used Python 2.7, pipenv, so launch it locally you have to do the next:
* install pipenv:
```
pip install pipenv
```

* Step into the repo filder and create virtual env:
```
cd telegram-moto-bot;
pipenv install;
```

* Export env variable with your token:
```
export TELEGRAM_TOKEN=<your private token>
```
* Start virtual env and run a bot:
```
pipenv shell;
python main.py
```

**Please, do not hesitate to change code on your taste or push me with some questions!**
