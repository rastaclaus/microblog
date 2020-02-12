from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'artems'}
    posts = [
        {'author': {'username': 'John'},
         'body': 'Beautiful day in Portland!'},
        {'author': {'username': 'Susan'},
         'body': 'The Avengers movie was so cool!'},
        {'author': {'username': 'Ипполит'},
         'body': 'Какая гадость эта ваша заливная рыба!!'}]
    context = {'user': user, 'posts': posts, 'title': 'Home'}
    return render_template('index.html', **context)