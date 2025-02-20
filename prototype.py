import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXCEL_FILE = r"E:\Coding Projects\autotrader_data.xlsx"

def autotrader_scraper_selenium(urls):
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("_tt_enable_cookie=1") 
    options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass bot detection
    options.add_argument("--window-size=1920,1080")  # Set a normal window size to mimic human behavior

    driver_service = Service(r"C:\Windows\chromedriver-win64\chromedriver.exe")  # Update path to ChromeDriver
    driver = webdriver.Chrome(service=driver_service, options=options)

    results = []
    today_date = datetime.today().strftime('%d-%m-%Y')  # Get today's date

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

            # Getting the make of the car
            try:
                make_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[@data-testid='advert-title']"))
                )
                make_text = make_element.text.strip()
            except:
                make_text = "Make not found"

            # Store the result
            results.append({"URL": url, "Make": make_text, today_date: price_text})

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            results.append({"URL": url, "Make": "Error fetching make", today_date: "Error fetching price"})

    driver.quit()

    # Convert results to DataFrame
    df_new = pd.DataFrame(results)

    # Check if the Excel file already exists
    if os.path.exists(EXCEL_FILE):
        # Load existing data
        df_existing = pd.read_excel(EXCEL_FILE, dtype=str)
        
        # Print actual column names (debugging step)
        print("Original Columns in Excel:", df_existing.columns.tolist())

        # Ensure column names match expectations
        column_mapping = {
            "url": "URL",
            "make": "Make",
            "price": today_date  # If there is an old "price" column, replace it with today's date
        }

        df_existing.rename(columns={col: column_mapping[col] for col in df_existing.columns if col in column_mapping}, inplace=True)

        # Print updated column names
        print("Updated Columns After Renaming:", df_existing.columns.tolist())

        # Ensure required columns exist
        if "URL" not in df_existing.columns or "Make" not in df_existing.columns:
            raise KeyError(f"Existing Excel file still missing 'URL' or 'Make' after renaming. Found columns: {df_existing.columns.tolist()}")

        # Merge new data with existing data
        df_combined = df_existing.merge(df_new, on=["URL", "Make"], how="outer")
    else:
        df_combined = df_new

    # Save to Excel
    df_combined.to_excel(EXCEL_FILE, index=False)

    print(f"\n✅ Data saved to {EXCEL_FILE}")

    # Print results
    for result in results:
        print(f"URL: {result['URL']}\nMake: {result['Make']}\nPrice ({today_date}): {result[today_date]}\n")

# Example URLs
urls = [
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
    "https://www.autotrader.co.uk/car-details/202501218242382?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501188152626?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501238324828?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202501158046351?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ",
    "https://www.autotrader.co.uk/car-details/202412317639076?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"
]

autotrader_scraper_selenium(urls)

