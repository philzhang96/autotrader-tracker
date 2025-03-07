from selenium import webdriver
from utils.autotrader_scraper import scrape_autotrader_info
from utils.excel_exporter import export_price_to_excel
from utils.data_importer import read_urls_from_excel
from utils.url_manager import remove_sold_urls

# Read URLs from an Excel file
urls = read_urls_from_excel(input_file="urls.xlsx", column_name="URL")

# Initialize a single WebDriver instance
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Scrape all URLs and collect data using the same driver session
all_car_data = []
sold_urls = []

for url in urls:
    car_info = scrape_autotrader_info(driver, url)
    if car_info:
        all_car_data.append(car_info)
        if car_info["Price"] == "SOLD":
            sold_urls.append(url)

# Export only the price data to the Excel file
export_price_to_excel(all_car_data, output_file="car_info.xlsx")

# Remove sold URLs from the input Excel file
remove_sold_urls(input_file="urls.xlsx", output_file="urls.xlsx", sold_urls=sold_urls)

# Close the WebDriver after all scrapes are complete
driver.quit()
