#-*- coding: utf-8 -*-
#

from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json, os, sys, time
from . import datastore as ds

DEBUG = False


class get_saved_novels(Resource):
    def get(self):
        inp = request.get_json()
        username = inp["username"] if "username" in inp.keys() else "unknown"
        password = inp["password"] if "password" in inp.keys() else "unknown"
        result = ds.get_user_saved_nodels(username)
        return {"status": "success", "result": result}


class generate_next(Resource):
    def get(self):
        inp = request.get_json()
        print("input body : ", inp)

        outp = "Computer Said: 집에 가서 자자."
        return {"status": "success",
                "model_answer": outp}


class save_novel(Resource):
    def get(self):
        return self.post()

    def post(self):
        inp = request.get_json()
        print("input body : ", inp)
        username = inp["username"] if "username" in inp.keys() else "unknown"
        password = inp["password"] if "password" in inp.keys() else "unknown"
        contents = inp["contents"] if "contents" in inp.keys() else "unknown"
        ds.save_novel(username, password, contents)
        return {"status": "saved"}


class delete_novel(Resource):
    def get(self):
        return {"status": "success"}

    def delete(self):
        return {"status": "success"}

