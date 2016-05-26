import sqlite3 as lite
import pandas as pd
import sys


con = lite.connect('getting_started.db') 
# month = raw_input('Enter a month: ')

with con:

    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS weather");
    cur.execute("DROP TABLE IF EXISTS cities");
    
    cur.execute("CREATE TABLE cities(name text, state text)");
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_temp integer)");
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 88)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 87)")

    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# join data in sqlite
with con:
    cur = con.cursor()
    
    NOT WORKING: 
    # cur.execute("SELECT weather.name, weather.year, weather.warm_month, weather.cold_month, weather.average_temp
    # FROM weather
    # INNER JOIN cities 
    # ON name = cities.city;")

with con:

  cur = con.cursor()    
  cur.execute("SELECT city FROM weather WHERE warm_month");
    

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)


