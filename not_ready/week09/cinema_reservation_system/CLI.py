import sqlite3
from DB_communicator import Communicator


class CLI:

    def __init__(self, db_communicator):
        self.db_communicator = db_communicator
        self.user_status = True

        self.user_commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "make_reservations": self.make_reservations,
            "finalize": self.finalize,
            "exit": self.exit
        }

    def show_movies(self, *args):
        print(self.db_communicator.get_movies())

    def show_movie_projections(self, *args):
        m_id = args[0]
        name_movie = self.db_communicator.get_name_movie(m_id)
        try:
            if args[1] is not None:
                print(self.db_communicator.get_movie_projections_with_date(m_id, args[1], name_movie))
            else:
                print(self.db_communicator.get_movie_projections(m_id, name_movie))
        except:
                print(self.db_communicator.get_movie_projections(m_id, name_movie))

    def make_reservations(self, *args):
        user_name = input("Step 1 (User): Choose name> ")
        number_of_tickets = input("Step 1 (User): Choose number of tickets> ")

        self.show_movies()

        user_movie_id = input("Step 2 (Movie): Choose a movie> ")
        self.show_movie_projections(user_movie_id)
        user_projection_id = int(input("Step 3 (Projection): Choose a projection> "))

        self.db_communicator.projection_choose(user_projection_id)
        seats = ""
        reservation_list = list()
        id_ticket = 1

        while int(number_of_tickets) + 1 > id_ticket:
            choose_seat = input("Step 4 (Seats): Choose seat {}> ".format(id_ticket))
            seats += choose_seat + ", "
            list_with_position = self.db_communicator.get_position(choose_seat)

            if self.db_communicator.check_position(user_projection_id, list_with_position) is not True:
                print(self.db_communicator.check_position(user_projection_id, list_with_position))
            else:
                current_data_for_reservation = \
                   (user_name, user_projection_id, list_with_position)
                reservation_list.append(current_data_for_reservation)
                id_ticket += 1

        name_movie = self.db_communicator.get_name_movie(user_movie_id)
        date_and_time = self.db_communicator.get_projection_by_id(user_movie_id, name_movie)
        print(" This is your reservation:\n Movie: '{}' \n Date and Time: {}\n Seats: {}"\
            .format(name_movie, date_and_time, seats))

        end_input = input("Step 5 (Confirm - type 'finalize') > ")
        if end_input == "finalize":
            self.finalize(reservation_list, user_projection_id)


    def finalize(self, reservation_list, user_projection_id):
        print(self.db_communicator.create_new_reservation(reservation_list, user_projection_id))
        return self.exit()

    def exit(self, *args):
        self.user_status = False

    def start(self):
        print("WELCOME TO THE CINEMA!\n")
        while self.user_status:
            command = ""
            argument_one = None
            argument_two = None

            user_input = input("Enter command: >>> ")
            user_input = user_input.split(" ")
            command = user_input[0]
            if len(user_input) > 1:
                argument_one = user_input[1]
                if len(user_input) > 2:
                    argument_two = user_input[2]

            self.user_commands[command](argument_one, argument_two)


def main():
    db = sqlite3.connect('cinema_data.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    db_communicator = Communicator(cursor, db)
    cli = CLI(db_communicator)
    cli.start()


if __name__ == '__main__':
    main()
