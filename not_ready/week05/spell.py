class Spell:

    def __init__(self, name_spell, damage, mana_cost, cast_range):
        self.__name_spell = name_spell
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def _get_damage(self):
        return self.__damage
