#!/usr/bin/env python
print("hello,world!")

from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello,World!你好，世界！"

@app.route('/index')
def index():
    return "Index Page"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='Dick Sven'))
    

# 利用`SimpleMDE`在线编写markdown
@app.route('/md', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        raw_md = request.form['post_content']
    return render_template('SimpleMDE.html')


if __name__ == '__main__':
    app.run(debug=True)
