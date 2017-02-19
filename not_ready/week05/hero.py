from weapon import Weapon
from spell import Spell


class Hero:

    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate):
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__weapon = None
        self.__spell = None

    def __get_name(self):
        return self.__name

    def __get_title(self):
        return self.__title

    def known_as(self):
        return "{} the {}".format(self.__get_name(), self.__get_title())

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def is_alive(self):
        if self.get_health() <= 0:
            return False
        return True

    def can_cast(self):
        # _get_mana - metod ot class Spell - return mana_cost
        if self.get_mana > self.__spell._get_mana():
            return True
        return False

    def take_damage(self, damage_points):
        self.__health -= damage_points
        if self.get_health() <= 0:
            self.__health = 0

    def take_healing(self, healing_points):
        if self.is_alive():
            self.__health += healing_points
            if self.get_health() > 100:
                self.__health = 100
            return True
        else:
            return False

    def take_mana(self, mana_points):
        # da se dobavi pri move
        self.__mana += mana_points
        if self.get_mana() > 100:
            self.__mana = 100
        if self.get_mana() < 0:
            self.__mana = 0

    def equip(self, weapon):
        self.__weapon = weapon

    def learn(self, spell):
        self.__spell = spell

    def attack(self, by=""):
        if by == "weapon":
            self.__weapon._get_damage()
        if by == "spell":
            self.__spell._get_damage()
