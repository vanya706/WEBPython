import json
import os
import sys
from datetime import datetime, date

from app.forms import ContactForm
from flask import render_template, request, redirect, url_for, flash, session

from app import app
from .forms import DataForm
from .function import write_json, validations

today = date.today()
menu = {'Main page': '/', 'Info about me': '/info', 'My achievement': '/achievement',
        'Contact': '/contact',  'Register Cabinet':'/register_cabinet'}
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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    cookie_name = session.get("name")
    cookie_email = session.get("email")
    print(cookie_email, cookie_name)
    if request.method == 'POST':
        if cookie_name is None and cookie_email is None:
            if form.validate_on_submit():
                name = form.name.data
                email = form.email.data
                body = form.body.data
                session['name'] = name
                session['email'] = email
                with open('data.txt', 'a') as outfile:
                    json.dump({'name': session.get("name"), 'email': session.get("email"), 'body': body}, outfile)
                    outfile.write('\n')
                flash(message='The message was send success!')
                return redirect(url_for('contact'))
            else:
                flash(message='Error while sending the message!')
        else:
            form.name.data = cookie_name
            form.email.data = cookie_email
            if form.validate_on_submit():
                body = form.body.data
                with open('data.txt', 'a') as outfile:
                    json.dump({'name': session.get("name"), 'email': session.get("email"), 'body': body}, outfile)
                    outfile.write('\n')
                flash(message='The message was send success!')
                return redirect(url_for('contact'))
            else:
                flash(message='Error while sending the message!')
    return render_template('contact_form.html', menu=menu, form=form, cookie_name=session.get("name"),
                           cookie_email=session.get("email"))


@app.route("/register_cabinet", methods=['GET', 'POST'])
def register_cabinet():
    form = DataForm()
    validations(form)
    if form.validate_on_submit():
        session['email'] = form.email.data
        write_json(form)
        flash('User has been written in json file')
        return redirect(url_for('register_cabinet'))

    try:
        ses = session['email']
    except:
        return render_template('start.html', menu=menu, form=form)

    with open('data.json') as f:
        data_files = json.load(f)

    return render_template('start.html', menu=menu, form=form, email=ses, number=data_files[ses]['number'],
                           year=data_files[ses]['year'],
                           pin=data_files[ses]['pin'], serial=data_files[ses]['serial'],
                           number_doc=data_files[ses]['number_doc'])
