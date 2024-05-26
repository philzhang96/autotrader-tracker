import tkinter as tk
from tkinter import ttk
from scraper import scrape_makes_and_models

def on_make_select(event):
    selected_make = make_var.get()
    selected_models = make_model_dict.get(selected_make, [])
    model_var.set("")  # Clear the current selection
    model_dropmenu['values'] = selected_models

# Main code
window = tk.Tk()
window.title("Car Selector")

make_model_dict = scrape_makes_and_models()

make_var = tk.StringVar()
make_dropmenu = ttk.Combobox(window, textvariable=make_var, state="readonly")
make_dropmenu.grid(row=0, column=1, padx=10, pady=5)

model_var = tk.StringVar()
model_dropmenu = ttk.Combobox(window, textvariable=model_var, state="readonly")
model_dropmenu.grid(row=1, column=1, padx=10, pady=5)

make_options = list(make_model_dict.keys())
make_dropmenu['values'] = make_options

make_dropmenu.bind("<<ComboboxSelected>>", on_make_select)

window.mainloop()