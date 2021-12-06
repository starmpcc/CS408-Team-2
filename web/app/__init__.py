#-*- coding:utf-8 -*-
from flask import Flask, flash, request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import os, sys, datetime

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateTimeField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import Required, DataRequired, Regexp, EqualTo, Length

from config import config
# from .ai_functions import *

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    from . import datastore as ds
    from .web import web as web_blueprint

    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # create database if not exist 
    with app.test_request_context():
        from .models import UserModel, InteractiveNovelModel
        from .rest_api import generate_next

        db.create_all()
        print('database created at {}'.format(config[config_name].SQLALCHEMY_DATABASE_URI))

        api.add_resource(generate_next, "/api/generate_next")


    app.register_blueprint(web_blueprint)

    return app


