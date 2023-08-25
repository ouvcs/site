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

bsettings = Blueprint("bsettings", __name__, template_folder="templates")

@bsettings.route("/theme/<theme>/")
def set_theme(theme):
    response = make_response(redirect("/profile/"))
    if theme == "tea-dark" and session["id"] == "541161804": theme = "tea-dark"
    elif theme == "coffee" or theme == "tea" or theme == "tea-dark": theme = "light"

    response.set_cookie("theme", theme)

    return response