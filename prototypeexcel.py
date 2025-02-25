import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Output Excel file to save scraped data
OUTPUT_EXCEL_FILE = r"E:\Coding Projects\autotrader_data.xlsx"
# Input Excel file containing the URLs to scrape
INPUT_EXCEL_FILE = r"E:\Coding Projects\urls_input.xlsx"

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

    # Check if the output Excel file already exists
    if os.path.exists(OUTPUT_EXCEL_FILE):
        # Load existing data
        df_existing = pd.read_excel(OUTPUT_EXCEL_FILE, dtype=str)
        
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
    df_combined.to_excel(OUTPUT_EXCEL_FILE, index=False)

    print(f"\n✅ Data saved to {OUTPUT_EXCEL_FILE}")

    # Print results
    for result in results:
        print(f"URL: {result['URL']}\nMake: {result['Make']}\nPrice ({today_date}): {result[today_date]}\n")

if __name__ == '__main__':
    # Read the input Excel file containing the URLs.
    # Ensure that the Excel file has a column named 'URL'
    df_input = pd.read_excel(INPUT_EXCEL_FILE)
    urls = df_input["URL"].tolist()
    autotrader_scraper_selenium(urls)
