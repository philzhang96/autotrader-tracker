from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_autotrader_info(url, timeout=10):
    """
    Scrapes price, mileage, and registration year information from an AutoTrader car listing.
    
    Args:
        url (str): The URL of the AutoTrader car listing.
        timeout (int): Time in seconds to wait for elements to load.
        
    Returns:
        dict: A dictionary containing the scraped information.
    """
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(timeout)
    
    try:
        # Open the URL
        driver.get(url)
        
        # Define the XPaths for the required information
        xpaths = {
            "Price": '//h2[contains(text(), "£")]',
            "Miles": '//section//ul//li[contains(text(), "miles")]',
            "Registration Year": '//section//ul//li[contains(text(), "reg")]'
        }
        
        # Collect information using a single method
        car_info = {"URL": url}
        for key, xpath in xpaths.items():
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                car_info[key] = element.text
                print(f"{key}: {element.text}")
            except Exception as e:
                car_info[key] = None
                print(f"Could not find {key}: {e}")
                
        return car_info
    
    finally:
        driver.quit()
