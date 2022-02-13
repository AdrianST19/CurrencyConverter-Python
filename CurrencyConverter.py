from flask import request
import requests
import tkinter as tk

BASE_URL = "https://open.er-api.com/v6/latest/"

OptionList1 = [
    "USD",
    "EUR",
    "GBP",
    "RON",
    "AUD",
    "JPY",
    "CNY",
    "AED"
]

OptionList2 = [
    "USD",
    "EUR",
    "GBP",
    "RON",
    "AUD",
    "JPY",
    "CNY",
    "AED"
]


def Ok():

    fr = variable.get()
    to = variable1.get()

    amount = float(e1.get())

    request_url = f"{BASE_URL}{fr}"
    response = requests.get(request_url)
    data = response.json()
    value = data['rates'][to]
    tot = amount*value

    nsalText.set(tot)


root = tk.Tk()
root.geometry('300x200')
root.title("Currency Converter App")
root.configure(background='orange')

variable = tk.StringVar(root)
variable.set(OptionList1[0])

opt = tk.OptionMenu(root, variable, *OptionList1)
opt.config(width=10, font=('Helvetica', 12), background="white")
opt.pack(side="top")

variable1 = tk.StringVar(root)
variable1.set(OptionList2[0])

opt = tk.OptionMenu(root, variable1, *OptionList2)
opt.config(width=10, font=('Helvetica', 12), background="white")
opt.pack(side="top")

global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red', background="orange")
labelTest.pack(side="top")


tk.Label(root, text="From", background="orange").place(x=10, y=10)
tk.Label(root, text="To", background="orange").place(x=10, y=40)
tk.Label(root, text="Amount", background="orange").place(x=10, y=80)

tk.Label(root, text="Total:", background="orange").place(x=10, y=150)
tk.Label(root, text="", font=('Helvetica', 12), fg='blue', background="orange",
         textvariable=nsalText).place(x=100, y=150)
tk.Button(root, text="Calculate", background="green", command=Ok,
          height=1, width=9).place(x=100, y=110)

e1 = tk.Entry(root)
e1.place(x=80, y=80)

root.mainloop()
