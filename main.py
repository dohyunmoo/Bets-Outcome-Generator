import tkinter as tk
import datetime
import sys
import json
import os

import data

total_data = {}

def isNum(num):
    try:
        float(num) or int(num)
        return True
    except:
        return False

def get_weekend():
    today = datetime.datetime.now()
    today_in_num = today.weekday()
    days_left = (5 - today_in_num) % 7 # if today = 6 (sunday), then -1 % 7 is 6 as -1 = 7(-1) + 6

    saturday = today + datetime.timedelta(days=days_left)
    sunday = saturday + datetime.timedelta(days=1)
    return saturday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

class window:
    def __init__(self, main, saturday, sunday) -> None:
        self.entry_arr_left = []
        self.entry_arr_right = []

        self.label_arr_left = []
        self.label_arr_right = []

        fight_night_date = None

        for i in range(len(data.main_data)):
            if data.main_data[i]["commence_time"][:10] == saturday or data.main_data[i]["commence_time"][:10] == sunday:
                fight_night_date = f'{saturday} / {sunday}'
                content = data.main_data[i]["bookmakers"]
                for j in range(len(content)):
                    if content[j]["key"] == 'draftkings':
                        self.label_arr_left.append(content[j]["markets"][0]["outcomes"][0])
                        self.label_arr_right.append(content[j]["markets"][0]["outcomes"][1])

        if len(self.label_arr_left) != len(self.label_arr_right):
            print("Error in the matches...")
            sys.exit()
        
        title = f'UFC FIGHT on {fight_night_date}'

        tk.Label(main, text=title).grid(row=0, column=2, columnspan=2, sticky=tk.NSEW, padx=10, pady=5)
        main.title(title)

        for i in range(len(self.label_arr_left)):
            l_left = tk.Label(main, text=f'{self.label_arr_left[i]["name"]}')
            odd_left = tk.Label(main, text=f'{self.label_arr_left[i]["price"]}')
            in_left = tk.Entry(main)
            self.entry_arr_left.append(in_left)

            l_right = tk.Label(main, text=f'{self.label_arr_right[i]["name"]}')
            odd_right = tk.Label(main, text=f'{self.label_arr_right[i]["price"]}')
            in_right = tk.Entry(main)
            self.entry_arr_right.append(in_right)

            l_left.grid(row=i+1, column=0, sticky=tk.W, pady=5)
            odd_left.grid(row=i+1, column=1, sticky=tk.W, pady=5)
            in_left.grid(row=i+1, column=2, sticky=tk.NSEW, padx=2, pady=5)

            in_right.grid(row=i+1, column=3, sticky=tk.NSEW, padx=2, pady=5)
            odd_right.grid(row=i+1, column=4, sticky=tk.E, pady=5)
            l_right.grid(row=i+1, column=5, sticky=tk.E, pady=5)

        calculate_button = tk.Button(main, text="Calculate", command=lambda: self.create_json(self.entry_arr_left, self.entry_arr_right))
        calculate_button.grid(row=len(self.label_arr_left)+1, column=2, columnspan=2, sticky=tk.NSEW, padx=10, pady=5)

    def create_json(self, input_left, input_right):
        if len(input_left) != len(self.label_arr_left) or len(input_right) != len(self.label_arr_right):
            print("the number of inputs on both sides do not match")
            sys.exit()

        for i in range(len(input_left)):
            if isNum(input_left[i]):
                total_data.update({self.label_arr_left[i]['name']: {'odd': self.label_arr_left[i]['price'], 'amount': input_left[i]}})
            elif isNum(input_right[i]):
                total_data.update({self.label_arr_right[i]['name']: {'odd': self.label_arr_right[i]['price'], 'amount': input_right[i]}})
            else:
                pass
        
        filename = "bets.json"

        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, "w") as f:
            json.dump(total_data, f)

if __name__ == "__main__":
    sat, sun = get_weekend()
    root = tk.Tk()
    window(root, sat, sun)
    root.mainloop()
