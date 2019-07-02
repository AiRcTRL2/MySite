from bs4 import BeautifulSoup
import time
from selenium import webdriver
from fake_useragent import UserAgent

ua = UserAgent()
header = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

def create_ref_link():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent={0}'.format(header))

    # initialize the driver
    driver = webdriver.Chrome("../drivers/chromedriver.exe", options=options)

    # go to default auth page
    driver.get("https://id.g2a.com/login?client_id=g2a&redirect_uri=https:%2F%2Fwww.g2a.com%2Foauth2%2Ftoken&response_type=code")
    driver.implicitly_wait(15)

    # find consent button
    driver.find_element_by_xpath('/html/body/app/cookie-consent/div/div/div[3]/button[1]').click()

    # define the username xpath
    find_username = driver.find_element_by_xpath("/html/body/app/app-login/div/div/div/form/div[1]/div/input")
    find_username.click()
    find_username.send_keys("")

    # driver.get_screenshot_as_file("goldmine.png")
    # driver.close()

    # # define auth ## improve security here later
    find_pass = driver.find_element_by_xpath('/html/body/app/app-login/div/div/div/form/div[2]/div/input')
    find_pass.click()
    find_pass.send_keys(input("Enter pass"))

    login_button = driver.find_element_by_xpath('/html/body/app/app-login/div/div/div/form/div[5]/button')
    login_button.click()

    time.sleep(20)
    #
    # driver.get_screenshot_as_file("goldmine.png")

    # # select input box
    # xbox_search_field.click()
    # # get search name from function arg
    # xbox_search_field.send_keys(game_name)
    #
    # # perform search
    # xbox_search_button.click()
    #
    # time.sleep(1.05)
    #
    # # get all game div links for search results
    # xbox_search_results = driver.find_elements_by_class_name('gameDivLink')

create_ref_link()