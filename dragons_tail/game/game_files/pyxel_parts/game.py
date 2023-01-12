import pyxel as px
from time import time

from game_files.pyxel_parts.constants import WIDTH, HEIGHT
from game_files.pyxel_parts.game_states import TownScreenState
from game_files.other_assets.character_builder import Player
from game_files.other_assets.dicts import background_stats
bad_stats = [8,8,4,2]

game_stats = [background_stats['b']['stats']]
class Game:
    def __init__(self):

        self.score = 0
        self.lives = 3
        self.player = Player("Crae", **background_stats['b']['stats'], game=self)
        self.won_game = False
        self.text_timer = 0

        

        self.state = TownScreenState(self)

