#-*- coding:utf-8 -*-
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
import os, sys, datetime
import pandas as pd

from . import db
from .models import UserModel, InteractiveNovelModel


def user_add_ifnot(username, password):
    found_user = UserModel.query.filter_by(username=username).first()

    if found_user:
        return found_user.id
    else:
        t = UserModel(username=username, password=password)
        db.session.add(t)
        db.session.commit()
        return t.id


def save_novel(username, password, contents):
    userid = user_add_ifnot(username, password)

    # print("userid -> {}".format(userid))
    t = InteractiveNovelModel(user_id=userid, save_text=contents)
    db.session.add(t)
    db.session.commit()


def get_user_saved_nodels(username):
    found_user = UserModel.query.filter_by(username=username).first()

    if not found_user:
        return "{}"

    # InteractiveNovelModel.query.filter_by(userid=found_user.id).limit(3)
    result_ = db.engine.execute("select timestamp, contents from novel_table where userid={}".format(found_user.id))
    result_df = pd.DataFrame(result_.fetchall(), columns=['timestamp', 'contents'])
    result_df = result_df.sort_values(by="timestamp", ascending=False).head(3)
    return result_df.to_json(orient="records")

