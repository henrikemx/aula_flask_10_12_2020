import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for, abort, session, flash

# Coniguracoes ( variaveis globais )
DATABASE = './tmp/flaskr.db'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

# Annotation / Decorator
@app.before_request
def pre_request():
    g.bd = conectar_bd()

