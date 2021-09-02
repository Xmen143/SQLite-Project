import sqlite3


conn = sqlite3.connect('Mulesoft SQL.db')

#craete a cursor
c = conn.cursor()

c.execute("SELECT * FROM Movies")

print(c.fetchall())

conn.commit

conn.close
