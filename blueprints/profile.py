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

bprofile = Blueprint("bprofile", __name__, template_folder="templates")

@bprofile.route("/")
def profile():
    response = api("/accounts/full/"+session["id"])
    return render_template("/profile/profile.html", country=response["country"], valute=response["valute"], VK=VK)

@bprofile.route("/login/")
def login():
    if SERVER_VERSION == "test":
        session["id"] = "541161804"
        session["name"] = "Матвей"
        session["photo"] = "https://sun1-24.userapi.com/s/v1/ig2/SeqKQxOgjduh-nN0oMPoZf5rchkOyWamZbJsvHaSXaj5d5BelnSgYDknXNfov1BTcU7VqVb4WJNnngVjVmptJgl2.jpg?size=200x200&quality=95&crop=514,6,508,508&ava=1"
        session["screen_name"] = "nousad"
        session["moderation"] = False
        session["banned"] = False
        session["admin"] = True
        return redirect("/profile/")

    if hashlib.md5((VK+request.args.get("uid")+VK_SECRET).encode()).hexdigest() == request.args.get("hash"):
        session["id"] = request.args.get("uid")
        response = api("/accounts/account/"+session["id"])

        session["name"] = response["name"]
        session["screen_name"] = response["screen_name"]
        session["photo"] = response["photo"]
        session["moderation"] = response["moderation"]
        session["banned"] = response["banned"]
        session["admin"] = response["admin"]
        

        return redirect("/profile/")
    else:
        abort(406)
@bprofile.route("/logout/")
def logout():
    session.clear()
    return redirect("/profile/")

@bprofile.route("/country/")
def country():
    response = api("/accounts/full/"+session["id"])
    return render_template("/profile/edit-country.html", ruler=response["account"], country=response["country"])


@bprofile.route("/country/send/", methods=["GET", "POST"])
def country_send():
    args = {}
    
    args["id"] = session["id"]
    args["cid"] = request.form["cid"]
    args["name"] = request.form["name"]
    args["flag"] = request.form["flag"].replace("&", "&amp;")
    args["group"] = request.form["group"]
    args["goverment_type"] = request.form["goverment_type"]
    args["goverment_form"] = request.form["goverment_form"]
    args["ideology"] = request.form["ideology"]
    args["political_type"] = request.form["political_type"]
    args["desc"] = request.form["desc"]
    args["date"] = request.form["date"]

    args["key"] = KEY
    args["hash"] = hashlib.md5(str(str(args["id"])+str(args["cid"])+str(KEY)+str(VK_SECRET)).encode()).hexdigest()

    response = api("/edit/countries/", args)
    return render_template("specific/error.html", message=response)

@bprofile.route("/checklink/")
def checklink():
    response = str(requests.get(request.args.get("link")).status_code)
    return flask.Response(response=response, status=200, mimetype="text/plain")