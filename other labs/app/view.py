import os
import sys
from datetime import datetime, date

from flask import current_app as app
from flask import render_template, request

today = date.today()
age = today.year - 2002 - ((today.month, today.day) < (3, 14))


@app.route('/')
def index():
    return render_template('index.html',
                           os_login=os.getlogin(),
                           user_agent=request.headers.get('User-Agent'),
                           version=sys.version,
                           time_now=datetime.now().strftime("%H:%M"))


@app.route("/info")
def info():
    return render_template('info.html', age=age, month=today.month, day=today.day)


@app.route("/achievement")
def achievement():
    return render_template('achievement.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
