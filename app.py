import sqlite3
import os

def get_user(id):
    return sqlite3.connect('db').execute(f'SELECT * FROM users WHERE id={id}')

def run_cmd(host):
    os.system(f'ping {host}')
