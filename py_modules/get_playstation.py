# from bs4 import BeautifulSoup
# import time
# from selenium import webdriver
#
#
# def get_xbox_details(game_name):
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument('window-size=1920x1080')
#
#     # initialize the driver
#     driver = webdriver.Chrome("../drivers/chromedriver.exe", options=options)
#
#     # go to default xbox one page
#     driver.get("https://store.playstation.com/en-ie/home/games")
#
#     # wait for results to load
#     time.sleep(3.5)
#
#     # define the search elements
#     playstation_search_field = driver.find_element_by_class_name('search-text-box__input')
#     playstation_search_button = driver.find_element_by_name('jetstream-search__search-button')
#
#     # get search name from function arg
#     playstation_search_field.send_keys(game_name)
#
#     # perform search
#     playstation_search_button.click()
#
#     driver.implicitly_wait(5)
#
#     # get all game div links for search results
#     playstation_search_results = driver.find_elements_by_class_name('gameDivLink')
#
#     # empty dict to hold results
#     game_results_parsed = {}
#
#     try:
#         # parse each result and find game data
#         for result in xbox_search_results:
#             soup = BeautifulSoup(result.get_attribute('innerHTML'), 'html.parser')
#             game_results_parsed[soup.find('h3').text] = [soup.find('img')['src'],
#                                                          soup.find('span', {"class": "textpricenew"}).text]
#         driver.close()
#
#     except AttributeError:
#         driver.close()
#         return 404
#
#     return game_results_parsed
