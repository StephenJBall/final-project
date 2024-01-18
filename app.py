import os

from flask import Flask, redirect, render_template, request
from flask_session import Session
from db import conn, cursor

app = Flask(__name__)

app.config['SECRET KEY'] = 'secretkey'

@app.route("/")
def index():
    if request.method == "GET":
        cursor.execute("""SELECT name, date_of_birth, position, caps, tries, last_match, injury_status FROM playerbase""")
        players = cursor.fetchall()
        return render_template("playerbase.html", players=players)

@app.route("/playerbase")
def playerbase():
    if request.method == "GET":
        cursor.execute("""SELECT name, date_of_birth, position, caps, tries, last_match, injury_status FROM playerbase""")
        players = cursor.fetchall()
        return render_template("playerbase.html", players=players)
    
@app.route("/matchreports")
def matchreports():
    if request.method == "GET":
        cursor.execute("""SELECT opposition, venue, competition, stage, date FROM matchreports;""")
        matches = cursor.fetchall()
        return render_template("/matchreports.html", matches=matches)
    
@app.route("/injuryreports")
def injuryreports():
    if request.method == "GET":
        return render_template("/injuryreports.html")

@app.route("/contracts", methods=["GET", "POST"])
def contracts():
    if request.method == "GET":
        cursor.execute("""SELECT playerbase.name, contracts.duration, contracts.type, contracts.issuer
                       FROM contracts
                       INNER JOIN playerbase ON contracts.player_id = playerbase.id
                       ORDER BY contracts.duration;""")
        player_contract = cursor.fetchall()
        return render_template("contracts.html", player_contract=player_contract)
    if request.method == "POST":
        cursor.execute("""SELECT name FROM playerbase""")
        players = cursor.fetchall()
        name = request.form.get("name")
        cursor.execute("SELECT id FROM playerbase WHERE name = '%s';" % name)
        playerid = cursor.fetchall()
        playerid = playerid[0][0]
        duration = request.form.get("duration")
        type = request.form.get("type")
        issuer = request.form.get("issuer")
        cursor.execute("""INSERT INTO contracts 
                       (player_id, duration, type, issuer)
                       VALUES (%s,%s,%s,%s);
                       """,
                       (playerid, duration, type, issuer))
        conn.commit()
        return render_template("/contracts.html", players=players)
    
@app.route("/adddata", methods=["GET", "POST"])
def adddata():
    if request.method == "GET":
        cursor.execute("""SELECT name FROM playerbase""")
        players = cursor.fetchall()
        return render_template("/adddata.html", players=players)
    if request.method =="POST":
        name = request.form.get("playername")
        dob = request.form.get("playerdob")
        position = request.form.get("position")
        tries = request.form.get("tries")
        caps = request.form.get("caps")
        injurystatus = request.form.get("injurystatus")

        player_info = [name, dob, position, caps, tries, injurystatus]

        cursor.execute("""
                       INSERT INTO playerbase (name, date_of_birth, position, caps, tries, injury_status) 
                       VALUES (%s,%s,%s,%s,%s,%s);
                       """, 
                       (player_info))
        conn.commit()
        return render_template("/adddata.html")

@app.route("/editdata", methods=["GET", "POST"])
def editdata():
    if request.method == "POST":
        name = request.form.get("selectplayer")
        cursor.execute("SELECT * from playerbase where name = '%s';" % name)
        player = cursor.fetchall()
        name = player[0][1]
        dob = player[0][2]
        position = player[0][3]
        tries = player[0][4]
        caps = player[0][5]
        injurystatus = player[0][7]
        return render_template("/editdata.html", player=player, name=name, dob=dob, position=position, tries=tries, caps=caps, injurystatus=injurystatus)
    
@app.route("/datasubmitted", methods=["GET", "POST"])
def datasubmitted():
    if request.method == "POST":
        name = request.form.get("name")
        position = request.form.get("position")
        tries = request.form.get("tries")
        caps = request.form.get("caps")

        player_info = [position, tries, caps, name]
        cursor.execute("""
                       UPDATE playerbase 
                       SET position = %s, tries = %s, caps = %s 
                       WHERE name = %s;
                       """, 
                       (player_info))
        conn.commit()
        return render_template("/datasubmitted.html")

@app.route("/addmatch", methods=["GET", "POST"])
def addmatch():
    if request.method == "POST":
        opposition = request.form.get("opposition")
        venue = request.form.get("venue")
        competition = request.form.get("competition")
        stage = request.form.get("stage")
        date = request.form.get("date")
        cursor.execute("""INSERT INTO matchreports (opposition, venue, competition, stage, date)
                       VALUES (%s,%s,%s,%s,%s);""",
                       (opposition, venue, competition, stage, date))
        conn.commit()
        return render_template("/adddata.html")