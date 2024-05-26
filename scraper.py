from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def scrape_makes_and_models():
    make_model_dict = {}

    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    
    # Navigate to the Autotrader website
    driver.get("https://www.autotrader.co.uk/")

    try:
        # Wait for make dropdown to be clickable
        make_dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchVehiclesMake")))
        make_select = Select(make_dropdown)

        # Get make options
        make_options = [option.text.strip() for option in make_select.options if option.text.strip()]
        
        # Iterate through each make
        for make_option in make_options:
            make_select.select_by_visible_text(make_option)
            WebDriverWait(driver, 10).until(EC.staleness_of(make_dropdown))
            
            # Wait for model dropdown to load dynamically
            model_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchVehiclesModel")))
            model_select = Select(model_dropdown)
            
            # Get model options
            model_options = [option.text.strip() for option in model_select.options if option.text.strip()]
            
            # Associate each model with the current make
            make_model_dict[make_option] = model_options

    except Exception as e:
        print("Error occurred while scraping:", e)

    finally:
        driver.quit()

    return make_model_dict

# Test the scraping function
print(scrape_makes_and_models())
