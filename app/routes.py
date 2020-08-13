from flask import render_template

from flask import Flask,  render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}

    posts = [
        {'author': {'username': 'susan'},
         'body': 'post1'
         },
        {'author':  {'username': 'yang'},
         'body': 'post2'
         }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



