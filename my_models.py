from random import randint

from my_exceptions import EnemyDown
from my_exceptions import GameOver
from my_settings import LIVES


class Enemy:
    """
    Class of your enemy. Consists your level
    """
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        """
        A function to choose an attack
        :return: a random number
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Decrease the number of your enemy's lives
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    A worker class
    """
    def __init__(self, name):
        self.name = name
        self.lives = LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        Defines the result of fight.
        Warrior(1) wins robber(2). Robber(2) wins wizard(3). Wizard(3) wins warrior(1).
        :return: 1(win), -1(lose), 0(draw)
        """
        if attack == defense:
            return 0
        elif attack == 1 and defense == 2 \
                or attack == 2 and defense == 3 \
                or attack == 3 and defense == 1:
            return 1
        else:
            return -1

    def write_score(self):
        """
        Writes score in the file 'scores.txt'
        """
        file = open('scores.txt', 'a')
        row = "{}: {}\n".format(self.name, self.score)
        file.write(row)

    def decrease_lives(self):
        """
        Decrease number of your lives
        """
        self.lives -= 1
        if self.lives == 0:
            print('Your score: {}'.format(self.score))
            self.write_score()
            raise GameOver(self)

    def attack(self, enemy_obj):
        """
        Ask your character and print the result of the attack
        """
        you = None
        while you not in (1, 2, 3):
            try:
                you = int(input("Input a character to attack: "
                                "(warrior - 1, robber - 2, wizard - 3)"))
                if you not in (1, 2, 3):
                    raise ValueError
            except ValueError:
                print("Incorrect input")
        computer = enemy_obj.select_attack()
        result = self.fight(you, computer)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You attacked successfully!")
            self.score += 1
            enemy_obj.decrease_lives()
        if result == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        """
        Ask your character and print the result of the defence
         """
        you = int(input("Input a character to defence: (warrior - 1, robber - 2, wizard - 3)"))
        computer = enemy_obj.select_attack()
        result = self.fight(computer, you)
        if result == 0:
            print("It's a draw!")
        if result == -1:
            print("You defenced successfully!")
        if result == 1:
            print("You missed!")
            self.decrease_lives()
