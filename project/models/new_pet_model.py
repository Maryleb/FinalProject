import pandas

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
  ORDER BY client_name
 ''', conn)

def add_pet(conn, client_id, name, weight, mood, type, brade, gender):
 cursor = conn.cursor()
 cursor.execute(
 f'''
  INSERT INTO pet (client_id, pet_name, weight, mood, pet_gender, pet_type, brade)
  VALUES ('{client_id}', '{name}', '{weight}', '{mood}', '{gender}', '{type}', '{brade}')
 ''')
 conn.commit()
 return cursor.lastrowid