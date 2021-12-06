#-*- coding:utf-8 -*-
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

import os, sys, datetime
import pandas as pd

from . import db
from .models import UserModel, InteractiveNovelModel


def user_add(username, password):

    found_user = UserModel.query.filter_by(username=username).first()

    if found_user:
        return None
    else:
        t = UserModel(username=username, password=password)
        db.session.add(t)
        db.session.commit()
        return t.id

def user_login(username, password):
    user = UserModel.query.filter_by(username = username).first()
    if user and user.password == password:
        return user.id
    return None

def save_novel(user_id, novel_id, title, history, context):
    if novel_id:
        novel = InteractiveNovelModel.query.get(novel_id) 
        novel.title = title
        novel.history = history
        novel.context = context
        novel.timestamp = func.now()
        db.session.commit()
        return novel.id
    else:
        novel = InteractiveNovelModel(user_id, title, history, context)
        db.session.add(novel)
        db.session.commit()
        return novel.id

def load_novel(novel_id):
    novel = InteractiveNovelModel.query.get(novel_id)
    return novel

def get_user_saved_novels(id):

    result = InteractiveNovelModel.query.filter_by(userid=id).all()
    novel_list = list(map(lambda x: (x.id, x.title), result))

    return novel_list

