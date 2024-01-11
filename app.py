import os

from flask import Flask, redirect, render_template, request
from flask_session import Session
import sqlite3

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
    

