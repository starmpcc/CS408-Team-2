#-*- coding:utf-8 -*-
from io import StringIO
import pandas as pd
import numpy as np
import os, sys, datetime
from flask import Flask, flash, request, render_template, session, redirect, url_for, current_app, Response
from . import web
from .forms import NewNovelForm, LoginForm, GetUserTextForm, CurrentNovelDisplay, NovelSelectForm, RegisterButton, RegisterForm, SaveButton
import requests, json

from ..datastore import *

DEBUG = True
pd.options.display.float_format = lambda x: '{:,.0f}'.format(x) if x > 1e3 else '{:,.2f}'.format(x)


@web.route('/')
def root():
    return redirect(url_for('.home'))


@web.route('/home', methods=['GET', 'POST'])
def home():

    login = LoginForm()
    register = RegisterButton()

    if session.get('id'):
        redirect(url_for(".saved_novels"))

    if register.register.data == True:
        return redirect(url_for(".register", register =RegisterForm()))

    elif login.validate_on_submit() and login.submit.data == True:
        id = user_login(login.username.data, login.password.data)
        if id is not None:
            session["id"] = id
            return redirect(url_for(".saved_novels"))
        else:
            flash("Wrong Username or Password")

    return render_template('home.html', login=login, register = RegisterButton())


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    flash("REGISTER")
    if form.validate_on_submit():
        id = user_add(form.username.data, form.password.data)
        if id == None:
            flash("Existing Username. Please Try Others")
            return render_template('register.html', register = form)
        session["id"] = id
        return redirect(url_for(".saved_novels"))

    return render_template('register.html', register = form)


@web.route('/saved_novels', methods=['GET', 'POST'])
def saved_novels():
    if session.get('novel_id'): session.pop('novel_id')
    novel_list = get_user_saved_novels(session["id"])
    form = NovelSelectForm()
    newform = NewNovelForm()

    form.title.choices = novel_list


    if newform.submit.data and newform.validate_on_submit():
        session["history"] = []
        session["context"] = ""
        session["title"] = newform.title.data
        return redirect(url_for(".interactive_novel",
                                novel_title=session["title"],
                                dialogue = session["history"],
                                next_from=GetUserTextForm(),
                                save=SaveButton()))

    elif form.load.data:
        novel = load_novel(form.title.data)
        session["novel_id"] = novel.id
        session["title"] = novel.title
        session["history"] = novel.history

        return redirect(url_for('.interactive_novel', novel_title = novel.title, dialogue = novel.history, next_form = GetUserTextForm(), save = SaveButton()))

    return render_template('saved_novels.html', selectlist = form, newnovel = newform)

@web.route('/not_ready', methods=['GET', 'POST'])
def not_ready():
    return render_template('not_ready.html')


@web.route('/interactive_novel', methods=['GET', 'POST'])
def interactive_novel():
    if "my_choice" not in session or session["my_choice"] is None:
        next_form = GetUserTextForm()
    else:
        next_form = GetUserTextForm(user_enter=session["my_choice"])

    save_form = SaveButton()
    if save_form.save.data == True:
        novel_id = session.get('novel_id')
        session["novel_id"] = save_novel(session["id"], novel_id, session["title"], session["history"], session["context"])
        return render_template("interactive_novel.html",
                               novel_title=session["title"],
                               dialogue = session["history"],
                               next_form=GetUserTextForm(),
                               save = SaveButton())

    if next_form.validate_on_submit() and next_form.submit.data == True:
        user_enter = next_form.user_enter.data
        data = {
            "inp" : user_enter,
            "context" : session['context']
        }
        output = requests.get(url="http://0.0.0.0:5000/api/generate_next", json = data)
        output = output.json()
        model_answer = output["model_answer"]
        session["context"] = output["context"]
        session["history"].append((user_enter, model_answer))

        newform = GetUserTextForm()
        newform.user_enter.data = ""

        return render_template("interactive_novel.html",
                               novel_title=session["title"],
                               dialogue = session["history"],
                               next_form=newform,
                               save = SaveButton())


    return render_template("interactive_novel.html",
                           novel_title=session["title"],
                           dialogue = session["history"],
                           next_form=GetUserTextForm(),
                           save = SaveButton())

