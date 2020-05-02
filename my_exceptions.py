class GameOver(Exception):
    """
    We call this exception to end the game
    """
    def __init__(self, player):
        super().__init__()
        self.player = player

    @staticmethod
    def write_score(self):
        """
        Writes score in the file 'scores.txt'
        """
        file = open('scores.txt', 'a')
        row = "{}: {}\n".format(self.name, self.score)
        file.write(row)


class EnemyDown(Exception):
    """
    We call this exception when our enemy is killed
    """
    def __init__(self):
        super().__init__()
