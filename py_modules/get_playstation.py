import urllib3, json
import certifi
from bs4 import BeautifulSoup


def get_playstation(game_name):
    url = 'https://store.playstation.com/en-ie/grid/search-game/1?query='

    fmt_game_name = game_name.replace(' ', '%20')
    fmt_game_name = fmt_game_name.replace('-', '%20')
    constructed_url = url + fmt_game_name

    # initiate http request
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())

    request = http.request('GET', constructed_url)

    soup = BeautifulSoup(request.data, 'lxml')

    game_titles = soup.findAll('div', {"class": "grid-cell__title"})
    game_prices = soup.findAll('h3', {"class": "price-display__price"})
    game_link = soup.findAll('span', {"class": "grid-cell__prices-container"})
    game_image = soup.findAll('img', {"class": "product-image__img-main"})
    game_product_type = soup.findAll('div', {"class": "grid-cell__left-detail--detail-2"})
    game_psn_platform = soup.findAll('div', {"class": "grid-cell__left-detail--detail-1"})

    playstation_store_results = {}

    for result in range(0, (len(game_titles)-1)):
        if "bundle" in game_product_type[result].text.lower() or "game" in game_product_type[result].text.lower():
            dict = {}
            dict['PSN Price'] = game_prices[result].text
            dict['Product Type'] = game_product_type[result].text
            dict['PSN Platform'] = game_psn_platform[result].text
            dict['Image Location'] = game_image[result]['src'].replace("w=124&h=124", "w=1024")
            dict['PSN Link'] = 'https://store.playstation.com/' + \
                               game_link[result].findChild('a', {'class': 'internal-app-link'})['href']

            playstation_store_results[game_titles[result].text.strip().replace(u'\xa0', u' ')] = dict

    print(playstation_store_results)
    return playstation_store_results

