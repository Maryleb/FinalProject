from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.new_pet_model import add_pet, get_client
@app.route('/new_pet')
def new_pet():
    conn = get_db_connection()

    # нажата кнопка Добавить
    if request.values.get('client'):
        client_id =  int(request.values.get('client'))
        name = request.values.get('pet_name')
        type = request.values.get('pet_type')
        gender = request.values.get('pet_gender')
        brade = request.values.get('pet_brade')
        weight =request.values.get('pet_weight')
        mood = request.values.get('pet_mood')
        add_pet(conn, client_id, name, weight, mood, type, brade, gender)
     # выводим форму
    df_client = get_client(conn)

    html = render_template(
     'new_pet.html',
     combo_box = df_client,
     len = len
    )
    return html