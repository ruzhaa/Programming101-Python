import sqlite3


class CreateCinema:

    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')
        self.c = self.conn.cursor()

    def create_movies(self):
        movie = """ CREATE TABLE IF NOT EXISTS Movies
            (m_id INT PRIMARY KEY NOT NULL,
             name VARCHAR(255) NOT NULL,
             rating REAL NOT NULL);
            """
        self.c.execute(movie)

    def create_projections(self):
        projection = '''CREATE TABLE IF NOT EXISTS Projections
            (p_id INT PRIMARY KEY NOT NULL,
             movie_id INT NOT NULL,
             m_type VARCHAR(255) NOT NULL,
             m_date VARCHAR(255) NOT NULL,
             time VARCHAR(255) NOT NULL,
             FOREIGN KEY (movie_id) REFERENCES Movies (m_id));
            '''
        self.c.execute(projection)

    def create_reservations(self):
        reservation = '''CREATE TABLE IF NOT EXISTS Reservations
            (r_id INT PRIMARY KEY NOT NULL,
             username VARCHAR(255) NOT NULL,
             projection_id INT NOT NULL,
             row INT NOT NULL,
             col INT NOT NULL,
             FOREIGN KEY (projection_id) REFERENCES Projections (p_id));
            '''
        self.c.execute(reservation)

    def create_tables(self):
        self.create_movies()
        self.create_projections()
        self.create_reservations()

        self.conn.commit()
