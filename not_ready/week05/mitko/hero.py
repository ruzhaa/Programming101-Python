from weapon import Weapon
from spell import Spell


class Hero:

    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=5):
        self.__name = name
        self.__title = title
        self._health = health
        self._mana = mana
        self._mana_regeneration_rate = mana_regeneration_rate
        self._weapon = Weapon()
        self._spell = Spell()

    def __get_name(self):
        return self.__name

    def __get_title(self):
        return self.__title

    def known_as(self):
        return "{} the {}".format(self.__get_name(), self.__get_title())

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        if self.get_health() <= 0:
            return False
        return True

    def can_cast(self):
        # _get_mana - metod ot class Spell - return mana_cost
        if self.get_mana > self._spell._get_mana():
            return True
        return False

    def take_damage(self, damage_points):
        self._health -= damage_points
        if self.get_health() <= 0:
            self._health = 0

    def take_healing(self, healing_points):
        if self.is_alive():
            self._health += healing_points
            if self.get_health() > 100:
                self._health = 100
            return True
        else:
            return False

    def take_mana(self, mana_points):
        # da se dobavi pri move
        self._mana += mana_points
        if self.get_mana() > 100:
            self._mana = 100
        if self.get_mana() < 0:
            self._mana = 0

    def regenerate_mana(self):
        self.take_mana(self._mana_regeneration_rate)

    def equip(self, weapon, damage):
        self._weapon = Weapon(weapon, damage)

    def learn(self, name, damage, mana_cost, cast_range):
        self._spell = Spell(name, damage, mana_cost, cast_range)

    def attack(self, by):
        if by == "weapon":
            return self._weapon._get_damage()
        if by == "spell":
            self._mana -= self._spell._mana_cost
            return self._spell._get_damage()
