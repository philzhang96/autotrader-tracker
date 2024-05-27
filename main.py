from scraper import scrape_autotrader
from gui import create_gui

def main():
    make_model_options = scrape_autotrader()
    
    # Iterate over the dictionary to print makes and models
    for make, models in make_model_options.items():
        print(f"Make: {make}")
        print(f"Models: {models}")

if __name__ == "__main__":
    main()