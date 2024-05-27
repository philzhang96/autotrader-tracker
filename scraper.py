from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_autotrader():
    make_options = []
    model_options = []

    driver = webdriver.Chrome() 
    driver.get("https://www.autotrader.co.uk/")

    try:
        make_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "make")))
        make_options = [option.text.strip() for option in make_dropdown.find_elements(By.TAG_NAME, "option")]

        model_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "model")))
        model_options = [option.text.strip() for option in model_dropdown.find_elements(By.TAG_NAME, "option")]

    finally:
        driver.quit()
    
    return make_options, model_options