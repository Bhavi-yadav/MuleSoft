import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('moviedatabase.db')

# create a cursor
cur = conn.cursor()

# create a table
cur.execute("""CREATE TABLE movies(
        movie_name text,
        actor_name text,
        actress_name text,
        release_year text,
        director_name text
    )""")

'''
cur.execute("INSERT INTO movies VALUES ('pirates of the caribbean sea', 'Johnny Depp', 'Keira Knightley', '2017', 'Joachim Rønning and Espen Sandberg')")
cur.execute("INSERT INTO movies VALUES ('alita battle angel', 'Keann Johnson', 'Rosa Salazar', '2019', 'Robert Rodriguez')")
cur.execute("INSERT INTO movies VALUES ('Bad Boys', 'Will Smith', 'Tea Lione', '2020', 'Bilall Fallah')")
cur.execute("INSERT INTO movies VALUES ('Horrer Story', 'Robert Eggers', 'Zoe', '2019', 'George Romero')")
cur.execute("INSERT INTO movies VALUES ('Hopes and show', 'Chris Morgan', 'rose russel', '2019', 'David leach')")
'''


# Update records into the table 
'''cur.execute("""UPDATE movies SET movie_name='Golden Plate'
    WHERE director_name="David leach"
    """) '''

# Delete record into the table 
'''cur.execute("DELETE from movies WHERE director_name='David leach'")'''

# Query The Database
cur.execute("SELECT * FROM movies")
items = cur.fetchall()
# print(items)
for item in items:
    print(item)

conn.commit()

conn.close()
