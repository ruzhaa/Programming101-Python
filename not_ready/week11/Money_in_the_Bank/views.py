from controllers import ClientAlreadyRegistered


class MainView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        while True:
            command = input('Enter command> ')

            if command == 'register':
                username = input('Enter your username: ')
                password = input('Enter your password: ')

                try:
                    self.controller.register(username, password)
                    print('Success!')
                except ClientAlreadyRegistered as e:
                    print(e)

            elif command == 'login':
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                self.controller.login(username, password)
            #     try:
            #         logged_user = self.controller.login(username, password)
            #     except UserBlockedException as e:
            #         print(e)

                # if logged_user:
                #     logged_menu(logged_user)
                # else:
                #     print("Login failed")
