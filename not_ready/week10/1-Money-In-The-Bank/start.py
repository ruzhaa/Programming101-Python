import sql_manager
from validate import StrongPasswordException


commands = {
    "register": register_user,
    "login": login,
    "help": help_menu,
    "exit": exit,
    "info": info
}

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        sql_manager.register(username, password)
        print("Registration Successfull")
    except StrongPasswordException as e:
        print(e)


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    logged_user = sql_manager.login(username, password)

    if logged_user:
        logged_menu(logged_user)
    else:
        print("Login failed")


def help():
    return """login - for logging in!
              register - for creating new account!
              exit - for closing program!"""


# def exit(self, *args):
#     if command == 'exit':
#             break
#     else:
#         print("Not a valid command")


def main_menu():
    print("Welcome to our bank service. You are not logged in.\n\
           Please register or login")

    while True:
        command = input("$$$>")

        commands[command]()

        if command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
