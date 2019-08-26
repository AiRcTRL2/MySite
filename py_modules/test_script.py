from MySite.py_modules.set_database import *

# next query the DB the retrieve the newly created game_id associated with the game name
get_id_query = """ SELECT game_id
                    FROM `mysite-games`.game_database
                    WHERE game_name='borderlands 3';"""
game_id = send_to_db(get_id_query)
for row in game_id:
    print(row)

    # SELECT
    # D.game_name, D.game_trailer, D.date_recorded, D.image_loc, G.game_genre, R.game_platform, R.game_rating
    # FROM
    # game_database as D, game_genres as G, game_platform_ratings as R;
    #