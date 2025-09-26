import sqlite3 
from flask import Flask , render_template,request,redirect

app = Flask(__name__)

DATABASE = 'students.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 