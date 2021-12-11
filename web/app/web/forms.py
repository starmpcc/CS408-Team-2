#-*- coding:utf-8 -*-
from flask import Flask, flash, request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os, sys, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateTimeField, SubmitField, SelectField, TextAreaField
from wtforms.fields.simple import PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Required, DataRequired, Regexp, EqualTo, Length, StopValidation, ValidationError


DEBUG = True

'''
Forms for Web Page
'''
class NewNovelForm(FlaskForm):
    title = StringField(u"Title", validators=[DataRequired()])
    submit = SubmitField(u'새로운 소설 작성하기')


class LoginForm(FlaskForm):
    username = StringField(u'ID')
    password = StringField(u'Password')
    submit = SubmitField(u'로그인')

    def validate_username(form, field):
        if form.submit.data:
            DataRequired()(form, field)
    def validate_password(form, field):
        if form.submit.data:
            DataRequired()(form, field)

    register = SubmitField(u"회원가입")

class GetUserTextForm(FlaskForm):
    user_enter = StringField("")
    submit = SubmitField(u'실행')
    save = SubmitField(u'저장')

    def validate_user_enter(form, field):
        if form.submit.data:
            DataRequired()(form, field)

class RegisterForm(FlaskForm):
    username = StringField(u'ID', validators=[DataRequired()])
    password = PasswordField(u'New Password', validators=[DataRequired(), EqualTo('confirm', message="Passwords must match")])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(u"회원가입")

class NovelSelectForm(FlaskForm):
    title = SelectField(u'Novel Name', choices = [])
    load = SubmitField(u'불러오기')
