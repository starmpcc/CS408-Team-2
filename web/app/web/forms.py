#-*- coding:utf-8 -*-
from flask import Flask, flash, request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os, sys, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateTimeField, SubmitField, SelectField, TextAreaField
from wtforms.fields.simple import PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Required, DataRequired, Regexp, EqualTo, Length


DEBUG = True

'''
Forms for Web Page
'''
class NewNovelForm(FlaskForm):
    title = StringField(u"Title", validators=[DataRequired()])
    submit = SubmitField(u'새로운 소설 작성하기')


class LoginForm(FlaskForm):
    username = StringField(u'ID', validators=[DataRequired()])
    password = StringField(u'Password', validators=[DataRequired()])
    submit = SubmitField(u'로그인')

class GetUserTextForm(FlaskForm):
    user_enter = StringField("", validators=[DataRequired()])
    submit = SubmitField(u'실행')


class CurrentNovelDisplay(FlaskForm):
    user_enter = StringField("")
    model_answer = TextAreaField("", render_kw={"rows": 3})

class RegisterForm(FlaskForm):
    username = StringField(u'ID', validators=[DataRequired()])
    password = PasswordField(u'New Password', validators=[DataRequired(), EqualTo('confirm', message="Passwords must match")])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(u"회원가입")

class RegisterButton(FlaskForm):
    register = SubmitField(u"회원가입")

class SaveButton(FlaskForm):
    save = SubmitField(u"저장")

class NovelSelectForm(FlaskForm):
    title = SelectField(u'Novel Name', choices = [])
    load = SubmitField(u'불러오기')
