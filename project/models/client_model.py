import pandas
def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
  ORDER BY client_name
 ''', conn)

def get_client_record(conn, client_id):
 # записи на стрижку клиентов
 return pandas.read_sql('''
  SELECT record_date AS Дата, record_time AS Время, pet_name AS Кличка, pet_type AS Животное, brade AS Порода, weight AS Вес, mood AS Характер
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  INNER JOIN pet USING (pet_id)
  WHERE pet.client_id = :id
  ORDER BY record_date, record_time;
 ''', conn, params={"id": client_id})

def get_date_record(conn,  date_record):
 # поиск записей на определенную дату
 return pandas.read_sql('''
  SELECT record_date AS Дата, record_time AS Время, client_name AS Клиент, phone_number AS 'Номер телефона', pet_name AS Кличка, master_full_name AS 'Имя мастера'
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  INNER JOIN pet USING (pet_id)
  INNER JOIN client USING (client_id)
  WHERE record_date = :date
  ORDER BY record_time;
 ''', conn, params={"date": date_record})
