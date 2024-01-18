from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.masters_model import get_master, get_client, get_master_record_free, add_record
@app.route('/masters')
def masters():
    conn = get_db_connection()

    # нажата кнопка Найти
    if request.values.get('master'):
        master_id = int(request.values.get('master'))
        session['master_id'] = master_id

        # нажата кнопка Записать
        if request.values.get('master') and request.values.get('date_time') and request.values.get('client') and request.values.get('pet_name') \
                and request.values.get('master_double'):
            session['master_id'] = int(request.values.get('master_double'))
            client_id = int(request.values.get('client'))
            date_time = request.values.get('date_time')
            pet_name = request.values.get('pet_name')
            master = int(request.values.get('master_double'))

            add_record(conn, client_id, date_time, pet_name, master)

    # вошли первый раз
    else:
        session['master_id'] = 1

    df_master = get_master(conn)
    df_client = get_client(conn)
    df_master_record = get_master_record_free(conn, session['master_id'])

     # выводим форму
    html = render_template(
     'masters.html',
     master_id = session['master_id'],
     master_id1 = request.values.get('master'),
     combo_box1 = df_master,
     combo_box2 = df_client,
     master_record = df_master_record,
     len = len
    )
    return html