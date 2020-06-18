import os
import sys
from seleniumrequests import Chrome
from selenium.webdriver import ChromeOptions
import time
from openpyxl import load_workbook, Workbook
import csv
from CarSpecs import *


def fb_number(radius):
    fb_numbers = [1, 2, 5, 10, 20, 40, 60, 80, 100, 250, 500]
    for i in fb_numbers:
        if i >= radius:
            return i


def search_autolist(car_specs):
    autolist_url = f"https://autolist.com/listings#make={car_specs.brand}&model={car_specs.model}"
    autolist_url += f"&price_min={car_specs.price_min}"
    autolist_url += f"&price_max={car_specs.price_max}"
    autolist_url += f"&year_min={car_specs.year_min}"
    autolist_url += f"&year_max={car_specs.year_max}"
    autolist_url += f"&radius={car_specs.search_radius}"
    driver.get(autolist_url)


def search_craigslist(car_specs):
    craigslist_url = f"https://westernmass.craigslist.org/search/cta?auto_make_model={car_specs.brand}" \
                     f"+{car_specs.model}"
    craigslist_url += f"&min_price={car_specs.price_min}"
    craigslist_url += f"&max_price={car_specs.price_max}"
    craigslist_url += f"&min_auto_year={car_specs.year_min}"
    craigslist_url += f"&max_auto_year={car_specs.year_max}"
    craigslist_url += f"&search_distance={car_specs.search_radius}"
    driver.get(craigslist_url)


def search_edmunds(car_specs):
    edmunds_url = f"https://www.edmunds.com/inventory/srp.html?make={car_specs.brand}&model={car_specs.model}/"
    edmunds_url += f"&price={car_specs.price_min}-"
    edmunds_url += f"{car_specs.price_max}"
    edmunds_url += f"&year={car_specs.year_min}-"
    edmunds_url += f"{car_specs.year_max}"
    edmunds_url += f"&radius={car_specs.search_radius}"
    driver.get(edmunds_url)


def search_fb(car_specs):
    fb_url = f"https://www.facebook.com/marketplace/107710392585440/vehicles?make={car_specs.brand}" \
             f"&model={car_specs.model}"
    fb_url += f"&minPrice={car_specs.price_min}"
    fb_url += f"&maxPrice={car_specs.price_max}"
    fb_url += f"&minYear={car_specs.year_min}"
    fb_url += f"&maxYear={car_specs.year_max}"
    driver.get(fb_url)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//div[@class="buofh1pr"]').click()
    driver.implicitly_wait(2)
    list_element = driver.find_element_by_xpath('//div[@aria-label="Radius"]').click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath(f'//*[text() = "{fb_number(car_specs.search_radius)} "]').click()
    apply_button = driver.find_element_by_xpath('//div[@aria-label="Apply"]')
    time.sleep(2)
    driver.execute_script("arguments[0].click()", apply_button)


def search_cr(car_specs):
    cr_url = f"https://inventory.consumerreports.org/cars/inventory/search?crMakeName={car_specs.brand}" \
             f"&crModelName={car_specs.model}"
    cr_url += f"&priceMin={car_specs.price_min}"
    cr_url += f"&priceMax={car_specs.price_max}"
    cr_url += "&crModelYear="
    for x in range(int(car_specs.year_min), int(car_specs.year_max)):
        cr_url += f"{x},"
    cr_url += f"&distance={car_specs.search_radius}"
    driver.get(cr_url)


def get_specs():
    brand = input("Brand: ")
    model = input("Model: ")
    price_min = input("Minimum Price: ")
    price_max = input("Maximum Price: ")
    year_min = input("Minimum Year: ")
    year_max = input("Maximum Year: ")
    search_radius = input("Search Radius: ")
    _specs = CarSpecs(brand, model, price_min, price_max, year_min, year_max, search_radius)
    return _specs


# Initializes chrome options
download_dir = os.getcwd() + r"\Homebase Spreadsheets"
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": download_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# Gets the path of the chromedriver, and creates it if it doesn't exist
executable_path = os.getcwd() + os.path.sep + 'chromedriver'
if sys.platform in ['win32', 'win64']:
    executable_path += ".exe"

# Initializing URLs
homebase_url = "https://app.joinhomebase.com/"

# Initializing driver
driver = Chrome(options=chrome_options, executable_path="%s" % executable_path)
current_specs = get_specs()
search_cr(current_specs)