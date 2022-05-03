from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

PATH = 'C:/webdrivers/chromedriver.exe'
PRICE_CLASS = 'tm-motors-search-card__price'
NAME_CLASS = 'tm-motors-search-card__title'
LINK = 'https://www.trademe.co.nz/a/motors/cars/bmw/search?bof=rfCE4bHM&user_region=70&year_min=2019&year_max=2022' \
       '&odometer_min=20000&odometer_max=40000&price_max=90000'


def get_data():
    # Get website
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(LINK)

    # Wait
    browser.implicitly_wait(5)

    # Get price as an array
    price = browser.find_elements(By.CLASS_NAME, PRICE_CLASS)

    name = browser.find_elements(By.CLASS_NAME, NAME_CLASS)

    name_vec = []
    price_vec = []

    # Print array
    for i in range(0, len(price)):
        name_vec.append(name[i].text)
        price_vec.append(price[i].text)
        # print(name_vec[i], price_vec[i])

    # Wait after close the tab
    time.sleep(3)
    browser.close()

    return name_vec, price_vec
