import random


class Car:

    def __init__(self, car, model, max_speed):
        self.__car = car
        self.__model = model
        self.__max_speed = max_speed

    def __str__(self):
        return "{} {} with {} max_speed"\
                .format(self.__car, self.__model, self.__max_speed)


class Driver:

    def __init__(self, name, car):
        self.__name = name
        self.__car = car

    def __str__(self):
        return "{} is racing {}".format(self.__name, self.__car)


class Race:
    def __init__(self, list_of_drivers):
        self.__list_of_drivers = list_of_drivers
        self. __list_of_crashed_drivers = []
        self.__list_of_points = {}
        self.__crash_chance = random.randrange(10)

    def __str__(self):
        return self.__list_of_points

    def crash(self, crashed):
        for car in self.__list_of_drivers:
            if car.__crash_chance == crashed:
                return car.__name

    def start_race(self):  # za edna obikolka
        crashed = max([car.__crash_chance for car in self.__list_of_drivers])
        print(crashed)
        self.__list_of_crashed_drivers.append(self.crash(crashed))
        return self.__list_of_crashed_drivers

    def calculate_points(self, _list_of_drivers):
        self.__list_of_points[self.__list_of_drivers[0]] = 8
        self.__list_of_points[self.__list_of_drivers[1]] = 6
        self.__list_of_points[self.__list_of_drivers[2]] = 4
        self.__list_of_points[self.__list_of_drivers[3]] = 0

        print(self.__list_of_points)

    def result(self):
        return "List of last champions:" + self.__list_of_drivers + \
               "List of crashed_drivers" + self.__list_of_crashed_drivers


class Championship:
    def __init__(self, name, races_count):
        self.__name = name
        self.__races_count = races_count

    def _print_score(self):
        print("Race " + self.__name)
        print("##### START #####")

    def top_3(self):
        pass


class CLI:

    def __init__(self, race):
        self.__race = race
        self.__race.start_race()

    def __hello_message(self):
        return "Hello PyRacer! \
              \nPlease, call command with the proper argument:"

    def start(self):

        print(self.__hello_message())

        while True:
            console_input = input("Enter a command:> ")
            try:
                text = console_input.split()
                command = text[0]
                if command == "exit":
                    break
                if command == "start":
                    race_name = text[1]
                    race_count = text[2]
                    # championship = Championship(race_name, race_count)
                    # print(championship._print_score())
                    print(self.__race.start_race())
                    # self.championship.define_score(race_count)
                # if command == "standings":
                #     pass
            except:
                print("You entered an invalid command! Please try again!")


def main():
    first_car = Car("audi", "A8", 300)
    second_car = Car("mercedes", "124", 260)
    third_car = Car("VW", "golf", 240)
    fourth_car = Car("mazda", "6", 270)
    ivo = Driver("ivo", first_car)
    rado = Driver("rado", second_car)
    slavqna = Driver("slavqna", third_car)
    pavlin = Driver("pavlin", fourth_car)

    race = Race([ivo, rado, slavqna, pavlin])
    # championship = Championship("first_race", 3)
    interface = CLI(race)
    interface.start()


if __name__ == '__main__':
    main()

