from bottle import route, run, response, request
import json
import psycopg2

@route('/nba/teams/spurs/2015/player_stats')
def retrieve_all_stats():
    response.content_type = 'application/json; charset=UTF-8'
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM spurs_stats""")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    humanStats = []
    for row in data:
        count = 1
        statDict = {}
        for i in feildList:
            statDict[i] = '{}'.format(row[count])
            count += 1
        humanStats.append(statDict)

    return json.dumps(humanStats)

@route('/nba/teams/spurs/2015/')
def retrieve_player_stats():
    response.content_type = 'application/json; charset=UTF-8'
    playerName = request.query.name
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM spurs_stats WHERE player_name=%s""", [playerName])
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    count = 1
    humanStats = {}

    for i in feildList:
        humanStats[i] = '{}'.format(data[0][count])
        count += 1

    return json.dumps(humanStats)


feildList = ('Name', 'Age', 'Games played', 'Games started', 'Minutes played',
             'Shots made', 'Shots attempted', 'Shooting %', 'Three points made',
             'Three points attempted', 'Three point %', 'Two points made',
             'Two points attempted', 'Two point %', 'Shooting %',
             'Free throws made', 'Free throws attempted', 'Free throw %',
             'Offensive rebounds', 'Defensive rebounds', 'Total rebounds',
             'Assists', 'Steals', 'Blocked shots', 'Turn overs', 'Personal fouls',
             'Total points')

run(host='localhost', port=8080)

# Output for each function
# http://localhost:8080/nba/teams/spurs/2015/player_stats
# [{"Games played": "65", "Personal fouls": "65", "Offensive rebounds": "65",..., "Total rebounds": "27", "Shots attempted": "48"}]
#
# http://localhost:8080/nba/teams/spurs/2015/?name=Tim+Duncan
# {"Turn overs": "90", "Free throws made": "92", "Steals": "47", ..., "Age": "39"}
