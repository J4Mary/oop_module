class GameOver(Exception):
    """
    We call this exception to end the game
    """
    def __init__(self, player):
        super().__init__()
        self.player = player


class EnemyDown(Exception):
    """
    We call this exception when our enemy is killed
    """
    def __init__(self):
        super().__init__()
