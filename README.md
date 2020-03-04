# myflask

ref:[flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)

 The Minimal Flask APP

## To run the application

  use the *flask* command or *python -m flask*. Before you can do that you need to tell your terminal the application to work with by exporting the **FLASK_APP** environment variable:

  ``` 
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```

 Or,`bash run.sh`
 ```
#!/usr/bin/bash

ps -ef|grep flask|awk '{print $2}'|xargs kill -9

# virtualenv -p python3 venv
virtualenv -p ~/anaconda3/bin/python venv

source $PWD/venv/bin/activate

pip install -Ur requirement.txt

export FLASK_ENV=development

export FLASK_APP=hello.py

# flask run --host=0.0.0.0 --port=8000

flask run --port=5050

```
