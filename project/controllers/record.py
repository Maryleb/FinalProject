from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.record_model import get_master_available, get_date_available, get_master_time
@app.route('/record')
def record():
    conn = get_db_connection()

    # нажата кнопка Показать
    if request.values.get('day_begin'):
        date_s = request.values.get('day_begin')
        session['date_s'] = date_s
    else:
        session['date_s'] = '2023-11-01'
    df_master_available = get_master_available(conn, session['date_s'])
    df_date_available = get_date_available(conn, session['date_s'])
    df_master_time = get_master_time(conn, session['date_s'])

     # выводим форму
    html = render_template(
     'record.html',
     date_s = session['date_s'],
     master_available=df_master_available,
     date_available=df_date_available,
     master_time = df_master_time,
     len = len
    )
    return html