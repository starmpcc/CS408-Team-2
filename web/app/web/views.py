#-*- coding:utf-8 -*-
from io import StringIO
import pandas as pd
import numpy as np
import os, sys, datetime
from flask import Flask, flash, request, render_template, session, redirect, url_for, current_app, Response
from . import web
from .forms import NewNovelForm, LoadSavedInputForm, GetUserTextForm, CurrentNovelDisplay
import requests, json

DEBUG = True
pd.options.display.float_format = lambda x: '{:,.0f}'.format(x) if x > 1e3 else '{:,.2f}'.format(x)


def build_current_context(a, b):
    current_form = CurrentNovelDisplay()
    current_form.user_enter.data = a
    current_form.model_answer.data = b
    return current_form


@web.route('/')
def root():
    return redirect(url_for('.home'))


@web.route('/home', methods=['GET', 'POST'])
def home():
    if "username" not in session or session["username"] is None:
        form2 = LoadSavedInputForm()
    else:
        form2 = LoadSavedInputForm(username=session["username"], password=["password"])

    form1 = NewNovelForm()
    if form1.validate_on_submit():
        session["history"] = []
        return redirect(url_for(".interactive_novel",
                                novel_number=1,
                                current_context=build_current_context("", ""),
                                next_from=GetUserTextForm()))

    elif form2.validate_on_submit():
        session["username"] = form2.username.data
        session["password"] = form2.password.data
        return redirect(url_for(".load_saved_novels"))

    return render_template('home.html', new_start=form1, load_saved=form2)


@web.route('/not_ready', methods=['GET', 'POST'])
def not_ready():
    return render_template('not_ready.html')


@web.route('/interactive_novel', methods=['GET', 'POST'])
def interactive_novel():
    if "my_choice" not in session or session["my_choice"] is None:
        next_form = GetUserTextForm()
    else:
        next_form = GetUserTextForm(user_enter=session["my_choice"])

    if next_form.validate_on_submit():
        user_enter = next_form.user_enter.data
        context = ""
        data = {
            "inp" : "Hello.",
            "context" : ""
        }
        output = requests.get(url="http://0.0.0.0:5000/api/generate_next", json = data)
        print(output)
        output = output.json()
        print(output)
        model_answer = output["model_answer"]
        context = ["context"]

        session["history"].append((user_enter, model_answer))
        return render_template("interactive_novel.html",
                               novel_number=1,
                               current_context=build_current_context(user_enter, model_answer),
                               next_form=GetUserTextForm())

    if len(session["history"]) > 0:
        next_novel = session["history"][-1]
    else:
        next_novel = ("", "")

    return render_template("interactive_novel.html",
                           novel_number=1,
                           current_context=build_current_context(next_novel[0], next_novel[1]),
                           next_form=GetUserTextForm())

