class Dungeon:

    def __init__(self, file_name):
        self.file_name = file_name
        self.dungeon = []
        self.lives = 3
        self.position = [0, 0]

    def get_map(self):  # loading map
        with open(self.file_name, 'r') as data:
            self.dungeon = [line.rstrip('\n') for line in data]
        return self.dungeon

    def print_map(self):
        for element in self.dungeon:
            print(element)

    # finding the first free position in a row for positioning our hero
    def check_row(self, row_number):
        for index in range(len(self.dungeon[0])):
            if self.dungeon[row_number][index] == '.':
                self.position[0] = row_number
                self.position[1] = index
                return False
                break
        return True

    # position our hero on the first free cell within the map
    def starting_point(self):
        self.get_map()
        y = 0
        while y < len(self.dungeon) and self.check_row(y):
            y += 1

    # inserts/prints a symbol (ex.'H' for hero) to the chosen row
    def print_hero(self, avatar, y, x):
        if x == 0:
            row = '{}{}'.format(avatar, self.dungeon[y][x + 1:])
        if x == len(self.dungeon[y]) - 1:
            row = '{}{}'.format(self.dungeon[y][:x], avatar)
        row = '{}{}{}'.format(
            self.dungeon[y][:x], avatar, self.dungeon[y][x + 1:])
        self.dungeon[y] = row

    def spawn(self):
        if self.lives > 0:
            self.starting_point()
            self.print_hero('H', self.position[0], self.position[1])

    def is_cell_open(self, y, x):
        __open_cell = ['.', 'T', 'E', 'G']
        return self.dungeon[y][x] in __open_cell

    def hero_status(self, y, x):
        __open_cell = {'.': 'Moving', 'T': 'Treasure_found', 'E': 'Enemy_defeated', 'G': 'End'}
        return __open_cell[self.dungeon[y][x]]

    def move_down(self):
        if self.position[0] < len(self.dungeon) - 1 and self.is_cell_open(self.position[0] + 1, self.position[1]):
            self.print_hero('.', self.position[0], self.position[1])
            self.position[0] += 1
            _status = self.hero_status(self.position[0], self.position[1])
            self.print_hero('H', self.position[0], self.position[1])
            return _status

    def move_up(self):
        if self.position[0] > 0 and self.is_cell_open(self.position[0] - 1, self.position[1]):
            self.print_hero('.', self.position[0], self.position[1])
            self.position[0] -= 1
            _status = self.hero_status(self.position[0], self.position[1])
            self.print_hero('H', self.position[0], self.position[1])
            return _status

    def move_right(self):
        if self.position[1] < len(self.dungeon[0]) - 1 and self.is_cell_open(self.position[0], self.position[1] + 1):
            self.print_hero('.', self.position[0], self.position[1])
            self.position[1] += 1
            _status = self.hero_status(self.position[0], self.position[1])
            self.print_hero('H', self.position[0], self.position[1])
            return _status

    def move_left(self):
        if self.position[1] > 0 and self.is_cell_open(self.position[0], self.position[1] - 1):
            self.print_hero('.', self.position[0], self.position[1])
            self.position[1] -= 1
            _status = self.hero_status(self.position[0], self.position[1])
            self.print_hero('H', self.position[0], self.position[1])
            return _status
