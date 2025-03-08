from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def scrape_autotrader_info(driver, url, timeout=10):
    """
    Scrapes price, mileage, and registration year information from an AutoTrader car listing.
    Reuses the provided WebDriver session to avoid reopening the browser.
    
    Args:
        driver: Selenium WebDriver instance to reuse for multiple URLs.
        url (str): The URL of the AutoTrader car listing.
        timeout (int): Time in seconds to wait for elements to load.
        
    Returns:
        dict: A dictionary containing the scraped information or default values if the advert is sold.
    """
    try:
        driver.get(url)
        
        # Check if the advert is no longer available
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'The advert you are looking for is no longer available')]")
                )
            )
            print(f"Advert no longer available: {url}")
            return {
                "URL": url,
                "Price": "SOLD",
                "Mileage": "N/A",
                "Registration Year": "N/A"
            }
        except Exception:
            pass  # Continue with normal scraping if not sold
        
        # Define the XPaths for the required information
        xpaths = {
            "Make": "//h1[@data-testid='advert-title']",
            "Price": '//h2[contains(text(), "£")]',
            "Mileage": '//section//ul//li[contains(text(), "miles")]',
            "Registration Year": '//section//ul//li[contains(text(), "reg")]'
        }
        
        # Collect information using a single method
        car_info = {"URL": url}
        for key, xpath in xpaths.items():
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                text = element.text
                
                # If the key is "Mileage", extract only the numeric value and convert to int
                if key == "Mileage":
                    match = re.search(r"(\d+,?\d*)", text)
                    if match:
                        text = int(match.group(0).replace(",", ""))
                
                car_info[key] = text
                print(f"{key}: {text}")
            except Exception as e:
                car_info[key] = "N/A"
                print(f"Could not find {key}: {e}")
                
        return car_info
    
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
