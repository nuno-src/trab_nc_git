from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for #, session
from flask_login import login_required, current_user
from . import db
#from . import socketio
import json
import random
from string import ascii_uppercase


views = Blueprint('views', __name__)



#rooms = {}

#def generate_unique_code(length):
#    while True:
#        code = ""
#        for _ in range(length):
#            code += random.choice(ascii_uppercase)
#        
#        if code not in rooms:
#            break
#    
#    return code

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    
    #session.clear()

    return render_template("home.html", user=current_user)


#@views.route("/room")
#@login_required
#def room():
#    room = session.get("room")
#    if room is None or session.get("name") is None or room not in rooms:
#        return redirect(url_for("home"))
#
#    return render_template("room.html", code=room, messages=rooms[room]["messages"])




















