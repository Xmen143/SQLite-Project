import sqlite3

#connect the database
conn = sqlite3.connect('Mulesoft SQL.db')

#craete a cursor
c = conn.cursor()

#craete a Query
c.execute("SELECT * FROM Movies")

c.execute("SELECT Name FROM Movies Where Actor = 'Salman Khan'")

print(c.fetchall())

#commit the db
conn.commit

#Close the db
conn.close
