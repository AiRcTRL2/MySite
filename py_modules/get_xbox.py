from bs4 import BeautifulSoup
import time
from selenium import webdriver


def get_xbox_details(game_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    # initialize the driver
    driver = webdriver.Chrome("../drivers/chromedriver.exe", options=options)

    # go to default xbox one page
    driver.get("https://www.xbox.com/en-IE/games/xbox-one?xr=shellnav")

    # wait for results to load
    driver.implicitly_wait(12)

    # define the search elements
    xbox_search_field = driver.find_element_by_name('search-field')
    xbox_search_button = driver.find_element_by_name('search-button')

    # select input box
    xbox_search_field.click()
    # get search name from function arg
    xbox_search_field.send_keys(game_name)

    time.sleep(5)
    # perform search
    xbox_search_button.click()

    # get all game div links for search results
    xbox_search_results = driver.find_elements_by_class_name('gameDivLink')

    # empty dict to hold results
    game_results_parsed = {}

    try:
        # parse each result and find game data
        for result in xbox_search_results:
            soup = BeautifulSoup(result.get_attribute('innerHTML'), 'html.parser')
            game_results_parsed[soup.find('h3').text] = [soup.find('img')['src'],
                                                         soup.find('span', {"class": "textpricenew"}).text]
        driver.close()
    finally:
        pass
    # except AttributeError:
    #     driver.close()
    #     return 404

    return game_results_parsed