from MySite.py_modules.set_database import *
from MySite.py_modules.get_playstation import *
from MySite.py_modules.game_object import *

def find(game_name):
    """ The find function provides the functionality at the backend to determine whether a record exists
        for the searched term. It should return required metadata for the front-end based on the search results.

        Parameters:
            :argument1 (string): Game name

        Returns:
            Lists: Game ID, Game Name, Trailer Link, Tracking since (record date), Image locations
    """

    get_game_data = """ SELECT * FROM `mysite-games`.game_database
                            WHERE game_name LIKE '%{}%';
                        """.format(game_name)
    result = send_to_db(get_game_data, True)
    result = [list(row) for row in result]

    for row in result:
        row[3] = str(row[3])

    return result

def build(game_name):
    """ The purpose of this function is to be executed when the find function fails to identify any records
        in the database. It will then consult some game search engines, such as PSN, Microsoft Store and Metacritic
        to collect relevant metadata (if the title exists).

        Parameters:
            :argument1 (string): Game Name

        Returns:

    """

    query_psn = get_playstation(game_name)

    for key, value in query_psn.items():
        object = GameObject(key, value['Image Location'])
        # print(key)
        # print(value['Image Location'])

        object.set_metadata()
        object.get_game_data()

build("mortal kombat")