from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.record_model import get_master, get_free_record, get_free_record_all_masters, add_record, get_client
@app.route('/record')
def record():
    conn = get_db_connection()

    if request.values.get('master') and request.values.get('date_start') and request.values.get('date_end'):
        master = int(request.values.get('master'))
        date_start = request.values.get('date_start')
        date_end = request.values.get('date_end')
    else:
        master = -1
        date_start = '2023-11-01'
        date_end = '2023-11-02'

    if master == 0:
        df_free_record = get_free_record_all_masters(conn, date_start, date_end)
    else:
        df_free_record = get_free_record(conn, master, date_start, date_end)
    df_master = get_master(conn)
    df_client = get_client(conn)

    if request.values.get('data') and request.values.get('pet_name') and request.values.get('client'):
        data = request.values.get('data')
        record_date = data[:10]
        record_time = data[10:18]
        master_name = int(data[18:])
        client_id = int(request.values.get('client'))
        pet_name = request.values.get('pet_name')
        add_record(conn, client_id, record_date, record_time, pet_name, master_name)

     # выводим форму
    html = render_template(
     'record.html',
     combo_box = df_master,
     relation_free = df_free_record,
     combo_box1 = df_client,
     len = len,
        str = str
    )
    return html