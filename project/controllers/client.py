from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.client_model import get_date_record
@app.route('/client')
def client():
    conn = get_db_connection()

    # нажата кнопка Найти
    if request.values.get('date_record'):
        date_r = request.values.get('date_record')
        session['date_r'] = date_r
    else:
        session['date_r'] = '2023-11-01'
    df_date_record = get_date_record(conn, session['date_r'])

     # выводим форму
    html = render_template(
     'client.html',
     date_r = session['date_r'],
     date_record = df_date_record,
     len = len
    )
    return html