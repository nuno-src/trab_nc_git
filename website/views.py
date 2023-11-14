from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from . import db
#from . import socketio
import json
import random
from string import ascii_uppercase


views = Blueprint('views', __name__)


ss = 0

def ler():
    with open('./public/sessions.txt', 'r') as f:
        l = f.read()
        #print(l)
        global ss
        if l == "logged":
            ss += 1
            print("ss:", ss)

rooms = {}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    
    session.clear()

    ler()

    

    return render_template("home.html", user=current_user)


@views.route("/room")
@login_required
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))

    return render_template("room.html", code=room, messages=rooms[room]["messages"])











data = {
    "status_code": ss
}

@views.route("/check")
def check():
    ler()
    print("ss no check:", ss)
    print("x", data["status_code"])
    if ss != 0:
        
        return jsonify(data), 200
    else:
        return jsonify(data), 403










