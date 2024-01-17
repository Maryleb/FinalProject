import pandas

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def add_client(conn, client_name, client_phone):
 cursor = conn.cursor()
 cursor.execute(
 f'''
  INSERT INTO client (client_name, phone_number)
  VALUES ('{client_name}', '{client_phone}')
 ''')
 conn.commit()
 return cursor.lastrowid