import sqlite3
import copy
# from create_cinema import CreateCinema


CINEMA_MAP = [['  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
              [' 1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              [' 9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


class Cinema:

    def __init__(self):
        # self.cinema = CreateCinema()
        # self.conn = self.cinema.conn
        # self.c = self.cinema.c
        self.conn = sqlite3.connect('cinema.db')
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    def create_movies(self):
        table = """ CREATE TABLE IF NOT EXISTS Movies
            (m_id INT PRIMARY KEY NOT NULL,
             name VARCHAR(255) NOT NULL,
             rating REAL NOT NULL);
            """
        self.c.execute(table)
        self.conn.commit()

    def create_projections(self):
        table = '''CREATE TABLE IF NOT EXISTS Projections
            (p_id INT PRIMARY KEY NOT NULL,
             movie_id INT NOT NULL,
             m_type VARCHAR(255) NOT NULL,
             m_date VARCHAR(255) NOT NULL,
             time VARCHAR(255) NOT NULL,
             FOREIGN KEY (movie_id) REFERENCES Movies (m_id));
            '''
        self.c.execute(table)
        self.conn.commit()

    def create_reservations(self):
        table = '''CREATE TABLE IF NOT EXISTS Reservations
            (r_id INT PRIMARY KEY AUTOINCREMENT,
             username VARCHAR(255) NOT NULL,
             projection_id INT NOT NULL,
             row INT NOT NULL,
             col INT NOT NULL,
             FOREIGN KEY (projection_id) REFERENCES Projections (p_-id));
            '''
        self.c.execute(table)
        self.conn.commit()

    def create_tables(self):
        self.create_movies()
        self.create_projections()
        self.create_reservations()

        # self.conn.commit()

    def insert_into_movies(self):
        text = '''INSERT INTO Movies (m_id, name, rating)
                  VALUES (1, "Her", 8.3),
                         (2, "The Hunger Games: Catching Fire", 7.9),
                         (3, "Wreck-It Raplsh", 7.8);
        '''
        self.c.execute(text)

    def insert_into_projections(self):
        text = '''INSERT INTO Projections (p_id, movie_id, m_type, m_date, time)
                  VALUES (1, 1, "3D", "2014-04-01", "19:10"),
                         (2, 1, "2D", "2014-04-01", "19:00"),
                         (3, 1, "4DX", "2014-04-02", "21:10"),
                         (4, 3, "2D", "2014-04-05", "20:20"),
                         (5, 2, "3D", "2014-04-02", "22:10"),
                         (6, 2, "2D", "2014-04-02", "19:30");
        '''
        self.c.execute(text)

    def insert_into_reservations(self):
        text = '''INSERT INTO Reservations (username, projection_id, row, col)
                  VALUES ("RadoRado", 1, 2, 1),
                         ("RadoRado", 1, 3, 5),
                         ("RadoRado", 1, 7, 8),
                         ("Ivo", 3, 1, 1),
                         ("Ivo", 3, 1, 2),
                         ("Slavyana", 5, 2, 3),
                         ("Slavyana", 5, 2, 4);
        '''
        self.c.execute(text)

    def insert(self):
        self.insert_into_movies()
        self.insert_into_projections()
        self.insert_into_reservations()

        self.conn.commit()

    def get_projection(self, m_id):
        t = (m_id, )
        get = '''SELECT p.p_id
                 FROM Projections AS p
                 JOIN Movies AS m
                 ON m.m_id = p.movie_id
                 WHERE m.m_id=?
'''
        self.c.execute(get, t)
        self.conn.commit()

        list_with_id_projections = list()
        for row in self.c.fetchall():
            list_with_id_projections.append(row['p_id'])

        return list_with_id_projections

    @staticmethod
    def print_map():
        print_map = ""
        for row in CINEMA_MAP:
            for col in row:
                print_map += col + " "
            print_map += "\n"
        return print_map

    def get_position(self, seat):
        for char in seat:
            if char in " ,()":
                seat = seat.replace(char, '')
        row = int(seat[0])
        col = int(seat[1])

        return row, col

    def change_map(self, tuple_spots):
        current_map = CINEMA_MAP
        for group in tuple_spots:
            row = group[0]
            col = group[1]
            current_map[row][col] = 'X'
        return current_map

    def get_spots(self, m_id, p_id):
        t = (m_id, p_id)
        self.c.execute('''SELECT m.name, p.m_type, p.p_id, p.m_date, p.time, r.username, r.row, r.col
                          FROM Movies AS m
                          JOIN Projections AS p
                          ON m.m_id = p.movie_id
                          JOIN Reservations AS r
                          ON r.projection_id = p.p_id
                          WHERE m.m_id=? AND p.p_id=?;''', t)
        self.conn.commit()

        tuple_spots = ()
        for row in self.c.fetchall():
            tuple_spots += ((row['row'], row['col']), )
        return tuple_spots

    def count_spots(self, m_id, p_id):
        tuple_of_spots = self.get_spots(m_id, p_id)

        self.change_map(tuple_of_spots)
        return sum([x.count('.') for x in CINEMA_MAP])

    def show_movies(self):
        self.c.execute('''SELECT Movies.m_id, Movies.name, Movies.rating
                          FROM Movies
                          ORDER BY Movies.rating DESC;
            ''')
        self.conn.commit()
        result = "Current movies: \n"
        for row in self.c.fetchall():
            result += "[{}] - {} ({}) \n".\
                    format(row['m_id'], row['name'], row['rating'])
        return result

    def show_movie_projections(self, m_id, name_movie=None):
        t = (m_id, )
        text = '''SELECT p.p_id, p.m_type, p.m_date, p.time
                  FROM Projections AS p
                  JOIN Movies AS m
                  ON p.movie_id = m.m_id
                  WHERE m.m_id = ?
                  ORDER BY p.m_date;'''

        self.c.execute(text, t)
        self.conn.commit()
        count = 1
        result = "Projections for movie '{}': \n".format(name_movie)

        for row in self.c.fetchall():
            spots = self.count_spots(m_id, row['p_id'])
            result += "[{}] - {} {} ({}) - {} spots available\n".\
                     format(count, row['m_date'], row['time'], row['m_type'], spots)
            count += 1
        return result

    def show_movie_projections_with_date(self, name_movie, m_id, m_date):
        t = (m_id, m_date)
        text = '''SELECT p.m_type, p.time
                  FROM projections AS p
                  JOIN movies AS m
                  ON p.movie_id = m.m_id
                  WHERE m.m_id = ? AND p.m_date = ?
                  ORDER BY p.m_date;'''

        self.c.execute(text, t)
        self.conn.commit()

        count = 1
        result = "Projections for movie '{}' on date {}: \n".format(name_movie, m_date)
        for row in self.c.fetchall():
            result += "[{}] - {} ({})\n".\
                    format(count, row['time'], row['m_type'])
            count += 1
        return result

    def get_name_movie(self, m_id):
        t = (m_id, )
        self.c.execute('''SELECT Movies.name
                          FROM Movies
                          WHERE Movies.m_id = ?''', t)
        self.conn.commit()

        for row in self.c.fetchall():
            return row['name']

    def projection_choose(self, choose_projection):
        print("Available seats (marked with a dot):")
        return self.print_map()

    def check_seat(self, choose_movie, choose_user, choose_projection, seat):
        # list_projections = self.get_projection(choose_movie)
        tuple_row_col = self.get_spots(choose_movie, choose_projection)
        row, col = self.get_position(seat)

        if CINEMA_MAP[row][col] == 'X':
            print("This seat is already taken!")
            print(self.print_map())
        elif row >= len(CINEMA_MAP) or col >= len(CINEMA_MAP[0]):
            print("Lol...NO!")
        else:
            self.make_new_reservation(choose_movie, choose_user, choose_projection, seat)

            # ako se e izpulnilo vika make make_new_reservation

    def make_new_reservation(self, m_id, username, projection_id, seat):
        row, col = self.get_position(seat)
        user = (username, projection_id, row, col)
        reservation = '''INSERT INTO Reservations (username, projection_id, row, col)
                         VALUES (?, ?, ?, ?);'''
        self.c.execute(reservation, user)
        self.conn.commit()

        tuple_with_spots = self.get_spots(m_id, projection_id)
        self.change_map(tuple_with_spots)
        print(self.print_map())


class CLI:

    def __init__(self):
        self.cinema = Cinema()

    def check_show_movie_projections(self, split_input):
        id_movie = split_input[1]
        name_movie = self.cinema.get_name_movie(id_movie)

        try:
            date = split_input[2]
            return self.cinema.show_movie_projections_with_date(name_movie, id_movie, date)
        except IndexError:
            return self.cinema.show_movie_projections(id_movie, name_movie)

    def make_reservation(self):
        choose_user = input("Step 1 (User): Choose name> ") # username
        choose_tickets = input("Step 1 (User): Choose number of tickets> ")

        print(self.cinema.show_movies())

        choose_movie = input("Step 2 (Movie): Choose a movie> ")
        name = self.cinema.get_name_movie(choose_movie)

        print(self.cinema.show_movie_projections(choose_movie, name))

        choose_projection = input("Step 3 (Projection): Choose a projection> ")
        print(self.cinema.projection_choose(choose_projection))

        for ticket in range(0, int(choose_tickets)):
            seat = input("Step 4 (Seats): Choose seat {}> ".format(ticket + 1))
             # seat e string a trqbva da e tuple
            self.cinema.check_seat(choose_movie, choose_user, choose_projection, seat)
            # ako ima svobodno mqsto vika make_new_reservation

    def input_command(self):
        start_input = input("> ")
        split_input = start_input.split(" ")
        command = split_input[0]
        while command != "exit":
            if command == "show_movies":
                print(self.cinema.show_movies())
                self.input_command()
            elif command == "show_movie_projections":
                print(self.check_show_movie_projections(split_input))
                self.input_command()
            elif command == "make_reservation":
                print(self.make_reservation())


def main():
    # c = Cinema()
    # print(c.print_map())
    test = CLI()
    print(test.input_command())

if __name__ == '__main__':
    main()
