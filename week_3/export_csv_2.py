import psycopg2

newPlayerList = []
feildList = ('Name', 'Age', 'Games played', 'Games started', 'Minutes played',
             'Shots made', 'Shots attempted', 'Shooting %', 'Three points made',
             'Three points attempted', 'Three point %', 'Two points made',
             'Two points attempted', 'Two point %', 'Shooting %',
             'Free throws made', 'Free throws attempted', 'Free throw %',
             'Offensive rebounds', 'Defensive rebounds', 'Total rebounds',
             'Assists', 'Steals', 'Blocked shots', 'Turn overs', 'Personal fouls',
             'Total points')

def retrieve_player(playerName):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM spurs_stats WHERE player_name=%s""", [playerName])
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    count = 1
    player_stats = data[0]

    for i in feildList:
        print('{}: {}'.format(i, player_stats[count]))
        count += 1

def insert_player(playerList):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
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
                  %s, %s, %s, %s, %s, %s, %s)""", playerList)
    conn.commit()
    cur.close()
    conn.close()


print('Welcome to the 2015-16 spurs stats sheet.')
while True:
    print('Press:\n(v) to view a players stats')
    print('(a) to add a players stats\n(r) to reset the player records')
    print('(e) to exit')
    userChoice = input('> ')
    if 'v' in userChoice.lower():
        inputName = input('Enter the name of a player to retrieve thier stats: ')
        retrieve_player(inputName)
    elif 'a' in userChoice.lower():
        print('Complete each entry below to add a player.')
        for i in feildList:
            newPlayerInput = input('{}: '.format(i))
            newPlayerList.append(newPlayerInput)
        insert_player(newPlayerList)
    elif 'e' in userChoice.lower():
        print('Thanks for stopping by!')
        break
