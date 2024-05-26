from tkinter import Tk
from gui import setup_gui, on_make_select
from scraper import scrape_makes_and_models

def main():
    # Create the Tkinter root window
    root = Tk()
    root.title("Car Selector")

    # Set up the GUI
    setup_gui(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()