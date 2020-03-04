#!/usr/bin/bash

ps -ef|grep flask|awk '{print $2}'|xargs kill -9

source $PWD/venv/bin/activate

export FLASK_ENV=development

export FLASK_APP=hello.py

# flask run --host=0.0.0.0 --port=8000

flask run --port=5050


