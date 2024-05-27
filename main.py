from scraper import scrape_autotrader
from gui import create_gui

def main():
    make_options, model_options = scrape_autotrader()
    create_gui(make_options, model_options)

if __name__ == "__main__":
    main()
