#-*- coding:utf-8 -*-

import os, sys, datetime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from . import db

'''
UserModel

id          : 키값
username    : 사용자 이름
passowrd    : 비밀번호
'''

class UserModel(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<User {}: {}>'.format(self.id, self.username)

    def __init__(self, username, password):
        self.username = username
        self.password = password


'''
InteractiveNovelModel

id          : 키값
userid		: User
title       : Text
history     : Pickle
context     : Text
timestamp   : 저장 시각
'''

class InteractiveNovelModel(db.Model):
    __tablename__ = 'novel_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, ForeignKey("user_table.id"), nullable=False)
    title = db.Column(db.UnicodeText())
    history = db.Column(db.PickleType())
    context = db.Column(db.UnicodeText())
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<InteractiveNovel {}>'.format(self.userid)

    def __init__(self, user_id, title, history, context):
        self.timestamp = func.now()
        self.userid = user_id
        self.title = title
        self.history = history
        self.context = context

