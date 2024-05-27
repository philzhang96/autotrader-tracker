from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

def scrape_autotrader():
    make_model_options = {}

    driver = webdriver.Chrome() 
    driver.get("https://www.autotrader.co.uk/")

    try:
        # Wait for the cookie consent notification to disappear
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, "sp_message_iframe_1086457")))

        # Scraping make options
        make_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "make")))
        make_options = [option.text.strip() for option in make_dropdown.find_elements(By.TAG_NAME, "option")]

        # Scraping models for each make
        for make in make_options:
            make_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "make")))
            select_make = Select(make_dropdown)
            
            try:
                select_make.select_by_visible_text(make)
            except NoSuchElementException:
                # Attempt to select the make using partial matching
                for option in make_dropdown.find_elements(By.TAG_NAME, "option"):
                    if make in option.text.strip():
                        option.click()
                        break

            # Retry mechanism to handle StaleElementReferenceException
            attempts = 0
            while attempts < 3:
                try:
                    # Locate the model dropdown
                    model_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "model")))
                    models = [option.text.strip() for option in model_dropdown.find_elements(By.TAG_NAME, "option")]
                    make_model_options[make] = models
                    break
                except StaleElementReferenceException:
                    attempts += 1
                    print("StaleElementReferenceException occurred. Retrying...")

            # Refresh the model dropdown element
            model_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "model")))

    finally:
        driver.quit()
    
    return make_model_options
