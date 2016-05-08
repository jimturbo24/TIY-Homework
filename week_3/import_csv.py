import csv
import psycopg2
import datetime

# Read data from CSV file, store it in wavedata list
wavedata = []
with open('wavedata.csv') as csvfile:
    wavereader = csv.reader(csvfile)
    header = next(wavereader)
    for row in wavereader:
        wavedata.append(row[1:])


# Connect to test database
conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
cur = conn.cursor()

for row in wavedata:
    cur.execute("""
INSERT INTO wave_data
            (height_meters,
             period,
             speed,
             temp_c,
             capture_date)
      VALUES (%s, %s, %s, %s, %s)""", row)

conn.commit()
cur.close()
conn.close()
