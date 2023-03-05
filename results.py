import json
import datetime
import sys

import data

def get_last_weekend():
    today = datetime.datetime.now()
    today_in_num = today.weekday()
    days_left = (5 - today_in_num) % 7 # if today = 6 (sunday), then -1 % 7 is 6 as -1 = 7(-1) + 6

    saturday = today + datetime.timedelta(days=(days_left - 7))
    sunday = saturday + datetime.timedelta(days=1)
    return saturday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

def main():
    main_data = None
    last_sat, last_sun = get_last_weekend()
    final_date = None
    try:
        with open(f"{last_sat}.json", "r") as f:
            main_data = json.load(f)
            final_date = last_sat
    except:
        try:
            with open(f"{last_sun}.json", "r") as f:
                main_data = json.load(f)
                final_date = last_sun
        except:
            print("cannot find the json file")
            sys.exit()

    total_payout = 0

    winners_list = data.get_event_result(data.get_event_data(final_date))

    for i in range(len(main_data)):
        for j in range(len(winners_list)):          
            if main_data[f'data{i}']['name'] == winners_list[j]:
                total_payout += main_data[f'data{i}']['odd'] * main_data[f'data{i}']['amount']
            else:
                pass

    return total_payout

if __name__ == '__main__':
    print(main())