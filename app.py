import flask
from werkzeug.exceptions import HTTPException
from flask import Flask, redirect, make_response, abort, session, request
import requests
import os
import json
from markdownify import markdownify
from markdown import markdown
import random
import hashlib
from functions import *

from blueprints.countries import bcountries
from blueprints.valutes import bvalutes
from blueprints.profile import bprofile
from blueprints.settings import bsettings

app = Flask(__name__)
app.secret_key = SECRETKEY

app.register_blueprint(bcountries, url_prefix="/countries")
app.register_blueprint(bvalutes, url_prefix="/valutes")
app.register_blueprint(bprofile, url_prefix="/profile")
app.register_blueprint(bsettings, url_prefix="/settings")

@app.route("/")
def index():
    if round(random.random(), 3) != 0.356:
        response = make_response(redirect("/error/"))
        
        if random.randint(0, 1) == 1:
            response.set_cookie("theme", "coffee")
        else:
            response.set_cookie("theme", "tea")

        return response
    else:
        return redirect("/countries")

@app.route("/error/")
def error():
    abort(418)

@app.route("/map/")
def map():
    return render_template("/map/map.html")

@app.route("/markdown/")
def markdown():
    return render_template("/markdown/markdown.html")


@app.before_request
def before():
    if not "id" in session:
        session["id"] = "000000000"
        session["name"] = "Профиль"
        session["photo"] = "/static/images/defaults/profile.png"
        session["screen_name"] = ""
        session["moderation"] = False
        session["banned"] = False
        session["admin"] = False


@app.after_request
def after(response):
    if not "theme" in request.cookies:
        response.set_cookie("theme", "light")

    return response

@app.errorhandler(HTTPException)
def error(e):
    return render_template("/specific/error.html", error=str(e.code), description=HTTP_STATUS_CODES[e.code])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
