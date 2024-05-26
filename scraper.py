from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk

#Creating a function that does the scraping to collect the makes and models from Autotrader's website
def scrape():
    #Initialising variables
    make_options = []
    model_options = []

    # Set up Selenium WebDriver
    driver = webdriver.Chrome() 
    driver.get("https://www.autotrader.co.uk/")

    try:
        # Wait for make dropdown to load
        make_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "make")))
        make_options = [option.text.strip() for option in make_dropdown.find_elements(By.TAG_NAME, "option")]

        # Wait for model dropdown to load
        model_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "model")))
        model_options = [option.text.strip() for option in model_dropdown.find_elements(By.TAG_NAME, "option")]

    finally:
        driver.quit()  # Close the browser window when done scraping
    
    return make_options, model_options

# Retrieves the relevant information once the submit button has been clicked by the user
def submit():
    make_selected = make_var.get()
    model_selected = model_var.get()
    print("Make:", make_selected)
    print("Model:", model_selected)

# Creating GUI window for users to select their make and model
window = tk.Tk()
window.title("Find your car")

# Creating the Car Makes' dropdown menu
make_label = ttk.Label(window, text="Make")
make_label.grid(row=0, column=0, padx=10, pady=5)
make_var = tk.StringVar()
make_dropmenu = ttk.Combobox(window, textvariable=make_var, state="readonly")
make_dropmenu.grid(row=0, column=1, padx=10, pady=5)

# Creating the Car Models' dropdown menu
model_label = ttk.Label(window, text="Model:")
model_label.grid(row=1, column=0, padx=10, pady=5)
model_var = tk.StringVar()
model_dropmenu = ttk.Combobox(window, textvariable=model_var, state="readonly")
model_dropmenu.grid(row=1, column=1, padx=10, pady=5)

# Utilising Scrape function to populate dropdown menu
make_options, model_options = scrape()
make_dropmenu['values'] = make_options
model_dropmenu['values'] = model_options

# Creating submit button
submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2,padx=10, pady=10)

window.mainloop()
