from sql_manager import SQL_manager
import sqlite3


class CLI:

    def __init__(self, sql_manager):
        self.sql_manager = sql_manager
        self.status = True
        self.commands = {
        'register': self.register_user,
        'login': self.login_user(),
        'help': self.help,
        'exit': self.exit
        }

    def register_user(self, *args):
        username = args[0]
        password = args[1]
        self.sql_manager.register(username, password)

    def login_user(self, *args):
        username = args[0]
        password = args[1]
        logged_user = self.sql_manager.login(username, password)

        if logged_user:
            self.logged_menu(logged_user)
        else:
            print("Login failed")

    def help(self, *args):
        return """login - for logging in!
                  register - for creating new account!
                  exit - for closing program!"""

    def exit(self, *args):
        self.status = False

    def menu(self):
        print("Welcome to our bank service. You are not logged in.\n \
               Please register or login")

        while self.status:
            command = input("$$$>")

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            self.commands[command](username, password)

            # print("Not a valid command")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                self.sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self.sql_manager.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")


def main():
    conn = sqlite3.connect("bank.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql_manager = SQL_manager(conn, cursor)
    sql_manager.create_clients_table()

    cli = CLI(sql_manager)
    cli.menu()

if __name__ == '__main__':
    main()
