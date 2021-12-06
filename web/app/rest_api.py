#-*- coding: utf-8 -*-
#

from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json, os, sys, time
from . import datastore as ds
sys.path.append('/root/CS408-Team-2/model')
from model_helper import Model
import json
model =Model()

DEBUG = False

class generate_next(Resource):
    def get(self):

        params = request.get_json()
 
        inp = params["inp"]
        context = params["context"]
        outp, context = model.generate(inp, context)
        return {"status": "success",
                "model_answer": outp,
                "context": context}