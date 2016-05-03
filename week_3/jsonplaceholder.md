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
