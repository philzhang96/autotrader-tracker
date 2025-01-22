'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.autotrader.co.uk/car-details/202501087851713?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"

def autotrader_scraper(url):
    #Fetching the page's content
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    
    #Extracting data from page
    price_element = soup.find("h2", {"data-testid": "advert-price"})
    if price_element:
        price_text = price_element.text.strip()
        print(f"Price: {price_text}")
'''
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def autotrader_scraper_selenium(url):
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("_tt_enable_cookie=1")  # Run in headless mode (no browser UI)
    driver_service = Service(r"C:\Windows\chromedriver-win64\chromedriver.exe")  # Update path to ChromeDriver
    driver = webdriver.Chrome(service=driver_service, options=options)

    # Fetch the page
    driver.get(url)
    
    # Wait for the page to load (adjust time if necessary)
    driver.implicitly_wait(10)
    
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    
    # Extract price
    price_element = soup.find("h2", {"data-testid": "advert-price"})
    if price_element:
        price_text = price_element.text.strip()
        print(f"Price: {price_text}")
    else:
        print("Price element not found")

# Example URL
url = "https://www.autotrader.co.uk/car-details/202501087851713?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"
autotrader_scraper_selenium(url)
