from utils.autotrader_scraper import scrape_autotrader_info
from utils.excel_exporter import export_to_excel

# Define the URL of the AutoTrader listing
urls = [
'https://www.autotrader.co.uk/car-details/202412077088745?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ',
'https://www.autotrader.co.uk/car-details/202412317639076?fromSavedAds=true&advertising-location=at_cars&sort=relevance&postcode=CB58TJ'
]

# Call the scraping function and print the results
'''car_info = scrape_autotrader_info(url)
print("\nScraped Information:")
for key, value in car_info.items():
    print(f"{key}: {value}")'''

all_car_data = []
for url in urls:
    car_info = scrape_autotrader_info(url)
    #checks that the car info contains valid data and is not empty
    if car_info:
        all_car_data.append(car_info)

export_to_excel(all_car_data, output_file="car_info.xlsx")
