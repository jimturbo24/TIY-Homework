import csv
import psycopg2

spurs_data = []
with open("spurs_stats.csv") as csvfile:
    spurs_reader = csv.reader(csvfile)
    header = next(spurs_reader)
    for row in spurs_reader:
        spurs_data.append(row[1:])

conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
cur = conn.cursor()

for row in spurs_data:
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
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)

conn.commit()
cur.close()
conn.close()
