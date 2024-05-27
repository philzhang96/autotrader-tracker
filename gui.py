import tkinter as tk
from tkinter import ttk

def submit():
    make_selected = make_var.get()
    model_selected = model_var.get()
    print("Make:", make_selected)
    print("Model:", model_selected)

def create_gui(make_options, model_options):
    window = tk.Tk()
    window.title("Find your car")

    make_label = ttk.Label(window, text="Make")
    make_label.grid(row=0, column=0, padx=10, pady=5)
    make_var = tk.StringVar()
    make_dropmenu = ttk.Combobox(window, textvariable=make_var, state="readonly")
    make_dropmenu.grid(row=0, column=1, padx=10, pady=5)
    make_dropmenu['values'] = make_options

    model_label = ttk.Label(window, text="Model:")
    model_label.grid(row=1, column=0, padx=10, pady=5)
    model_var = tk.StringVar()
    model_dropmenu = ttk.Combobox(window, textvariable=model_var, state="readonly")
    model_dropmenu.grid(row=1, column=1, padx=10, pady=5)
    model_dropmenu['values'] = model_options

    submit_button = ttk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()
