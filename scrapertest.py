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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def autotrader_scraper_selenium(urls):
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("_tt_enable_cookie=1")  # Run in headless mode (no browser UI)
    options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass bot detection
    options.add_argument("--window-size=1920,1080")  # Set a normal window size to mimic human behavior

    driver_service = Service(r"C:\Windows\chromedriver-win64\chromedriver.exe")  # Update path to ChromeDriver
    driver = webdriver.Chrome(service=driver_service, options=options)

    results = []

    for url in urls:
        try:
            print(f"Scraping: {url}")
            driver.get(url)

            # Wait for the price element to appear
            try:
                price_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//h2[@data-testid='advert-price']"))
                )
                price_text = price_element.text.strip()
            except:
                price_text = "Price not found"

            # Store the result
            results.append({"url": url, "price": price_text})

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            results.append({"url": url, "price": "Error fetching price"})

    driver.quit()

    # Print results
    for result in results:
        print(f"URL: {result['url']}\nPrice: {result['price']}\n")

# Example URLs
urls = [
    "https://www.autotrader.co.uk/car-details/202501087851713?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202409204270639?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"
]

autotrader_scraper_selenium(urls)

