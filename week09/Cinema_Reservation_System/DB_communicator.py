import sqlite3
import settings


class Communicator:

    @staticmethod
    def print_map(cinema_map):
        current_cinema_map = ""
        for row in cinema_map:
            for col in row:
                current_cinema_map += col + " "
            current_cinema_map += "\n"
        return current_cinema_map

    def __init__(self, cursor, db):
        self.c = cursor
        self.db = db

    def get_movies(self):
        self.c.execute('''SELECT Movies.m_id, Movies.name, Movies.rating
                          FROM Movies
                          ORDER BY Movies.rating DESC;
            ''')

        result = "Current movies: \n"

        for row in self.c.fetchall():
            result += "[{}] - {} ({}) \n".\
                    format(row['m_id'], row['name'], row['rating'])
        return result

    def get_projection_by_id(self, projection_id, name_movie):
        self.c.execute('''SELECT p.m_type, p.m_date, p.time
                  FROM Projections AS p
                  JOIN Movies AS m
                  ON p.movie_id = m.m_id
                  WHERE p.p_id = ?
                  ORDER BY p.m_date;''', projection_id)

        result = ""
        for row in self.c.fetchall():
            result += "{} {} ({})".format(row['m_date'], row['time'], row['m_type'])
        return result

    def get_movie_projections(self, m_id, name_movie):
        t = (m_id, )
        self.c.execute('''SELECT p.p_id, p.m_type, p.m_date, p.time
                  FROM Projections AS p
                  JOIN Movies AS m
                  ON p.movie_id = m.m_id
                  WHERE m.m_id = ?
                  ORDER BY p.m_date;''', t)
        result = "Projections for movie '{}':\n".format(name_movie)

        for row in self.c.fetchall():
            seats = self.count_seats(str(row['p_id']))
            result += "[{}] - {} {} ({}) - {}\n".\
                       format(row['p_id'], row['m_date'], row['time'], row['m_type'], seats)
        return result

    def get_movie_projections_with_date(self, m_id, m_date, name_movie):
        t = (m_id, m_date)
        self.c.execute('''SELECT p.m_type, p.time
                  FROM projections AS p
                  JOIN movies AS m
                  ON p.movie_id = m.m_id
                  WHERE m.m_id = ? AND p.m_date = ?;
                  ''', t)

        count = 1
        result = "Projections for movie '{}' on date {}: \n".\
            format(name_movie, m_date)

        for row in self.c.fetchall():
            result += "[{}] - {} ({})\n".\
                    format(count, row['time'], row['m_type'])
            count += 1
        return result

    def get_name_movie(self, movie_id):
        self.c.execute('''SELECT Movies.name
                          FROM Movies
                          WHERE Movies.m_id = ?;''', str(movie_id))

        for row in self.c.fetchall():
            return row['name']

    def projection_choose(self, user_projection_id):
        print("Available seats (marked with a dot):")
        matrix = self.change_map(user_projection_id)
        print(self.print_map(matrix))

    def change_map(self, p_id):
        rows = settings.CINEMA_ROW
        cols = settings.CINEMA_COL
        tuple_of_seats_for_current_projection = self.get_seats_for_projection(p_id)

        cinema_map = []

        row_headers = ["  " if x == 0 else str(x) for x in range(rows + 1)]
        cinema_map.append(row_headers)

        for row in range(rows):
            cinema_map.append([" " + str(row + 1) if col == 0 else "." for col in range(cols + 1)])

        for group in tuple_of_seats_for_current_projection:
            cinema_map[group[0]][group[1]] = "X"

        return cinema_map

    def check_seat_in_map(self, p_id, row, col):
        current_cinema_map = self.change_map(p_id)

        if current_cinema_map[row][col] == 'X':
            return True
        return False

    def get_seats_for_projection(self, p_id):
        self.c.execute('''SELECT r.row, r.col
                          FROM Reservations AS r
                          JOIN Projections AS p
                          ON r.projection_id=p.p_id
                          WHERE p.p_id=?;''', str(p_id))
        tuple_of_seats = ()
        for row in self.c.fetchall():
            tuple_of_seats += ((row['row'], row['col']), )
        return tuple_of_seats

    def get_position(self, str_with_position):
        for char in str_with_position:
            if char in "()":
                str_with_position = str_with_position.replace(char, '')

        row_and_col = str_with_position.split(", ")

        return row_and_col

    def count_seats(self, p_id):
        self.c.execute(''' SELECT COUNT(r.projection_id)
                           FROM projections AS p
                           JOIN reservations AS r
                           ON r.projection_id=p.p_id
                           WHERE p.p_id=?''', p_id)
        all_seats = settings.CINEMA_ROW * settings.CINEMA_COL
        number_of_seats = 0
        for row in self.c.fetchall():
            number_of_seats = row['COUNT(r.projection_id)']
        return all_seats - number_of_seats

    def check_position(self, p_id, list_with_position):
        row = int(list_with_position[0])
        col = int(list_with_position[1])
        if row > settings.CINEMA_ROW or col > settings.CINEMA_COL:
            return "Lol...NO!"
        elif self.check_seat_in_map(p_id, row, col):
            print("This seat is already taken!")
            current_map = self.change_map(p_id)
            print(self.print_map(current_map))
        else:
            return True

    def make_new_reservation(self, reservation_list):
        whole_reservation = list()
        for group in reservation_list:
            user_name = group[0]
            user_projection_id = group[1]
            row = group[2][0]
            col = group[2][1]

            data_for_one_reservation = (user_name, user_projection_id, int(row), int(col))
            whole_reservation.append(data_for_one_reservation)

        return whole_reservation

    def create_new_reservation(self, reservation_list, user_projection_id):
        reservation = self.make_new_reservation(reservation_list)
        for group in reservation:
            self.c.execute(''' INSERT INTO Reservations (username, projection_id, row, col)
                               VALUES (?, ?, ?, ?)''', group)
        self.db.commit()
        return " Thanks \n Bye bye! :)"
