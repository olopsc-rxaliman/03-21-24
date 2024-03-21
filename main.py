from Entities import Player, Monster

player = Player('Steve', 20, 5)
monster = Monster('Zombie', 10, 2)

player.attack(monster)
player.attack(monster)
player.attack(monster)
monster.attack(player)

monster2 = Monster('Tarantula', 10, 100)

monster2.attack(player)
player.attack(monster2)