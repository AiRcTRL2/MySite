from MySite.py_modules.get_metadata import *
from MySite.py_modules.get_xbox import *
from MySite.py_modules.set_database import *


class GameObject:
    """ The purpose of this class is to implement all other available modules which help construct game
        information and collect metadata prior to exporting this to a database.

        The only information it assumes to be supplied is the game name and platform (optional),
        and should resolve to an error if this is incorrect.
    """

    def __init__(self, game_name, game_platform=None):
        self.game_name = game_name
        self.game_rating = None
        self.game_img_loc = None
        self.game_genres = None
        self.game_platform = game_platform
        self.game_cost_at_store = None
        self.game_found = False




    def get_metadata(self):
        # format game name for applicable urls at metacritic.com
        fmt_game_name = self.game_name.replace(':', "")
        fmt_game_name = fmt_game_name.replace(" ", "-")
        fmt_game_name = fmt_game_name.lower()
        print(fmt_game_name)
        data = get_metadata(fmt_game_name)
        print(data)
        self.game_genres = data[1]
        print(self.game_genres)

