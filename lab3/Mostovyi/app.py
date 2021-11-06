from flask import Flask, render_template, request
from datetime import datetime, date
import sys
import os

app = Flask(__name__)
today = date.today()
menu = {'Main page': '/', 'Info about me': '/info', 'My achievement': '/achievement'}
age = today.year - 2002 - ((today.month, today.day) < (3, 14))


@app.route('/')
def index():
    return render_template('index.html',
                           menu=menu,
                           os_login=os.getlogin(),
                           user_agent=request.headers.get('User-Agent'),
                           version=sys.version,
                           time_now=datetime.now().strftime("%H:%M"))


@app.route('/info')
def info():
    return render_template('info.html', menu=menu, age=age, month=today.month, day=today.day)


@app.route('/achievement')
def achievement():
    return render_template('achievement.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
