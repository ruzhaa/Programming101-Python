class Spell:

    def __init__(self, name='none', damage=0, mana_cost=0, cast_range=0):
        self._name_spell = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def _get_damage(self):
        return self._damage

    def get_name_spell(self):
        return self._name_spell
