import sql_manager


def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    sql_manager.register(username, password)

    print("Registration Successfull")


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    logged_user = sql_manager.login(username, password)

    if logged_user:
        logged_menu(logged_user)
    else:
        print("Login failed")


def help_menu():
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")


def info_menu(logged_user):
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')


def changepass(logged_user):
    new_pass = input("Enter your new password: ")
    sql_manager.change_pass(new_pass, logged_user)


def change_message(logged_user):
    new_message = input("Enter your new message: ")
    sql_manager.change_message(new_message, logged_user)


def show_message(logged_user):
    print(logged_user.get_message())


def logged_help():
    print("info - for showing account info")
    print("changepass - for changing passowrd")
    print("change-message - for changing users message")
    print("show-message - for showing users message")


commands = {
    'register': register_user,
    'login': login_user,
    'help': help_menu,
}

logged_commands = {
    'info': info_menu,
    'changepass': changepass,
    'change-message': change_message,
    'show-message': show_message,
    'help': logged_help
}


def main_menu():
    print("Welcome to our bank service. You are not logged in.\
          \nPlease register or login")

    while True:
        command = input("$$$>")
        if command == 'exit':
            break
        else:
            try:
                commands[command]()
            except:
                print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'help':
            logged_commands[command]()
        else:
            logged_commands[command](logged_user)


def main():
    sql_manager.create_clients_table()
    main_menu()


if __name__ == '__main__':
    main()
