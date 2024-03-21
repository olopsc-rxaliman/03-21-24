class Entity:
    def __init__(self, name: str, health: int, attack_power: int):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        print('-' * 20)
        if health <= 0:
            self.__health = 0
            self.__alive = False
            print(f"A wild {self} has spawned, but died immediately... (0 HP)")
        else:
            self.__alive = True
            print(f"A wild {self} has spawned! ({health} HP)")

    @property
    def __take_damage(self):
        return f"{self} says \'Ouch!\'"

    @__take_damage.setter
    def __take_damage(self, attack_damage):
        self.__health -= attack_damage
        if self.__health <= 0:
            self.__health = 0
            self.__alive = False
            print(f"{self} fainted... (0 HP)")
        else:
            print(f"{self} receives {attack_damage} attack damage! ({self.__health} HP)")

    def is_alive(self):
        return self.__alive

    def __str__(self):
        return f"{type(self).__name__} \'{self.__name}\'"


class Player(Entity):
    def __init__(self, name: str, health: int, attack_power: int):
        super().__init__(name, health, attack_power)
    
    def attack(self, monster: Entity):
        print('-' * 20)
        if self.is_alive():
            print(f"{self} hits {monster} with its fists!")
            if monster.is_alive():
                print(monster._Entity__take_damage)
                monster._Entity__take_damage = self._Entity__attack_power
            else:
                print(f"But {monster} is already fainted... (0 HP)")
        else:
            print(f"{self} can\'t attack... (0 HP)")


class Monster(Entity):
    def __init__(self, name: str, health: int, attack_power: int):
        super().__init__(name, health, attack_power)
    
    def attack(self, player: Entity):
        print('-' * 20)
        if self.is_alive():
            print(f"{self} bites the {player} with its mouth!")
            if player.is_alive():
                print(player._Entity__take_damage)
                player._Entity__take_damage = self._Entity__attack_power
            else:
                print(f"But {player} is already fainted... (0 HP)")
        else:
            print(f"{self} can\'t attack... (0 HP)")