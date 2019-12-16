#! usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import argparse

browser = webdriver.Firefox(executable_path='bin/geckodriver')

parser = argparse.ArgumentParser(description="Wyszukiwanie plyt vinylowych na Discogs")
parser.add_argument('-v', '--vinyl', dest="vinyl", type=str, help="pass vinyl title")


def start_site(site):

    browser.maximize_window()
    browser.get(site)

def search_marketplace(position):
    browser.find_element_by_id("onetrust-accept-btn-handler").click()
    browser.find_element_by_id("marketplace-search-input").send_keys(position)
    browser.find_element_by_id("marketplace-search-input").send_keys(Keys.RETURN)

def add_attributes():
    actual_site = browser.current_url
    browser.get(actual_site+"&ships_from=Poland&condition=Near+Mint+%28NM+or+M-%29&format=Vinyl")

start_site("https://www.discogs.com/sell/list")
sleep(2)
search_marketplace(parser.parse_args().vinyl)
sleep(3)
add_attributes()

# sleep(10000)
# browser.close()

