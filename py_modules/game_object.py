from MySite.py_modules.get_metadata import *
from MySite.py_modules.get_xbox import *
from MySite.py_modules.goldmine import *
from MySite.py_modules.set_database import *
import datetime



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
        self.record_created = datetime.datetime.now().strftime("%Y/%m/%d")
        self.meta_critic_urls = None
        self.fetch_failed = False
        self.game_id = None

    def set_metadata(self):
        # format game name for applicable urls at metacritic.com
        fmt_game_name = self.game_name.replace(':', "")
        fmt_game_name = fmt_game_name.replace(" ", "-")
        fmt_game_name = fmt_game_name.lower()

        # send request to metacritic to get rating/
        data = get_metadata(fmt_game_name)

        # set the objects values to return values from metacritic
        self.game_genres = list(data[1])

        # cycle through tested platforms and find valid platforms
        temp_list = []
        for platform in data[0]:
            if data[0][platform]:
                temp_list.append(platform)
        self.game_platform = temp_list

        # game rating
        self.game_rating = data[0]

        # first check if xbox is a valid platform
        if 'Xbox One' in self.game_platform:
            # send request to microsoft to get artwork / price at store
            msoft_img_price = get_xbox_details(self.game_name)
        else:
            # This should not be here. Look to alternative platforms if Xbox is not a valid platform.
            # ----------------- BUILD ABOVE SCRIPTS! important! ----------------------
            msoft_img_price = None

        # initialise msoft_img_price_lower
        msoft_img_price_lower = None

        # below occaisionally fails, but usually not twice in a row. If fail, try again
        try:
            msoft_img_price_lower = dict((key.lower(), value) for key, value in msoft_img_price.items())
        except AttributeError:
            self.fetch_failed = True
            print("Error occurred with initial get_xbox_details query, thus except invalidated. Please send the"
                  "request again")

        if msoft_img_price_lower is not None:
            for key in msoft_img_price_lower:
                if self.game_name in key:
                    # print(msoft_img_price_lower.get(key))
                    self.game_img_loc = msoft_img_price_lower.get(key)[0]
                    try:
                        self.game_img_loc = self.game_img_loc.replace("h=300&w=200", "w=720")
                    except:
                        pass
                    self.game_cost_at_store = msoft_img_price_lower.get(key)[1]
                    self.game_name = key
                    break
        else:
            print("The dictionary is empty.")

        try:
            self.game_name = self.game_name.strip(" pre-order")
        except:
            pass

        # metacritic urls
        self.meta_critic_urls = data[2]

    def get_game_data(self):
        print(self.game_name)
        print(self.game_rating)
        print(self.game_img_loc)
        print(self.game_genres)
        print(self.game_platform)
        print(self.game_cost_at_store)
        print(self.record_created)
        print(self.meta_critic_urls)
        return self.game_name, self.game_rating, self.game_img_loc, self.game_genres, self.game_platform,\
            self.game_cost_at_store, self.record_created, self.meta_critic_urls

    def queries(self):

        # creates the first record in the DB in order to generate the game_id
        insert_game_meta = """ INSERT INTO game_database
                (game_id, game_name, game_trailer, date_recorded, image_loc)
                VALUES (NULL,%s,%s,%s,%s); """
        vals = (self.game_name, "www.youtube.com", self.record_created, self.game_img_loc)
        send_to_db(insert_game_meta, vals)

        # next query the DB the retrieve the newly created game_id associated with the game name
        get_id_query = """ SELECT game_id
                            FROM `mysite-games`.game_database
                            WHERE game_name='{}';""".format(self.game_name)
        self.game_id = send_to_db(get_id_query)[0]
        print(self.game_id)

        # insert each genre for the game
        insert_game_genres = """ INSERT INTO game_genres
                        (table_id, game_id_num, game_genre)
                        VALUES (NULL,%s,%s); """
        # execute this command for each genre found for the game
        for genre in self.game_genres:
            vals = (self.game_id, genre)
            send_to_db(insert_game_genres, vals)

        # insert ratings for each platform with respect to the game ID
        insert_game_ratings = """ INSERT INTO game_platform_ratings
                        (game_platform, game_id_number_plat, game_rating)
                        VALUES (%s,%s,%s); """
        for platform in self.game_platform:
            vals = (platform, self.game_id, self.game_rating[platform])
            send_to_db(insert_game_ratings, vals)



        # insert_game_name = """ INSERT INTO game_database\
        #                 (game_id, game_name, game_trailer, date_recorded)\
        #                 VALUES (NULL,%s,%s,%s); """
        # insert_game_name = """ INSERT INTO game_database\
        #                 (game_id, game_name, game_trailer, date_recorded)\
        #                 VALUES (NULL,%s,%s,%s); """
        # insert_game_name = """ INSERT INTO game_database\
        #                 (game_id, game_name, game_trailer, date_recorded)\
        #                 VALUES (NULL,%s,%s,%s); """
        # insert_game_name = """ INSERT INTO game_database\
        #                 (game_id, game_name, game_trailer, date_recorded)\
        #                 VALUES (NULL,%s,%s,%s); """
        # insert_game_name = """ INSERT INTO game_database\
        #                 (game_id, game_name, game_trailer, date_recorded)\
        #                 VALUES (NULL,%s,%s,%s); """

#
#
# fifa = GameObject("fifa 19")
# fifa.set_metadata()
# fifa.get_game_data()
# fifa.queries()
