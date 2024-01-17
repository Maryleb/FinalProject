from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.index_model import get_master, get_master_record
@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()

    # нажата кнопка Найти
    if request.values.get('master'):
        master_id = int(request.values.get('master'))
        session['master_id'] = master_id
        date_start = request.values.get('date_start')
        date_end = request.values.get('date_end')

     # вошли первый раз
    else:
        session['master_id'] = 1
        date_start = '2023-11-01'
        date_end = '2023-12-01'
    df_master = get_master(conn)
    df_master_record = get_master_record(conn, session['master_id'], date_start, date_end)


     # выводим форму
    html = render_template(
     'index.html',
     master_id = session['master_id'],
     combo_box = df_master,
     master_record = df_master_record,
     len = len
    )
    return html