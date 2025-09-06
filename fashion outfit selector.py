import tkinter as tk
from tkinter import ttk
import random

# Outfit suggestions for each occasion
outfits = {
    "Casual": [
        "Jeans with a white t-shirt and sneakers",
        "Summer dress with sandals",
        "Oversized hoodie with leggings"
    ],
    "Formal": [
        "Blazer with tailored pants and loafers",
        "White shirt with black skirt and heels",
        "Formal suit with tie"
    ],
    "Party": [
        "Sequin dress with heels",
        "Black shirt with slim jeans and boots",
        "Cocktail dress with clutch bag"
    ],
    "Workout": [
        "Sports bra with leggings and trainers",
        "Tank top with gym shorts",
        "Hoodie with joggers"
    ]
}

# Main window
root = tk.Tk()
root.title("Fashion Outfit Selector")
root.geometry("500x300")

# Label
title_label = tk.Label(root, text="Select an Occasion", font=("Arial", 14))
title_label.pack(pady=10)

# Dropdown menu
occasion_var = tk.StringVar()
occasion_dropdown = ttk.Combobox(root, textvariable=occasion_var)
occasion_dropdown["values"] = list(outfits.keys())
occasion_dropdown.current(0)
occasion_dropdown.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
result_label.pack(pady=20)

# Function to show outfit
def show_outfit():
    occasion = occasion_var.get()
    suggestion = random.choice(outfits[occasion])
    result_label.config(text=f"Suggested Outfit:\n{suggestion}")

# Button
btn = tk.Button(root, text="Get Outfit Suggestion", command=show_outfit)
btn.pack(pady=10)

root.mainloop()
