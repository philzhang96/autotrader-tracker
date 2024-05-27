import tkinter as tk
from tkinter import ttk
from scraper import scrape_autotrader

def submit():
    make_selected = make_var.get()
    model_selected = model_var.get()
    print(f"Make: {make_selected}")
    print(f"Model: {model_selected}")

def update_models(event):
    selected_make = make_var.get()
    models = make_model_options.get(selected_make, [])
    model_dropmenu['values'] = models
    model_var.set('')

# Creating the main window
window = tk.Tk()
window.title("Autotrader Make/Model Selector")

# Calling the scraper function
make_model_options = scrape_autotrader()

# Creating and placing the Make dropdown menu
make_label = ttk.Label(window, text="Make")
make_label.grid(row=0, column=0, padx=10, pady=5)
make_var = tk.StringVar()
make_dropmenu = ttk.Combobox(window, textvariable=make_var, state="readonly")
make_dropmenu['values'] = list(make_model_options.keys())
make_dropmenu.grid(row=0, column=1, padx=10, pady=5)
make_dropmenu.bind("<<ComboboxSelected>>", update_models)

# Creating and placing the Model dropdown menu
model_label = ttk.Label(window, text="Model")
model_label.grid(row=1, column=0, padx=10, pady=5)
model_var = tk.StringVar()
model_dropmenu = ttk.Combobox(window, textvariable=model_var, state="readonly")
model_dropmenu.grid(row=1, column=1, padx=10, pady=5)

# Creating and placing the Submit button
submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
