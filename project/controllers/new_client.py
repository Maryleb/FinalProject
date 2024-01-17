from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.new_client_model import add_client
@app.route('/new_client')
def new_client():
    conn = get_db_connection()

    # нажата кнопка Добавить
    if request.values.get('client_name') and request.values.get('client_phone'):
        add_client(conn, request.values.get('client_name'), request.values.get('client_phone'))
     # выводим форму
    html = render_template(
     'new_client.html',
     len = len
    )
    return html