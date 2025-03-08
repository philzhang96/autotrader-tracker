import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrape_autotrader_by_url(url):
    chrome_options = Options()
    chrome_options.add_argument("_tt_enable_cookie=1")  # Run in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        print(f"Accessing {url}...")
        
        time.sleep(5)  # Allow page to load
        
        source = driver.page_source
        content = BeautifulSoup(source, "html.parser")
        
        # Extract car listings
        articles = content.findAll("section", attrs={"data-testid": "trader-seller-listing"})
        
        data = []
        for article in articles:
            details = {
                "name": None,
                "year": None,
                "mileage": None,
                "owners": None,
            }
            
            # Extract name
            details["name"] = article.find("h3", attrs={"data-testid": "listing-title"}).text.strip()
            
            # Extract specs (year, mileage, owners)
            specs_list = article.find("ul", attrs={"data-testid": "search-listing-specs"})
            if specs_list:
                for spec in specs_list.find_all("li"):
                    if "reg" in spec.text.lower():  # Year
                        details["year"] = re.sub(r"\s+\(.*?\)", "", spec.text.strip())  # Clean " (xx reg)" part
                    elif "miles" in spec.text.lower():  # Mileage
                        details["mileage"] = spec.text.strip().replace(",", "").replace(" miles", "")
                    elif "owner" in spec.text.lower():  # Owners
                        details["owners"] = re.search(r"(\d+)\sowner", spec.text.lower())
                        if details["owners"]:
                            details["owners"] = details["owners"].group(1)
                        else:
                            details["owners"] = "Unknown"
            
            data.append(details)
        
        print(f"Scraped {len(data)} listings.")
        return data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    finally:
        driver.quit()


if __name__ == "__main__":
    # Example URL
    url = "https://www.autotrader.co.uk/car-details/202501188152626?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ"
    results = scrape_autotrader_by_url(url)
    
    for result in results:
        print(result)
