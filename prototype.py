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
    # Selenium must be run as "_tt_enable_cookie=1" otherwise will likely not work,
    options.add_argument("_tt_enable_cookie=1") 
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
    "https://www.autotrader.co.uk/car-details/202409204270639?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202502018634758?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202502038698884?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202502058754268?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501308577450?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501308559520?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202407011312408?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202412067072278?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202410295712702?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202306058163586?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202412036942163?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202412077088745?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202411156319287?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202410084967287?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202411146282450?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202302204461549?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202410295706788?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202405139652007?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202411015835018?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501037712516?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501087851713?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501087851713?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501218242382?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501188152626?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501238324828?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501158046351?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202412317639076?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"
]

autotrader_scraper_selenium(urls)

