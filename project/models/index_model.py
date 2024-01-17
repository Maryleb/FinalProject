import pandas
def get_master(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM master
 ''', conn)

def get_master_record(conn, master_id, date_start, date_end):
 # записи на стрижку
 return pandas.read_sql('''
  SELECT record_date AS Дата, record_time AS Время, pet_name AS Кличка, pet_type AS Животное, brade AS Порода, weight AS Вес, mood AS Характер
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  INNER JOIN pet USING (pet_id)
  WHERE master.master_id = :id AND record_date >= :date_s AND record_date < :date_e
  ORDER BY record_date, record_time;
 ''', conn, params={"id": master_id, "date_s": date_start, "date_e": date_end})

# для обработки данных о новом читателе
def get_new_reader(conn, new_reader):
 cur = conn.cursor()
 # добавить нового читателя в базу
 df = pandas.read_sql(
     '''
     INSERT INTO reader (reader_name) 
      VALUES (:new_reader);
     ''', conn, params={"new_reader": new_reader})
 return cur.lastrowid

# для обработки данных о взятой книге
def borrow_book(conn, book_id, reader_id):
 cur = conn.cursor()
 # добавить взятую книгу (book_id) читателю (reader_id) в таблицу book_reader
 # указать текущую дату как дату выдачи книги
 # уменьшить количество экземпляров взятой книги
 return True