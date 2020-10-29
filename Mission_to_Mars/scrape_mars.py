import os
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
featured_url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
table_url_mars = 'https://space-facts.com/mars/'


def Scrape():
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_results = soup.find_all('div', class_= "content_title")
    teaser_paragraph = soup.find_all('div', class_= "rollover_description_inner")
    return news_title= title_results[0].text
    teaser_paragraph = soup.find_all('div', class_= "rollover_description_inner")
    return news_p = teaser_paragraph[0].text

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(featured_url_jpl)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    browser.click_link_by_partial_text('.jpg')
    return featured_image_url = browser.url

    tables = pd.read_html(table_url_mars)
    df0 = tables[0]
    return mars_html_table = df0.to_html()



    
