import psycopg2

def delete_data(player):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()

    cur.execute("""DELETE FROM spurs_stats WHERE player_name=%s""", [player])

    conn.commit()
    cur.close()
    conn.close()


delete_data('Andre Miller')
