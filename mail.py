import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        round_num = 1
        print("Игра начинается! Добро пожаловать в Битву героев!\n")

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_num}")
            self.player.attack(self.computer)

            if self.computer.is_alive():
                self.computer.attack(self.player)

            print(f"{self.player.name} — здоровье: {self.player.health}")
            print(f"{self.computer.name} — здоровье: {self.computer.health}")
            round_num += 1

        # Объявление победителя
        if self.player.is_alive():
            print(f"\n Победил {self.player.name}!")
        else:
            print(f"\n Победил {self.computer.name}!")

# Запуск игры
if __name__ == "__main__":
    name = input("Введите имя вашего героя: ")
    game = Game(name)
    game.start()
