import csv
import psycopg2

def delete_data():
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""DELETE FROM spurs_stats""")
    conn.commit()
    cur.close()
    conn.close()

def open_csv():
    rowData = []
    with open('spurs_stats.csv') as csvfile:
        fileReader = csv.reader(csvfile)
        header = next(fileReader)
        for row in fileReader:
            rowData.append(row[1:])
    return rowData

def insert_data(aList):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    for row in aList:
        cur.execute("""
    INSERT INTO spurs_stats
                (player_name,
                  age,
                  gm_tot,
                  gm_start,
                  min_plyd,
                  feild_gl_md,
                  feild_gl_att,
                  feild_gl_pct,
                  three_pt_md,
                  three_pt_att,
                  three_pt_pct,
                  two_pt_md,
                  two_pt_att,
                  two_pt_pct,
                  eff_fg_pct,
                  free_thw_md,
                  free_thw_att,
                  free_thw_pct,
                  off_rbnd,
                  def_rbnd,
                  rbnd_tot,
                  ast,
                  stl,
                  blk,
                  trn_ovr,
                  prsnl_fwl,
                  tot_pts)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s)""", row)
    conn.commit()
    cur.close()
    conn.close()

def open_and_insert():
    spursStats = open_csv()
    insert_data(spursStats)


# CREATE TABLE spurs_stats (id serial PRIMARY KEY, player_name varchar(30), age numeric(3,0), gm_tot numeric(3,0), gm_start numeric(3,0), min_plyd numeric(5,0), feild_gl_md numeric(5,0), feild_gl_att numeric(5,0), feild_gl_pct numeric(5,4), three_pt_md numeric(5,0), three_pt_att numeric(5,0), three_pt_pct numeric(5,4), two_pt_md numeric(5,0), two_pt_att numeric(5,0), two_pt_pct numeric(5,0), eff_fg_pct numeric(5,4), free_thw_md numeric(5,0), free_thw_att numeric(5,0), free_thw_pct numeric(5,4), off_rbnd numeric(5,0), def_rbnd numeric(5,0), rbnd_tot numeric(5,0), ast numeric(5,0), stl numeric(5,0), blk numeric(5,0), trn_ovr numeric(5,0), prsnl_fwl numeric(5,0), tot_pts numeric(5,0));
