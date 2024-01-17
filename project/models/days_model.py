import pandas
def get_master_available(conn, date_start):
 return pandas.read_sql(
 '''
    SELECT DISTINCT master_full_name, record_date, record_time
    FROM master INNER JOIN timetable USING (master_id)
    INNER JOIN timetable_date USING (timetable_id)
    INNER JOIN record USING (timetable_date_id)
    LEFT OUTER JOIN pet USING (pet_id)
    WHERE pet_id IS NULL AND record_date >= :date_s AND record_date < date(:date_s, "+8 days")
    ORDER BY master_full_name, record_date, record_time;
 ''', conn, params={"date_s": date_start})

def get_date_available(conn, date_start):
 return pandas.read_sql(
 '''
    SELECT DISTINCT record_date, 
    CASE
     WHEN strftime('%w',record_date) == '1' THEN "Понедельник"
     WHEN strftime('%w',record_date) == '2' THEN "Вторник"
     WHEN strftime('%w',record_date) == '3' THEN "Среда"
     WHEN strftime('%w',record_date) == '4' THEN "Четверг"
     WHEN strftime('%w',record_date) == '5' THEN "Пятница"
     WHEN strftime('%w',record_date) == '6' THEN "Суббота"
     WHEN strftime('%w',record_date) == '7' THEN "Воскресенье"
     ELSE "Не существует"
    END AS weekday
    FROM master INNER JOIN timetable USING (master_id)
    INNER JOIN timetable_date USING (timetable_id)
    INNER JOIN record USING (timetable_date_id)
    LEFT OUTER JOIN pet USING (pet_id)
    WHERE pet_id IS NULL AND record_date >= :date_s AND record_date < date(:date_s, "+8 days")
    ORDER BY record_date;
 ''', conn, params={"date_s": date_start})

def get_master_time(conn, date_start):
 return pandas.read_sql(
'''  SELECT master_full_name, record_date, record_time
  FROM master INNER JOIN timetable USING (master_id)
  INNER JOIN timetable_date USING (timetable_id)
  INNER JOIN record USING (timetable_date_id)
  LEFT OUTER JOIN pet USING (pet_id)
  WHERE pet_id IS NULL AND record_date >= :date_s AND record_date < date(:date_s, "+7 days")
  ORDER BY record_date;
  ''', conn, params={"date_s": date_start})