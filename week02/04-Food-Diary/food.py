import time


def input_command():
    print("Enter command> ")
    option = input()
    command = option.split(" ")
    return command


def main():
    print("Hello and Welcome!")
    print("Choose an option.")
    print("1. meal - to write what are you eating now.")
    print("2. list <dd.mm.yyyy> - lists all the means that you ate that day.\n")

    meals = list()
    data_list = dict()
    list_input = input_command()
    current_data = time.strftime("%d.%m.%Y")

    while list_input[0] == "meal":
        meals.append(list_input[1])
        data_list[current_data] = meals
        print("OK it is saved")
        list_input = input_command()

    if list_input[0] == "list":
        if list_input[1] in data_list:
            key = list_input[1]
            print(data_list[key])


if __name__ == '__main__':

    main()
