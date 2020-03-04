#!/usr/bin/bash

ps -ef|grep flask|awk '{print $2}'|xargs kill -9

rm -rf venv

# virtualenv -p python3 venv
virtualenv -p ~/anaconda3/bin/python venv

source $PWD/venv/bin/activate

pip install -Ur requirement.txt

export FLASK_ENV=development

export FLASK_APP=hello.py
# export FLASK_APP=test-wx.py

# flask run --host=0.0.0.0 --port=8000

flask run --port=5050


