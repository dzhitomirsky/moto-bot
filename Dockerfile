FROM python:2.7

MAINTAINER dzhitomirsky@danielzhitomirsky@gmail.com

WORKDIR /usr/src/onliner-telegram-bot
COPY . .

RUN set -ex && pip install pipenv --upgrade
RUN set -ex && pipenv install --deploy --system

CMD [ "python", "./main.py" ]
