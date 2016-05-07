import psycopg2

wavedata = []

# Connect to test database
conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
cur = conn.cursor()

cur.execute("""
SELECT height_meters,
        period,
        speed,
        temp_c,
        capture_date
 FROM wave_data ORDER BY capture_date
""")

data = cur.fetchall()

for row in data:
    print("Height in meters: " + str(float(row[0])))

conn.commit()
cur.close()
conn.close()
