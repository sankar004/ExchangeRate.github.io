import tkinter as tk
import requests

def get_exchange_rate(base_currency, target_currency):
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def update_label(base_currency, target_currency, label):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    label.config(text=f"1 {base_currency} = {exchange_rate} {target_currency}")

root = tk.Tk()
root.title("Forex Reminder")

base_currency = "EUR"
target_currency = "USD"

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Refresh", command=lambda: update_label(base_currency, target_currency, label))
button.pack()

root.mainloop()
