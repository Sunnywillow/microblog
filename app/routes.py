from flask import render_template, flash, redirect, url_for

from flask import Flask,  render_template
from app import app
from app.form import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for use {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


