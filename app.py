import os

from flask import Flask, redirect, render_template, request
from flask_session import Session
from db import conn, cursor

app = Flask(__name__)

app.config['SECRET KEY'] = 'secretkey'

@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/playerbase")
def playerbase():
    if request.method == "GET":
        return render_template("playerbase.html")
    
@app.route("/matchreports")
def matchreports():
    if request.method == "GET":
        return render_template("/matchreports.html")
    
@app.route("/injuryreports")
def injuryreports():
    if request.method == "GET":
        return render_template("/injuryreports.html")

@app.route("/contracts")
def contracts():
    if request.method == "GET":
        return render_template("/contracts.html")
    
@app.route("/adddata", methods=["GET", "POST"])
def adddata():
    if request.method == "GET":
        return render_template("/adddata.html")
    if request.method =="POST":
        name = request.form.get("playername")
        age = request.form.get("playerage")
        position = request.form.get("position")
        tries = request.form.get("tries")
        caps = request.form.get("caps")
        injurystatus = request.form.get("injurystatus")

        player_info = [name, age, position, tries, caps, injurystatus]

        cursor.execute("INSERT INTO playerbase (name, age, position, caps, tries, injury_status) VALUES (%s,%s,%s,%s,%s,%s);", 
                       player_info
                    )
        return render_template("/adddata.html")

    

