import sqlite3


conn = sqlite3.connect('cinema_data.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()


create_table_movies = '''CREATE TABLE IF NOT EXISTS Movies
            (m_id INTEGER PRIMARY KEY NOT NULL,
             name VARCHAR(255) NOT NULL,
             rating REAL NOT NULL);'''

c.execute(create_table_movies)

create_table_projections = '''CREATE TABLE IF NOT EXISTS Projections
            (p_id INTEGER PRIMARY KEY NOT NULL,
             movie_id INTEGER NOT NULL,
             m_type VARCHAR(255) NOT NULL,
             m_date VARCHAR(255) NOT NULL,
             time VARCHAR(255) NOT NULL,
             FOREIGN KEY (movie_id) REFERENCES Movies (m_id));'''

c.execute(create_table_projections)

create_table_reservations = '''CREATE TABLE IF NOT EXISTS Reservations
            (r_id INTEGER PRIMARY KEY AUTOINCREMENT,
             username VARCHAR(255) NOT NULL,
             projection_id INTEGER NOT NULL,
             row INTEGER NOT NULL,
             col INTEGER NOT NULL,
             FOREIGN KEY (projection_id) REFERENCES Projections (p_id));'''

c.execute(create_table_reservations)
conn.commit()


insert_into_movies = '''INSERT INTO Movies (m_id, name, rating)
                  VALUES (1, "Her", 8.3),
                         (2, "The Hunger Games: Catching Fire", 7.9),
                         (3, "Wreck-It Raplsh", 7.8);'''

c.execute(insert_into_movies)
conn.commit()

insert_into_projections = '''INSERT INTO Projections (p_id, movie_id, m_type, m_date, time)
                  VALUES (1, 1, "3D", "2014-04-01", "19:10"),
                         (2, 1, "2D", "2014-04-01", "19:00"),
                         (3, 1, "4DX", "2014-04-02", "21:10"),
                         (4, 3, "2D", "2014-04-05", "20:20"),
                         (5, 2, "3D", "2014-04-02", "22:10"),
                         (6, 2, "2D", "2014-04-02", "19:30");'''

c.execute(insert_into_projections)
conn.commit()

insert_into_reservations = '''INSERT INTO Reservations (username, projection_id, row, col)
                  VALUES ("RadoRado", 1, 2, 1),
                         ("RadoRado", 1, 3, 5),
                         ("RadoRado", 1, 7, 8),
                         ("Ivo", 3, 1, 1),
                         ("Ivo", 3, 1, 2),
                         ("Slavyana", 5, 2, 3),
                         ("Slavyana", 5, 2, 4);'''

c.execute(insert_into_reservations)
conn.commit()
