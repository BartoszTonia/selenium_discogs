#!/usr/bin/env/ python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox(executable_path='./geckodriver')

def start_site(site):
    browser.maximize_window()
    browser.get(site)
    sleep(1)

def search_marketplace(position):
    browser.find_element_by_id("marketplace-search-form").click()
    browser.find_element_by_id("marketplace-search-input").send_keys(position)
    browser.find_element_by_id("marketplace-search-input").send_keys(Keys.RETURN)
    # browser.find_element_by_xpath("/html/body/div[3]/div[4]/div[4]/form/button").click()

def add_attributes():
    actual_site = browser.current_url
    browser.get(actual_site+"&ships_from=Poland&condition=Near+Mint+%28NM+or+M-%29&format=Vinyl")

start_site("https://www.discogs.com/sell/list")

search_marketplace("Prodigy")
add_attributes()

#
# browser.close()

