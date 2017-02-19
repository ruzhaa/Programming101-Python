import os
from dungeon import Dungeon
from hero import Hero
from enemy import Enemy
from treasure import Treasure
from spell import Spell
from weapon import Weapon

print('Hello player,\nyour adventure is about to begin..')
name = input('Enter your character\'s name:> ')
title = input('Enter {}\'s title:> '.format(name))
hero = Hero(name, title)
treasure = Treasure()
dungeon = Dungeon('level01.txt')
dungeon.spawn()
os.system('clear')
dungeon.print_map()
commands = {'s': dungeon.move_down, 'w': dungeon.move_up,
            'a': dungeon.move_left, 'd': dungeon.move_right}


def fight_mode():
    enemy = Enemy()
    os.system('clear')
    print('<<< FIGHT MODE>>>\nYou {} have just met a monster.. FIGHT your enemy to DEATH!'.format(
        hero.known_as()))
    input('Press "ENTER" to start the fight..')
    while hero.is_alive() and enemy.is_alive():
        os.system('clear')
        print('<<< FIGHT MODE>>>')
        print('{} has {} health points and {} mana points'.format(
            hero.known_as(), hero.get_health(), hero.get_mana()))
        print('Enemy health points: {}'.format(enemy.get_health()))
        action = input('Enter "weapon" or "spell" to attack your enemy: ')
        enemy.take_damage(hero.attack(action))
        hero.take_damage(enemy.attack())


def treasure_found(choice, treasure):
    if choice == '1':
        hero.equip(treasure[0], treasure[1])
    elif choice == '2':
        hero.learn(treasure[0], treasure[1], treasure[2], treasure[3])
    elif choice == '3':
        hero.take_healing(treasure)
    elif choice == '4':
        hero.take_mana(treasure)
    input('Press \'Enter\' to continue..')


def main():
    while hero.is_alive():
        hero.regenerate_mana()
        print('{} has {} health points and {} mana points'.format(
            hero.known_as(), hero.get_health(), hero.get_mana()))
        comm = input('Enter command (\'W\' for up, \'S\' for down, \'A\' for left, \'D\' for right) and press \'ENTER\' to move: ')
        if comm == 'esc':
            break
        status = commands[comm]()
        if status == 'Enemy_defeated':
            fight_mode()
        elif status == 'Treasure_found':
            found = treasure.choose_treasure()
            treasure_found(found[0], found[1])
        elif status == 'End':
            print('Congratulations! You finished this level..')
            break
        os.system('clear')
        dungeon.print_map()
        if not hero.is_alive():
            status = 'GAME OVER'
        print('Status: {}'.format(status))


if __name__ == '__main__':
    main()
