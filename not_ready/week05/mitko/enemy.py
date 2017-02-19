class Enemy:
    def __init__(self, health=100, mana=100, damage=10):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points

    def take_mana(self, mana_points):
        self.mana += mana_points

    def attack(self):
        return self.damage

    def take_damage(self, damage):
        self.health -= damage
