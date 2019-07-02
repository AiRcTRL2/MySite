import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# base urls for pulling metacritic data
metacritic_platforms = {'Xbox One': "https://www.metacritic.com/game/xbox-one/",
                        'Playstation 4': "https://www.metacritic.com/game/playstation-4/",
                        'PC': "https://www.metacritic.com/game/pc/",
                        'Nintendo Switch': "https://www.metacritic.com/game/switch/"}

ua = UserAgent()
header = {'User-Agent': str(ua.chrome)}


def get_metadata(game_name, platform=None):

    if platform is None:

        # store for platform found
        platforms = {}
        genres = set()
        for platform in metacritic_platforms:

            # construct url
            url = metacritic_platforms[platform] + game_name
            # send request
            response = requests.get(url, headers=header)

            # parse the response html
            soup = BeautifulSoup(response.text, 'html.parser')

            # print(response.status_code)

            # check if we have received a not found error
            if response.status_code == 404:
                platforms[platform] = "N/A"

            else:
                # get game genre
                find_genre_div = soup.find('li', {"class": "product_genre"})\
                    .findChildren("span", {'class': 'data'}, recursive=False)

                for child in find_genre_div:
                    if child.text not in genres:
                        genres.add(child.text)

                # get metascore or n/a
                try:
                    metascore = soup.find('span', {"itemprop": "ratingValue"}).text
                except AttributeError:
                    metascore = "Rating not currently available."

                platforms[platform] = metascore

        return platforms, genres
