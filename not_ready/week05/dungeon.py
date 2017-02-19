import os


class Dungeon:

    def __init__(self, file_name):
        self.file_name = file_name
        self.dungeon = []
        self.spawn_points = 3
        self.position = [0, 0]

    def get_map(self):
        with open(self.file_name, 'r') as data:
            self.dungeon = [line.rstrip('\n') for line in data]
        return self.dungeon

    def print_map(self):
        for element in self.dungeon:
            print(element)

    def starting_point(self):
        self.get_map()
        for row in range(len(self.dungeon)):
            for index in range(len(self.dungeon[row])):
                if self.dungeon[row][index] == '.':
                    self.position[0] = row
                    self.position[1] = index
                    break

    def print_hero(self, avatar, y, x):
        if x == 0:
            row = '{}{}'.format(avatar, self.dungeon[y][x + 1:])
        if x == len(self.dungeon[y]) - 1:
            row = '{}{}'.format(self.dungeon[y][:x], avatar)
        row = '{}{}{}'.format(
            self.dungeon[y][:x], avatar, self.dungeon[y][x + 1:])
        self.dungeon[y] = row

    def spawn(self):
        if self.spawn_points > 0:
            self.starting_point()
            self.print_hero('H', self.position[0], self.position[1])

    def move_down(self):
        self.print_hero('.', self.position[0], self.position[1])
        self.position[0] += 1
        self.print_hero('H', self.position[0], self.position[1])


#os.system('clear')
a = Dungeon('level01.txt')
a.spawn()
#a.move_down()
a.print_map()
print a.position
