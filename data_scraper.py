import os
import sys
from seleniumrequests import Chrome
from selenium.webdriver import ChromeOptions
import time
from openpyxl import load_workbook, Workbook
import csv
from CarSpecs import *
from Car import *


def search_all(car_specs):
    search_autolist(car_specs)
    search_craigslist(car_specs)
    search_edmunds(car_specs)
    search_fb(car_specs)
    search_cr(car_specs)


def search_autolist(car_specs):
    autolist_url = f"https://autolist.com/listings#make={car_specs.brand}&model={car_specs.model.replace(' ', '+')}"
    autolist_url += f"&price_min={car_specs.price_min}"
    autolist_url += f"&price_max={car_specs.price_max}"
    autolist_url += f"&year_min={car_specs.year_min}"
    autolist_url += f"&year_max={car_specs.year_max}"
    autolist_url += f"&radius={car_specs.search_radius}"
    autolist_url += f"&mileage={car_specs.mileage}"
    print(f"Autolist: {autolist_url}")
    driver.get(autolist_url)
    scrape_autolist()


def scrape_autolist():
    web_cars = driver.find_elements_by_xpath('//div[@class="vehicle-item-view"]')
    cars = []
    for x in web_cars:
        name = x.find_elements_by_xpath('.//div[@class="headline"]')[0].text
        cost = x.find_elements_by_xpath('.//div[@class="headline"]')[1].text
        cars.append(Car(name, cost))


def search_craigslist(car_specs):
    craigslist_url = f"https://westernmass.craigslist.org/search/cta?auto_make_model={car_specs.brand.lower()}" \
                     f"+{car_specs.model.lower()}"
    craigslist_url += f"&min_price={car_specs.price_min}"
    craigslist_url += f"&max_price={car_specs.price_max}"
    craigslist_url += f"&min_auto_year={car_specs.year_min}"
    craigslist_url += f"&max_auto_year={car_specs.year_max}"
    craigslist_url += f"&search_distance={car_specs.search_radius}&postal=01742"
    craigslist_url += f"&max_auto_miles={car_specs.mileage}"
    print(f"Craigslist: {craigslist_url}")
    driver.get(craigslist_url)


def search_edmunds(car_specs):
    edmunds_url = f"https://www.edmunds.com/inventory/srp.html?make={car_specs.brand.lower()}" \
                  f"&model={car_specs.model.lower().replace(' ', '-')}/"
    edmunds_url += f"&price={car_specs.price_min}-"
    edmunds_url += f"{car_specs.price_max}"
    edmunds_url += f"&year={car_specs.year_min}-"
    edmunds_url += f"{car_specs.year_max}"
    edmunds_url += f"&radius={car_specs.search_radius}"
    edmunds_url += f"&mileage=*-{car_specs.mileage}"
    print(f"Edmunds: {edmunds_url}")
    driver.get(edmunds_url)


def search_fb(car_specs):
    fb_url = f"https://www.facebook.com/marketplace/107710392585440/vehicles?make={car_specs.brand}" \
             f"&model={car_specs.model}"
    fb_url += f"&minPrice={car_specs.price_min}"
    fb_url += f"&maxPrice={car_specs.price_max}"
    fb_url += f"&minYear={car_specs.year_min}"
    fb_url += f"&maxYear={car_specs.year_max}"
    fb_url += f"&maxMileage={car_specs.mileage}"
    driver.get(fb_url)
    print("Facebook: " + fb_url)


def search_cr(car_specs):
    cr_url = f"https://inventory.consumerreports.org/cars/inventory/search?crMakeName={car_specs.brand}" \
             f"&crModelName={car_specs.model}"
    cr_url += f"&priceMin={car_specs.price_min}"
    cr_url += f"&priceMax={car_specs.price_max}"
    cr_url += "&crModelYear="
    if car_specs.year_min is not '' and car_specs.year_max is not '':
        for x in range(int(car_specs.year_min), int(car_specs.year_max)):
            cr_url += f"{x},"
    cr_url += f"&distance={car_specs.search_radius}"
    cr_url += f"&milesMax={car_specs.mileage}"
    print(f"Consumer Reports: {cr_url}")
    driver.get(cr_url)


def get_specs():
    brand = input("Brand: ")
    model = input("Model: ")
    price_min = input("Minimum Price: ")
    price_max = input("Maximum Price: ")
    year_min = input("Minimum Year: ")
    year_max = input("Maximum Year: ")
    search_radius = input("Search Radius: ")
    mileage = input("Maximum Mileage: ")
    _specs = CarSpecs(brand, model, price_min, price_max, year_min, year_max, search_radius, mileage)
    return _specs


# Initializes chrome options
download_dir = os.getcwd() + r"\Homebase Spreadsheets"
chrome_options = ChromeOptions()
# Gets the path of the chromedriver, and creates it if it doesn't exist
executable_path = os.getcwd() + os.path.sep + 'chromedriver'
if sys.platform in ['win32', 'win64']:
    executable_path += ".exe"
# Initializing driver
driver = Chrome(options=chrome_options, executable_path="%s" % executable_path)

# Gets the specs for the car
current_specs = get_specs()

# Searches for the car using the specs
search_all(current_specs)
