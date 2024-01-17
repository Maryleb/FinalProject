from app import app
from flask import render_template, request, session
import sqlite3
from utils import get_db_connection
from models.cancel_record_model import get_client, get_need_record, cancel_record1
@app.route('/cancel_record')
def cancel_record():
    conn = get_db_connection()

    # нажата кнопка Отменить
    if request.values.get('client'):
        client_id = int(request.values.get('client'))
        session['client_id'] = client_id
        date_record = request.values.get('date_record')
        time_record = request.values.get('time_record')
        cancel_record1(conn, client_id, date_record, time_record)

     # вошли первый раз
    else:
        session['client_id'] = 1
        date_record = '2023-11-01'
        time_record = '-'
    df_client = get_client(conn)
    df_need_record = get_need_record(conn, session['client_id'], date_record, time_record)

     # выводим форму
    html = render_template(
     'cancel_record.html',
      client_id=session['client_id'],
      combo_box=df_client,
      need_record=df_need_record,
      len=len
    )
    return html