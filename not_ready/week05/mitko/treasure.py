import json
import os
from random import shuffle


def read_json(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
    return data


class Treasure:

    def __init__(self):
        self.treasure_list = read_json('treasures.json')['treasures']

    def random_treasure(self):
        shuffle(self.treasure_list)
        treasure = self.treasure_list[0]
        return treasure

    def treasure_list_shrink(self):
        if len(self.treasure_list) > 1:
            self.treasure_list = self.treasure_list[1:]

    def get_treasure(self):
        treasure = self.random_treasure()
        self.treasure_list_shrink()
        return treasure
        
    def print_list(self, treasure_dict):
        os.system('clear')
        print('Congratulations! You have found a treasure chest containing:')
        for element in sorted(treasure_dict):
            print(element)
        choice = input('Enter a number from 1 to 4 for your choice:> ')
        return choice[0]

    def print_treasure_type(self, choice, treasure):
        if choice == '1':
            print('You earned a weapon called \'{}\' causing {} damage to enemies!'.format(treasure[0], treasure[1]))
        elif choice == '2':
            print('You earned a spell called \'{}\' causing {} damage to enemies with {} mana cost and {} cast range!'.format(treasure[0], treasure[1], treasure[2], treasure[3]))
        elif choice == '3':
            print('You earned {} health points!'.format(treasure))
        elif choice == '4':
            print('You earned {} mana points!'.format(treasure))

    def choose_treasure(self):
        treasure_list = self.get_treasure()
        choice = self.print_list(treasure_list)
        for element in treasure_list:
            if choice in element:
                self.print_treasure_type(choice, treasure_list[element])
                return choice, treasure_list[element]

