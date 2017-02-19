class Weapon:

    def __init__(self, name_weapon='none', damage=0):
        self.__name_weapon = name_weapon
        self.__damage = damage

    def get_name_weapon(self):
        return self.__name_weapon

    def _get_damage(self):
        return self.__damage
