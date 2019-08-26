from bs4 import BeautifulSoup
import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
import uuid

ua = UserAgent()
header = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

def create_ref_link(game_name):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent={0}'.format(header))
    options.add_argument("user-data-dir=C:\\Users\\karzk\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1)")

    # initialize the driver
    driver = webdriver.Chrome("../drivers/chromedriver.exe", options=options)

    # go to default auth page
    # driver.get("https://id.g2a.com/login?client_id=g2a&redirect_uri=https:%2F%2Fwww.g2a.com%2Foauth2%2Ftoken&response_type=code")
    # driver.implicitly_wait(2)

    # find consent button
    # driver.find_element_by_xpath('/html/body/app/cookie-consent/div/div/div[3]/button[1]').click()

    try:
        # go to login page
        driver.get('https://www.g2a.com/goldmine/reflinks/')
        driver.find_element_by_xpath('//*[@id="mlmHeader"]/div/div[2]/div[3]/div/a[2]').click()

        # define the username xpath
        find_username = driver.find_element_by_xpath("/html/body/app/app-login/div/div/div/form/div[1]/div/input")
        find_username.click()
        find_username.send_keys("")

        # # define auth ## improve security here later
        find_pass = driver.find_element_by_xpath('/html/body/app/app-login/div/div/div/form/div[2]/div/input')
        find_pass.click()
        find_pass.send_keys(input("Enter pass: "))

        login_button = driver.find_element_by_xpath('/html/body/app/app-login/div/div/div/form/div[5]/button')
        login_button.click()

    except (AttributeError, NoSuchElementException) as e:
        pass


    # add a ref link
    driver.find_element_by_class_name("add-more").click()
    # click link to game
    driver.find_element_by_xpath('//*[@id="reflink-new-popup"]/div/div/ul[1]/li[1]').click()
    # click search bar
    search = driver.find_element_by_xpath('//*[@id="reflink-new-popup"]/div/div/ul[2]/li[1]/div[1]/input[1]')
    search.click()
    search.send_keys(game_name)
    time.sleep(.2)
    # click search button
    search_button = driver.find_element_by_xpath('//*[@id="searchGamesBtn"]')
    search_button.click()
    search_button.click()
    driver.implicitly_wait(5)
    time.sleep(1)
    #
    result = driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[1]')
    result.click()

    # get the title of the game
    title = driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[1]/div[3]/h4').text
    reflink_name = driver.find_element_by_xpath('//*[@id="reflink-new-popup"]/div/div/div[3]/div/input')
    reflink_name.click()

    # random string to use as reflink
    lowercase_str = uuid.uuid4().hex
    reflink_name.send_keys(lowercase_str)
    # press create reflink
    driver.find_element_by_xpath('//*[@id="reflink-new-popup"]/div/div/div[4]/div/div').click()
    # wait for reflinks table to populate new result -> implicitly wait does not work here for some reason. Probably
    # due to the fact that the webpage is technically already loaded?
    time.sleep(2)
    # find 1st available ref string on page -> newest updated
    all_ref_links = driver.find_element_by_class_name('url').text

    # formatted reflink to return
    reflink = "https://www.g2a.com/r/" + all_ref_links

    # split the title to decipher the information
    title = title.split()

    # platform is always 3rd last @ g2a
    platform = title[-3]
    # region always last @ g2a
    region = title [-1]
    # extract title
    title_formatted = "".join(word+" " for word in title[:-3])

    time.sleep(15)
    driver.close()
    driver.quit()

    return title_formatted, platform, region, reflink