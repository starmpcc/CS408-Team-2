#-*- coding:utf-8 -*-
from flask import Flask, flash, request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os, sys, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateTimeField, SubmitField, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import Required, DataRequired, Regexp, EqualTo, Length


DEBUG = True

'''
Forms for Web Page
'''
class NewNovelForm(FlaskForm):
    submit = SubmitField(u'새로운 소설 작성하기')


class LoadSavedInputForm(FlaskForm):
    username = StringField(u'ID', validators=[DataRequired()])
    password = StringField(u'Password', validators=[DataRequired()])
    submit = SubmitField(u'불러오기')


class GetUserTextForm(FlaskForm):
    user_enter = StringField("", validators=[DataRequired()])
    submit = SubmitField(u'실행')


class CurrentNovelDisplay(FlaskForm):
    user_enter = StringField("")
    model_answer = TextAreaField("", render_kw={"rows": 3})


