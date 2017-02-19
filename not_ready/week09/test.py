import sqlite3


conn = sqlite3.connect('cinema.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Movies
    (id INT PRIMARY KEY,
     name TEXT,
     rating REAL);
    """)

text_imput = input("Insert id, name, rating:")
c.execute("""INSERT INTO Movies (id, name, rating)
             VALUES ?""", text_imput)
