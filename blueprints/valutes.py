import flask
from flask import Blueprint, redirect, make_response, abort, session, request
import requests
import os
import json
from markdownify import markdownify
from markdown import markdown
import random
import hashlib
from functions import *

bvalutes = Blueprint("bvalutes", __name__, template_folder="templates")

@bvalutes.route("/")
def valutes():
    if request.args.get("search") == None:
        response = api("/valutes/")
    else:
        response = api("/valutes/?search="+request.args.get("search"))

    if "error" in response: 
        abort(504)

    return render_template("/valutes/valutes.html", valutes=response)

@bvalutes.route("/valute/<id>/")
def valute(id):
    response = api("/valutes/valute/"+id)
    response_ruler = api("/accounts/account/"+id)

    if "error" in response or "error" in response_ruler: 
        abort(504)

    return render_template("/valutes/valute.html", valute=response, ruler=response_ruler)

@bvalutes.route("/preview/<id>/")
def preview(id):
    response = api("/valutes/preview/"+id)
    response_ruler = api("/accounts/account/"+id)

    if "error" in response or "error" in response_ruler: 
        abort(504)

    return render_template("/valutes/valute.html", valute=response, ruler=response_ruler,preview=True)

@bvalutes.route("/changes/<id>/")
def changes(id):
    abort(303)
    response = api("/valutes/change/"+id)

    if "error" in response: 
        abort(504)

    return render_template("/valutes/changes.html", changes=response)

@bvalutes.route("/changes/<fid>/<tid>/")
def change(fid, tid):
    abort(303)
    response = api("/valutes/change/"+fid+"/"+tid)

    if "error" in response: 
        abort(504)
        
    return render_template("/valutes/change.html", change=response)