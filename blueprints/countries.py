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

bcountries = Blueprint("bcountries", __name__, template_folder="templates")

@bcountries.route("/")
def countries():
    if request.args.get("search") == None:
        response = api("/countries/")
    else:
        response = api("/countries/?search="+request.args.get("search"))

    if "error" in response: 
        abort(504)
        
    return render_template("/countries/countries.html", countries=response)

@bcountries.route("/country/<id>/")
def country(id):
    response = api("/countries/country/"+id)
    response_ruler = api("/accounts/account/"+id)

    if "error" in response or "error" in response_ruler: 
        abort(504)

    return render_template("/countries/country.html", country=response, ruler=response_ruler)

@bcountries.route("/preview/<id>/")
def preview(id):
    response = api("/countries/preview/"+id)
    response_ruler = api("/accounts/account/"+id)

    if "error" in response or "error" in response_ruler: 
        abort(504)

    return render_template("/countries/country.html", country=response, ruler=response_ruler, preview=True)