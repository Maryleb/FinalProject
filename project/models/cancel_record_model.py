import pandas

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
 ''', conn)

def get_need_record(conn, client_id, date_record, time_record):
 return pandas.read_sql(
 '''
  SELECT record_date AS Дата, record_time AS Время, client_name AS 'Имя клиента'
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  LEFT OUTER JOIN pet USING (pet_id)
  INNER JOIN client USING (client_id)
  WHERE record_date == :date AND record_time == :time AND client_id == :id;
 ''', conn, params={"date": date_record, "time": time_record, "id":client_id})

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def cancel_record1(conn, client_id, date_record, time_record):
 cancel = f'''
  UPDATE record SET pet_id = NULL
  WHERE record_id == (
  SELECT record_id
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  INNER JOIN pet USING (pet_id)
  INNER JOIN client USING (client_id)
  WHERE client_id == {client_id} AND record_date == '{date_record}' AND record_time == '{time_record}'
  LIMIT 1
  )
 '''
 execute_query(conn, cancel)