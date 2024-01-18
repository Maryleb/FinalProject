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
  ORDER BY client_name
 ''', conn)

def get_free_record_all_masters(conn, date_start, date_end):
 return pandas.read_sql(
 f'''
  SELECT master_full_name, master_id, record_date, record_time
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  LEFT OUTER JOIN record USING (timetable_date_id)
  LEFT OUTER JOIN pet USING (pet_id)
  WHERE record.pet_id IS NULL AND record_date >= '{date_start}' AND record_date <= '{date_end}'
 ''', conn)

def get_free_record(conn, master_id, date_start, date_end):
 return pandas.read_sql(
 f'''
  SELECT master_full_name, master_id, record_date, record_time
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  LEFT OUTER JOIN record USING (timetable_date_id)
  LEFT OUTER JOIN pet USING (pet_id)
  WHERE record.pet_id IS NULL AND record_date >= '{date_start}' AND record_date <= '{date_end}' AND master_id == {master_id}
 ''', conn)

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def add_record(conn, client_id, record_date, record_time, pet_name, master):
 added = f'''
   UPDATE record SET pet_id = (
   SELECT pet_id
   FROM pet INNER JOIN client USING(client_id)
   WHERE client_id == {client_id} and pet_name == '{pet_name}'
  )
  WHERE record_time == '{record_time}' AND timetable_date_id == (
   SELECT timetable_date_id 
   FROM master INNER JOIN timetable USING (master_id)
   INNER JOIN timetable_date USING (timetable_id)
   INNER JOIN record USING (timetable_date_id)
   WHERE record_date == '{record_date}' AND record_time == '{record_time}' AND master_full_name LIKE '%{master}%'
   LIMIT 1)
 '''
 execute_query(conn, added)