1.
In [39]: r = requests.get('http://jsonplaceholder.typicode.com/posts')

In [40]: r.status_code
Out[40]: 200

In [41]: data = r.json()

In [42]: for num in range(0, len(data)):
    print(data[num]['id'], end=', ')
   ....:     
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,


2.
In [68]: commentResp = requests.get('http://jsonplaceholder.typicode.com/comments')

In [69]: commentResp.status_code
Out[69]: 200

In [70]: comments = commentResp.json()

In [78]: postID_12 = []

In [80]: for num in range(0, len(comments)):
    if comments[num]['postId'] == 12:
        postID_12.append(comments[num])

In [84]: for num in [0,1,2,3,4]:
    print(postID_12[num]['email'], end=', ')
   ....:     
Vince_Crist@heidi.biz, Darron.Nikolaus@eulah.me, Ezra_Abshire@lyda.us, Jameson@tony.info, Americo@estrella.net,


3.
# I used the same initial list of dictionaries ('comments' from #2) to extract this data

In [23]: posts_1230 = []

In [24]: for num in range(0, len(comments)-1):
    if comments[num]['postId'] in range(12, 31):
        posts_1230.append(comments[num])

In [25]: emaiList = []

In [26]: for num in range(0, len(posts_1230)):
   ....:     if posts_1230[num]['email'] not in emaiList:
   ....:         emaiList.append(posts_1230[num]['email'])
   ....:         

In [27]: len(emaiList)
Out[27]: 95

In [28]: print(emaiList)
[u'Vince_Crist@heidi.biz', u'Darron.Nikolaus@eulah.me', u'Ezra_Abshire@lyda.us', u'Jameson@tony.info', u'Americo@estrella.net', u'Aurelio.Pfeffer@griffin.ca', u'Vesta_Crooks@dora.us', u'Margarett_Klein@mike.biz', u'Freida@brandt.tv', u'Mollie@agustina.name', u'Janice@alda.io', u'Dashawn@garry.com', u'Devan.Nader@ettie.me', u'Joana.Schoen@leora.co.uk', u'Minerva.Anderson@devonte.ca', u'Lavinia@lafayette.me', u'Sabrina.Marks@savanah.name', u'Desmond_Graham@kailee.biz', u'Gussie_Kunde@sharon.biz', u'Richard@chelsie.co.uk', u'Gage_Turner@halle.name', u'Alfred@sadye.biz', u'Catharine@jordyn.com', u'Esther_Ratke@shayna.biz', u'Evangeline@chad.net', u'Newton.Kertzmann@anjali.io', u'Caleb_Herzog@rosamond.net', u'Sage_Mueller@candace.net', u'Bernie.Bergnaum@lue.com', u'Alexzander_Davis@eduardo.name', u'Jacquelyn@krista.info', u'Grover_Volkman@coty.tv', u'Jovanny@abigale.ca', u'Isac_Schmeler@barton.com', u'Sandy.Erdman@sabina.info', u'Alexandro@garry.io', u'Vickie_Schuster@harley.net', u'Roma_Doyle@alia.com', u'Tatum_Marks@jaylon.name', u'Juston.Ruecker@scot.tv', u'River.Grady@lavada.biz', u'Claudia@emilia.ca', u'Torrey@june.tv', u'Hildegard.Aufderhar@howard.com', u'Leone_Fay@orrin.com', u'Lura@rod.tv', u'Lottie.Zieme@ruben.us', u'Winona_Price@jevon.me', u'Gabriel@oceane.biz', u'Adolph.Ondricka@mozell.co.uk', u'Allen@richard.biz', u'Nicholaus@mikayla.ca', u'Kayla@susanna.org', u'Gideon@amina.name', u'Cassidy@maribel.io', u'Stefan.Crist@duane.ca', u'Aniyah.Ortiz@monte.me', u'Laverna@rico.biz', u'Derek@hildegard.net', u'Tyrell@abdullah.ca', u'Reyes@hailey.name', u'Danika.Dicki@mekhi.biz', u'Alessandra.Nitzsche@stephania.us', u'Matteo@marquis.net', u'Joshua.Spinka@toby.io', u'Annabelle@cole.com', u'Kacey@jamal.info', u'Mina@mallie.name', u'Hudson.Blick@ruben.biz', u'Domenic.Durgan@joaquin.name', u'Alexie@alayna.org', u'Haven_Barrows@brant.org', u'Marianne@maximo.us', u'Fanny@danial.com', u'Trevion_Kuphal@bernice.name', u'Emmet@guy.biz', u'Megane.Fritsch@claude.name', u'Amya@durward.ca', u'Jasen_Rempel@willis.org', u'Harmony@reggie.com', u'Rosanna_Kunze@guy.net', u'Ressie.Boehm@flossie.com', u'Domenic.Wuckert@jazmyne.us', u'Rhett.OKon@brian.info', u'Mathias@richmond.info', u'Ottis@lourdes.org', u'Estel@newton.ca', u'Bertha@erik.co.uk', u'Joesph@matteo.info', u'Alva@cassandre.net', u'Vivienne@willis.org', u'Angelita@aliza.me', u'Timmothy_Okuneva@alyce.tv', u'Moriah_Welch@richmond.org', u'Ramiro_Kuhn@harmon.biz']

4.
In [4]: userReq = requests.get('http://jsonplaceholder.typicode.com/users')

In [5]: userReq.status_code
Out[5]: 200

In [6]: users = userReq.json()

In [26]: for item in ['email', 'phone']:
    print(users[5][item], end=' ')
for item in ['lat', 'lng']:
    print(users[5]['address']['geo'][item], end=' ')
   ....:     
Karley_Dach@jasper.info 1-477-935-8478 x6430 -71.4197 71.7478
