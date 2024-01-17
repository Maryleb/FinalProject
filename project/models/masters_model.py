import pandas
def get_master(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM master
 ''', conn)

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
  ORDER BY phone_number
 ''', conn)

def get_master_record_free(conn, master_id):
 # свободные записи на стрижку
 return pandas.read_sql('''
  SELECT record_date AS Дата, record_time AS Время
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  LEFT OUTER JOIN pet USING (pet_id)
  WHERE master.master_id = :id AND pet_id IS NULL AND record_date >= '2023-11-01'
  ORDER BY record_date, record_time;
 ''', conn, params={"id": master_id})

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def add_record(conn, client_id, date_time, pet_name, master):
 print('hueta')
 added = f'''
   UPDATE record SET pet_id = (
   SELECT pet_id
   FROM pet INNER JOIN client USING(client_id)
   WHERE client_id == {client_id} and pet_name == '{pet_name}'
  )
  WHERE record_time == strftime('%H:%M:%S', '{date_time}') AND timetable_date_id == (
   SELECT timetable_date_id 
   FROM timetable INNER JOIN timetable_date USING (timetable_id)
   INNER JOIN record USING (timetable_date_id)
   WHERE record_date == strftime('%Y-%m-%d', '{date_time}') AND record_time == strftime('%H:%M:%S', '{date_time}') AND master_id == {master}
   LIMIT 1)
 '''
 execute_query(conn, added)